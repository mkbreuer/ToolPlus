# ##### BEGIN GPL LICENSE BLOCK #####
#
#  Copyright (C) 2014-2017 script authors.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


# LOAD MODULS FROM PHYTON LIBS. #
import sys, subprocess, re, os, threading, struct, pprint

# LOAD MODULS FROM BLENDER LIBS. #
import bpy, bgl, blf
from bpy import*
from bpy.props import*
from bpy.types import AddonPreferences, Operator, PropertyGroup
from bpy_extras.io_utils import ExportHelper


# FUTURE: How to handle default folder + no thumbnail icon with different themes?
# FUTURE: Add possibility to re-render thumbs or update theme using a different thumbnail scene.
# FUTURE: Support multiple asset dirs? Not really useful, could be done file system wise.
# FUTURE: Render append/link from single components.
# FUTURE: Performance optimization: Cache several cost intensive calls:
#         - Theme settings .. 
#         - Preferences
# FUTURE: Option to rename and/or center on safe.
# FUTURE: User adjustable GUI colors, use theme by default (maybe other theme colors then currently?)
# FUTURE: Better error handling? Were catch errors? User feedback will be helpful.

# Various functions to access paths inside the addon directory.
def assetFlingerHome(): return os.path.dirname(__file__)
def assetFlingerIcons(): return os.path.join(assetFlingerHome(), "icons")
def assetFlingerThumbnailer(): return os.path.join(assetFlingerHome(), "thumbnailer")

def log(s):
    """
    Central log fn, lets modify logging behavior in a single place.
    """
    print("[asset-flinger, %5i] - %s" % (threading.get_ident(), s))
    
def objPath(path): return os.path.splitext(path)[0] + ".obj"
def blendPath(path): return os.path.splitext(path)[0] + ".blend"     


# https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running
def execute(cmd):
    """
    Runs an external application, in this case the blender executable for
    thumbnail generation. Returns all lines written by this application to stdout
    immediately on a line by line basis.
    """
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    _ = popen.wait()
    #if return_code:
    #    raise subprocess.CalledProcessError(return_code, cmd)

def createThumbnail(scene):
    """
    Used to create the thumbnail for the object specified in parameter 'scene', full path
    is required. 
    """
    log("*** CALL THUMBNAIL GEN ***")
    blenderExecutable = bpy.app.binary_path
    thumbscene = os.path.join(assetFlingerThumbnailer(), "Thumbnailer" + preferences().thumbnailScenePostfix() + ".blend")

    # Parse 'Tracing Sample' output to show as progress.
    ptrn = re.compile(".*Path Tracing Sample\\s+(\\d+)/\\d+.*")
    wm = bpy.context.window_manager
    wm.progress_begin(0, 300)
    
    # Run external instance of blender like the original thumbnail generator.
    cmd = [
        blenderExecutable, 
        "-b", thumbscene, 
        "--python-text", "ThumbScript", 
        "--", 
        "obj:" + scene, 
        "size:" + preferences().thumbnailRenderSize()
        ]
    log(repr(cmd))
    
    for l in execute(cmd):
        # Log special prefixed lines (using log/log_object functions in thumbnail scripts).
        if l.startswith("[log]"):
            log(l.strip()[5:])

        # If contains progress analyze and update progress.
        pts = ptrn.match(l)
        if pts:
            wm.progress_update(int(pts.group(1)))
            sys.stdout.write("\r%f %%" % (float(pts.group(1))/3))
            sys.stdout.flush()

    print("")
    wm.progress_end()

def preferences():
    """
    Return the instance of the AF user preferences.
    :rtype AssetFlingerPreferences
    """

#    addon_key = __package__.split(".")[0]    
#    panel_prefs = context.user_preferences.addons[addon_key].preferences

    return bpy.context.user_preferences.addons[__package__].preferences

