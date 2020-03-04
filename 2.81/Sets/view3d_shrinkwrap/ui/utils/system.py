import os


def makedir(pathstring):
    if not os.path.exists(pathstring):
        os.makedirs(pathstring)
    return pathstring


def open_folder(path):
    import platform
    import subprocess

    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        # subprocess.Popen(["xdg-open", pathstring])
        os.system('xdg-open "%s" %s &' % (path, "> /dev/null 2> /dev/null"))  # > sends stdout,  2> sends stderr


def get_new_directory_index(path):
    pngs = [f for f in sorted(os.listdir(os.path.join(path, 'icons'))) if os.path.isfile(os.path.join(path, 'icons', f)) and f.endswith('.png')]

    index = "001"

    while pngs:
        last = pngs.pop(-1)
        try:
            index = str(int(last[:3]) + 1).zfill(3)
            break
        except:
            pass

    return index
