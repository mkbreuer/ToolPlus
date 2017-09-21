Blender TuneUp 0.5

DOCUMENTATION:

	This addons performs major modifications on top of the default Blender settings in order to improve usability and provide a better workflow. 
	
	List of modifications:

		- Keyboard: Allows you to separate custom key shortcuts from default Blender configuration in order to make it easier to port them to new versions or other machines.
		You can edit data.json, inside the addon's folder, in order to add your custom shortcuts and load them through the addon. (see configuration file for details)

		- User Preferences:  You can edit data.json to store your custom settings and load them through the addon. 

		- Blender Panels: Lets you remove panels from the interface. Many of them are innecessary or duplicated taking screen space, which can be used for another new functionality.

		- New Menus: 
			- Object's specials menu (W key)
			 has been improved so you dont have to access the properties panel in order to perform common operations like shade flat/smooth or change the display or make the object selectable...
			- Curve Menu (W Key)
			Added show/hide handles and normals

			- Quickly change layout (F5)
			You can enable this menu by pressing the loading keyboard button. It display a pie menu where you can change the screen layout, editor type or access any properties panel area.

			- Headers Buttons
			A button with a red crossed ghost icon is added to the 3D view, Image/UV and  dopesheet editor in order to remove deleted data, like meshes, materials, images, textures...
			These buttons are contextual so the uv/image editor will only purge images or textures, the dopesheet will delete animations and the 3d view all of them at once.

		- New functionality.
			See "Operators Loaded" section below.
			This functionality is optional as soon as you dont bind it to any shortcut.

		- Purge data:
			A 3 new buttons, with a red crossed ghost icon, has been placed in the 3dview,
			image and dopesheet editors in order to preform a selective remove of unsued datablocks.
			- 3dview ghost will purge anything that is not being used
			- image editor will only purge unused textures
			- dopesheet editor will only purge animations

Profiles:
	Loads/Saves Blender current configuration. 
	- Save: it will create two zip files and store the local and user profile files. These are the startup file, user preferences and installed addons.
	- Load: It will replace all those files. The addons wont be overwritten so if you are moving to a newer blender version, the addons will be respected but it will install all the missing ones.
	- Open Configs: Opens the folder where the profiles are stored.

Configuration:
	It will read the file "data.json" and pull user preferences or keyboard setup or panels to destroy.

	Load Keyboard: Loads keyboard setup from data.json.
	Load Preferences: Loads preferences from data.json.
	Load Panels: Loads panels names to destroy.
	Open Config: Opens the file data.json

Operators Loaded:
	Description of all the new functionality.

	v0.5:
	- curve.primitive_bezier_curve_add: "Adds a bezier curve as a straight line with automatic handles"
	- curve.select_path: "Allows to select intermediate points between 2 selected points"
	- graph.show_toggle: "Shows/Hides/Solo selected animation curves"
	- mesh.select_pair_rings: "Select rings each two or more loops" (in development)
	- mesh.smart_mark_seam: "Toggles mark seams"
	- uv.smap_pin: "Toggles pin uv"
	- uv.smart_select: "Allows sync Uv editor with mesh select modes"