def importObject(filename, link):
    """
    Imports the specified object, prefer .blend if available, otherwise take .obj.
    """
    # Deselect all, otherwise they were moved to the cursor position too.
    for obj in bpy.data.objects:
        obj.select = False
    
    # Cut off extension, import object by extension preference.
    basename, _ = os.path.splitext(filename)
    log("Import object '%s'" % basename)

    # Prefer the blend to .obj.
    blend = basename + ".blend"
    if os.path.exists(blend):
        log("Use .blend version, link = %s" % repr(link))
#         # https://blender.stackexchange.com/questions/34540/how-to-link-append-a-data-block-using-the-python-api
#         with bpy.data.libraries.load(basename + ".blend", link = link) as (dfrom, dto):
#             dto.objects = dfrom.objects
# 
#         for obj in dto.objects:
#             if obj is not None:
#                 log("  Append: %s" % obj)
#                 bpy.context.scene.objects.link(obj)

        # https://blender.stackexchange.com/questions/34299/appending-with-bpy-data-libraries-load-and-drivers
        files = []
        with bpy.data.libraries.load(blend) as (data_from, _):
            for name in data_from.objects:
                files.append({'name': name})

        if link:
            bpy.ops.wm.link(directory=blend + "/Object/", files=files)
        else:
            bpy.ops.wm.append(directory=blend + "/Object/", files=files)

    # OK hopefully the obj exists.
    elif os.path.exists(basename + ".obj"):
        log("Use .obj version")
        bpy.ops.import_scene.obj(filepath=basename + ".obj")
        
    # In case we link, don't move to cursor.
    if not link:        
        bpy.ops.view3d.snap_selected_to_cursor()
        
    bpy.context.scene.objects.active = bpy.context.selected_objects[0]

class RenderTools:
    """
    Handle drawing functionality in one place. If future versions of blender
    have a different API, changes are restricted to this class.
    """
    @staticmethod
    def renderTexture(texture, x, y, width, height):
        bgl.glEnable(bgl.GL_BLEND)
        #bgl.glBlendFunc(bgl.GL_SRC_ALPHA, bgl.GL_ONE_MINUS_SRC_ALPHA)

        texture.gl_load()
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, texture.bindcode[0])

        bgl.glEnable(bgl.GL_TEXTURE_2D)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEAREST)
        bgl.glTexParameteri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEAREST)

        bgl.glColor4f(1, 1, 1, 1)

        bgl.glBegin(bgl.GL_QUADS)
        bgl.glTexCoord2d(0, 0)
        bgl.glVertex2d(x, y)
        bgl.glTexCoord2d(0, 1)
        bgl.glVertex2d(x, y + height)
        bgl.glTexCoord2d(1, 1)
        bgl.glVertex2d(x + width, y + height)
        bgl.glTexCoord2d(1, 0)
        bgl.glVertex2d(x + width , y)
        bgl.glEnd()

        texture.gl_free()

    @staticmethod
    def renderRect(color, x, y, width, height):
        bgl.glEnable(bgl.GL_BLEND)
        bgl.glColor4f(color[0], color[1], color[2], color[3])
        bgl.glRectf(x, y, x + width, y + height)

    @staticmethod
    def renderText(color, x, y, size, text, dpi = 72):
        bgl.glEnable(bgl.GL_BLEND)
        bgl.glColor4f(color[0], color[1], color[2], color[3])

        font_id = 0
        blf.position(font_id, x, y - size / 2, 0)
        blf.size(font_id, size, dpi)
        blf.draw(font_id, text)









