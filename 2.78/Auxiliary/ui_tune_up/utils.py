from bpy.ops import op_as_string
import os, re, json

dev = False

path = __file__

if dev:
	path = "D:\\Blender Foundation\\Blender\\2.72\\scripts\\addons\\ui_tune_up"

#debug dump variables
def dd(*value, dodir=0, vert=0):

	if dev:
		if dodir: 
			print(30*"-")
			print(dir(value))
		elif vert:
			for v in value[0]:
				print(v)
		else:
			n = len(value)
			pattern = n * "%s "
			value = pattern % value
			print(value)

def operator_exists(idname):
   try:
	   op_as_string(idname)
	   return True
   except:
	   return False

#compose a filename with the addon path
def p(file, open_folder = False):
	file = os.path.join(path, file)
	if open_folder:
		os.startfile(os.path.dirname(file))
	return file

def load_json(file):
	data = []
	#strip comments 
	with open(p(file), "r") as f:
		data = f.read()
		#strip // comments
		regex = re.compile("//.+", re.MULTILINE)
		data = re.sub(regex, "", data)
	try:
		data = json.loads(data)
	except Exception as e:
		return "Config Error: " + e.args[0]
	return data