class MenuItem:
    """
    Represents an existing asset or folder. Handles drawing of the visual representation
    as well as every user interaction with it.
    """
    def __init__(self, texture, deco, text, folderInfo = None, assetInfo = None):
        self._texture = texture
        self._deco = deco
        self._text = text
        self._folderInfo = folderInfo
        self._assetInfo = assetInfo

    def append(self, x, y):
        """
        Check relative mouse position for appending area.
        """
        return y > 95 and y < 120

    def link(self, x, y):
        """
        Check relative mouse position for link area (false for obj).
        """
        return self._assetInfo[1] and y > 70 and y < 95

    def draw(self, rect, mouse):
        """
        Draws the menu item in the given rect.
        """
        x, y, w, h = rect
        mx, my = mouse[0] - x, mouse[1] - y
        isInside = mx >= 0 and mx < w and my >= 0 and my < h

        p = preferences()
        margins = p.menuItemMargins()
        iconSize = p.iconSize()
        
        texts = p.itemTextSize()
        ttexts = p.toolTipTextSize()
        textc = p.itemTextColor()
        textcs = p.itemTextColorSelected()
        textx = x + margins + p.underlayWidth()

        # Render background rectangle.
        RenderTools.renderRect(
            p.menuColorSelected() if isInside else p.menuColor(),
            x + margins,
            y + margins,
            w - 2 * margins,
            h - 2 * margins
        )

        # Render a type specific background.
        RenderTools.renderTexture(
            self._deco,
            x + 2 * margins,
            y + margins,
            p.underlayWidth(),
            iconSize
        )

        # Render icon.
        RenderTools.renderTexture(
            self._texture,
            x + 2 * margins,
            y + margins,
            iconSize,
            iconSize
        )

        # Render text for asset.
        RenderTools.renderText(
            textcs if isInside else textc, 
            textx, 
            y + 26, 
            texts, 
            self._text
        )

        if self._assetInfo:
            _, blendExists, renderer = self._assetInfo
            append, link = False, False
            
            if isInside:
                if self.append(mx, my):
                    append = True
                    renderer.setInfo("Append object '%s' to scene ..." % self._text)

                if self.link(mx, my):
                    link = True
                    renderer.setInfo("Link object '%s' to scene ..." % self._text)

            if append:
                RenderTools.renderText((*textcs[0:3], 1), textx, y + 107, ttexts, "Click to append")
            else:
                RenderTools.renderText((*textcs[0:3], 0.3), textx, y + 107, ttexts, "Click to append")
                
            if blendExists:
                if link:
                    RenderTools.renderText((*textcs[0:3], 1), textx, y + 82, ttexts, "Click to link")
                else:
                    RenderTools.renderText((*textcs[0:3], 0.3), textx, y + 82, ttexts, "Click to link")

    def testClick(self, rect, mouse):
        """
        Handle user click, can be everywhere!
        """
        x, y, w, h = rect
        mx, my = mouse[0] - x, mouse[1] - y
        isInside = mx >= 0 and mx < w and my >= 0 and my < h

        # If clicked inside this instance ...
        if isInside:
            # Check if its a folder entry ..
            if self._folderInfo:
                # Update menu in renderer.
                full, _, renderer = self._folderInfo
                renderer.setMenuItems(MenuItem.buildListForFolder(*self._folderInfo))
            elif self._assetInfo:
                # If this is an asset, import, link or whatever.
                full, _, renderer = self._assetInfo

                # Decide whether append or link (if supported).
                if self.append(mx, my):
                    importObject(full, False)
                    renderer.setFinished()

                if self.link(mx, my):
                    importObject(full, True)
                    renderer.setFinished()

    @staticmethod
    def buildListForFolder(path, level, renderer):
        """
        Create the list of menu items for the given path. Level
        is used to determine if the top level has been reached (.. prevented).
        """
        r = []
        if level != 0:
            r.append(MenuItem(
                renderer.folderIcon(),
                renderer.decoDirIcon(),
                "..",
                folderInfo = (os.path.abspath(os.path.join(path, os.pardir)), level - 1, renderer)
            ))

        # Folders first ...
        for e in sorted(os.listdir(path)):
            full = os.path.join(path, e)
            if os.path.isdir(full):
                r.append(MenuItem(
                    renderer.folderIcon(),
                    renderer.decoDirIcon(),
                    e,
                    folderInfo = (full, level + 1, renderer)
                ))

        for e in sorted(os.listdir(path)):
            full = os.path.join(path, e)
            basename, ext = os.path.splitext(full)
            if ext.lower() == ".obj":
                iconImage = basename + ".png"
                icon = renderer.loadIcon(iconImage, False) if os.path.exists(iconImage) else renderer.noThumbnailIcon()
                blendExists = os.path.exists(basename + ".blend")
                deco = renderer.decoBlendIcon() if blendExists else renderer.decoObjIcon()
                if not os.path.isdir(full):
                    r.append(MenuItem(
                        icon,
                        deco,
                        os.path.basename(basename),
                        assetInfo = (full, blendExists, renderer)
                    ))

        return r

class ScreenRenderer:
    """
    Handles the rendering of the asset selection OSD as well as user interaction
    with the OSD. Manages loaded textures and cleans them up when calling dispose() which
    is done before releasing the object.
    """
    def __init__(self):
        self._dbg = ""
        self._nfo = ""
        self._finished = False

        # Last known mouse positions.
        self._mouseX = -1
        self._mouseY = -1

        # Store screen dimension in last draw call.
        self._width = -1
        self._height = -1

        # Scroll through assets.
        self._scrollPos = 0
        self._maxScroll = 0

        # Limit the asset menu area (for e.g. later additions).
        self._menuTop = 20

        self._items = []

        # Lists to store info about loaded textures (for later cleanup).
        self._genericIcons = []
        self._specificIcons = []

        # Some icons for multiple uses.
        self._folderIcon = self.loadIcon(os.path.join(assetFlingerIcons(), "folder.png"), True)
        self._noThumbnailIcon = self.loadIcon(os.path.join(assetFlingerIcons(), "nothumbnail.png"), True)
        self._decoObjIcon = self.loadIcon(os.path.join(assetFlingerIcons(), "button-decoration-obj.png"), True)
        self._decoBlendIcon = self.loadIcon(os.path.join(assetFlingerIcons(), "button-decoration-blend.png"), True)
        self._decoDirIcon = self.loadIcon(os.path.join(assetFlingerIcons(), "button-decoration-dir.png"), True)

    def loadIcon(self, path, generic):
        """
        Load icon as texture and return id. Stores information for later cleanup in one
        of the internal lists. One will cleanup of on every folder change, the other on final cleanup.
        """
        log("Load image: " + path)
        tid = bpy.data.images.load(filepath = path, check_existing = True)
        if generic:
            self._genericIcons.append(tid.filepath_raw)
        else:
            self._specificIcons.append(tid.filepath_raw)
        #log("   RAW: " + tid.filepath_raw)
        return tid

    def freeImages(self, lst):
        """
        Free textures not needed anymore.
        """
        for image in bpy.data.images:
            if image.filepath_raw in lst:
                #log("CLEAN TEX:" + image.filepath_raw)
                image.user_clear()
                bpy.data.images.remove(image, do_unlink = True)
        lst.clear()

    def dispose(self):
        """
        Called on termination, frees all loaded resources.
        """
        self.freeImages(self._genericIcons)
        self.freeImages(self._specificIcons)

    def folderIcon(self): return self._folderIcon
    def noThumbnailIcon(self): return self._noThumbnailIcon
    def decoObjIcon(self): return self._decoObjIcon
    def decoBlendIcon(self): return self._decoBlendIcon
    def decoDirIcon(self): return self._decoDirIcon

    def setMenuItems(self, items):
        """
        Set new list of menu items.
        """
        # Clear previous resources.
        #self.freeImages(self._specificIcons)
        self._items = items

    def setFinished(self):
        """
        Set finish state from outside (used after asset load).
        """
        self._finished = True

    def isFinished(self):
        """
        Reports if finished is reached (if asset has been load or any user interaction).
        """
        return self._finished
    
    def setInfo(self, s):
        self._nfo = s

    def renderInfo(self, height):
        """
        Render textual info in the top area.
        """
        if len(self._nfo) > 0:
            RenderTools.renderText((0.8, 0.8, 0.8, 1), 5, height - 8, 16, self._nfo)

    def renderDebug(self, width):
        """
        Render text in the lower area.
        """
        if len(self._dbg) > 0:
            RenderTools.renderRect(preferences().bgColor(), 0, 0, width, self._menuTop)
            RenderTools.renderText((0.6, 0.6, 1, 1), 5, 8, 16, self._dbg)

    def scrollArea(self, _, width, height):
        """
        Total height of all menu items. Used to determine scroll area.
        """
        count = len(self._items)
        itemsPerLine = round(width / preferences().menuItemWidth())
        lines = round(count / itemsPerLine) + (1 if (count % itemsPerLine) != 0 else 0)
        maxHeight = lines * preferences().menuItemHeight()
        displayHeight = height - self._menuTop

        if displayHeight >= maxHeight:
            return 0
        return maxHeight - displayHeight

    def calcMenuItemRect(self, index, _, width, height):
        """
        Based on valid area size, return the position of item number 'index', if count items should be rendered.
        """
        itemsPerLine = round(width / preferences().menuItemWidth())
        effectiveItemWidth = width / itemsPerLine

        col = index % itemsPerLine
        row = int(index / itemsPerLine)

        # self._dbg = "w: %f, c: %f, ipl: %f, lns: %f, eiw: %f" % (width, count, itemsPerLine, lines, effectiveItemWidth)
        # log("%i - %f, %f" % (index, row, col))
        # print((
        #     col * effectiveItemWidth,
        #     height - row * preferences().menuItemHeight(),
        #     effectiveItemWidth,
        #     preferences().menuItemHeight()
        # ))

        return (
            col * effectiveItemWidth,
            height - (row + 1) * preferences().menuItemHeight() - self._menuTop + self._scrollPos,
            effectiveItemWidth,
            preferences().menuItemHeight()
        )

    def draw(self, width, height):
        self._nfo = "Press ESC or RMB to cancel ..."
        self._width = width
        self._height = height

        # Render the background darker.
        RenderTools.renderRect(preferences().bgColor(), 0, 0, width, height)

        # Update scroll info.
        self._maxScroll = self.scrollArea(len(self._items), width, height)
        if self._scrollPos > self._maxScroll:
            self._scrollPos = self.maxScroll
        #self._dbg = "%f" % self._maxScroll

        # Limit drawing area.
        #bgl.glScissor(0, 0, width, height - self._menuTop)
        #bgl.glEnable(bgl.GL_SCISSOR_TEST)

        # Render the menu items.
        if not self._items:
            # Show informational text at the top.
            self._nfo = "No items in asset folder, verify path (%s)." % preferences().custom_library_path
        else:
            # Render item by item.
            for index, e in enumerate(self._items):
                # The target rectangle, based on current view size.
                itemRect = self.calcMenuItemRect(index, len(self._items), width, height)
                e.draw(itemRect, (self._mouseX, self._mouseY))

        #bgl.glDisable(bgl.GL_SCISSOR_TEST)

        # Render another dark rectangle on top (info area).
        RenderTools.renderRect(preferences().bgColor(), 0, height - self._menuTop, width, self._menuTop)
        self.renderInfo(height)
        
        self.renderDebug(width)

        # Cleanup render states.
        bgl.glDisable(bgl.GL_BLEND)
        bgl.glDisable(bgl.GL_TEXTURE_2D)

    def mouseMove(self, x, y):
        self._mouseX = x
        self._mouseY = y

    def mouseClick(self, x, y, button, event):
        #self._dbg = "%f, %f, %s, %s" % (x, y, button, event)
        # Prevent crash.
        if self._width < 1 or self._height < 1:
            return

        if button == "LEFTMOUSE" and event == "RELEASE":
            for index, e in enumerate(self._items):
                # The target rectangle, based on current view size.
                itemRect = self.calcMenuItemRect(index, len(self._items), self._width, self._height)
                e.testClick(itemRect, (x, y))

        if button == "RIGHTMOUSE":
            self._finished = True

    def wheel(self, up):
        """
        Handle mouse wheel event.
        """
        scrollAmount = 72
        if not up:
            self._scrollPos += scrollAmount
            if self._scrollPos > self._maxScroll:
                self._scrollPos = self._maxScroll
        else:
            self._scrollPos = 0 if self._scrollPos < scrollAmount else self._scrollPos - scrollAmount

    def otherEvent(self, event):
        if event.type == "ESC":
            self._finished = True


class AssetFlingerMenu(Operator):
    """
    Renders the OSD menu to select an existing asset for import.
    """
    bl_idname = "view3d.asset_flinger"
    bl_label = "Asset Flinger"
    bl_options = {'REGISTER', 'UNDO'}

    def __init__(self):
        self._renderer = None
        self._handle = None

    def modal(self, context, event):
        context.area.tag_redraw()

        # Forward several events to the renderer.
        if event.type == 'MOUSEMOVE':
            self._renderer.mouseMove(event.mouse_region_x, event.mouse_region_y)
        elif event.type == "LEFTMOUSE" or event.type == "MIDDLEMOUSE" or event.type == "RIGHTMOUSE":
            self._renderer.mouseClick(event.mouse_region_x, event.mouse_region_y, event.type, event.value)
        elif event.type == "WHEELUPMOUSE" or event.type == "WHEELDOWNMOUSE":
            self._renderer.wheel(event.type == "WHEELUPMOUSE")
        else:
            #log(repr(event.type))
            self._renderer.otherEvent(event)

        # Check if renderer signals that it can be removed.
        if self._renderer.isFinished():
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            self._renderer.dispose()
            self._renderer = None
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        """
        Called if user triggers the operator. Adds a custom render callback.
        """
        # Only this area type is supported.
        if context.area.type == 'VIEW_3D':
            self._renderer = ScreenRenderer()
            assets = preferences().custom_library_path
            if len(assets) > 0:
                self._renderer.setMenuItems(MenuItem.buildListForFolder(assets, 0, self._renderer))
            self._handle = bpy.types.SpaceView3D.draw_handler_add(self.drawCallback, (context, ), 'WINDOW', 'POST_PIXEL')
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot show asset flinger")
            return {'CANCELLED'}

    def drawCallback(self, context):
        self._renderer.draw(
            context.area.regions[4].width,
            context.area.regions[4].height
        )

class AssetFlingerExport(Operator, ExportHelper):
    """
    Manages all export related tasks. Uses ExportHelper for export file selection.
    """
    bl_idname = "export.asset_flinger"
    bl_label = "Asset Flinger Model Export"
    bl_options = {'REGISTER'}

    # Exporter stuff.
    filename_ext = ".blend"
    filter_glob = StringProperty(default="*.blend", options={'HIDDEN'})

    def execute(self, context):
        """
        This gets called after user has selected a file for export.
        """
        ###########################################
        # .blend export

        # https://docs.blender.org/api/blender_python_api_2_77_1/bpy.types.BlendDataLibraries.html
        log("Export as .blend")
        bpy.data.libraries.write(
            blendPath(self.properties.filepath), 
            set(bpy.context.selected_objects), 
            relative_remap = True
        )

        ###########################################
        # .obj export and thumb generation

        # Write wavefront obj to file.
        log("Export as .obj");
        bpy.ops.export_scene.obj(
            filepath = objPath(self.properties.filepath),
            use_selection = True,
            use_mesh_modifiers = True,
            use_materials = False
        )

        # Run thumbnail generator for this .obj.
        log("Create thumbnail.")
        createThumbnail(
            objPath(self.properties.filepath)
        )

        ###########################################
        # Done
        log("Completed.")
        return {'FINISHED'}










