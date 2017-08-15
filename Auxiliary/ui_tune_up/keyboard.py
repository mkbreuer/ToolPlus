import bpy
from ui_tune_up.utils import dd, operator_exists, load_json

print(30*"-")

kc = bpy.context.window_manager.keyconfigs['Blender User']

def setkey(k, props, kprops={}):

	try:
		for prop in props:
			setattr(k, prop, props[prop])
	except Exception as e:
		print("ERROR", e)
	
	try:
		for kprop in kprops:
			setattr(k.properties, kprop, kprops[kprop])
	except Exception as e:
		print(e)

def findkey(kdata, by = "type"):
	cmd, map, idname, kprops, props = kdata
	
	map_type = "KEYBOARD"
	if not "map_type" in props.keys():
		if props['type'].find("MOUSE")>-1:
			map_type = "MOUSE"
	else:
		map_type = props['map_type']
	
	props['shift'] = "shift" in props.keys() and props['shift'] == True
	props['ctrl'] = "ctrl" in props.keys() and props['ctrl'] == True
	props['alt'] = "alt" in props.keys() and props['alt'] == True
	props['oskey'] = "oskey" in props.keys() and props['oskey'] == True
	
	try:
		map = kc.keymaps[map]
	except:
		dd(map, "doesnt exists")
		return False
	
	keys = []

	for k in map.keymap_items:
		if k.map_type == map_type:
			found = True
			if by == "type":
				for prop in props:
					if getattr(k, prop) != props[prop]:
						found = False
						break
			elif by == "idname" and k.idname == idname:
				dd("found", idname)
				for kprop in kprops:
					if getattr(k.properties, kprop) != kprops[kprop]:
						found = False
						break
			else:
				found = False
				
			if found:
				#print(k.idname, k.type, k.ctrl, k.shift, k.alt)
				keys.append(k)
				
	n = len(keys)   
	
	if n == 0:
		dd("not found by", by)
		if by == "type":
			return findkey(kdata, "idname")
	elif n == 1:
		k = keys[0]
		dd("found by", by)
		return k, props, kprops
		#setkey(k, props, kprops)
	else:
		dd("multiples found by", by)
		return False

def loadkeys(data):
	i = 0
	for kdata in data:
		
		dd(kdata)
		
		cmd, map, idname, kprops, props = kdata
		
		if operator_exists(idname):
			k = findkey(kdata)
			
			if k:
				k, props, kprops = k
				k.idname = idname
			else:
				map = kc.keymaps[map]
				if "type" in props.keys():
					k = map.keymap_items.new(idname, props['type'], "PRESS")
				else:
					print(kdata)
					print("Cannot create key, please specify a type.")
					return 0
				
			setkey(k, props, kprops)
			#print(k.idname, k.is_user_defined == True or k.is_user_modified == True)
			i+=1
		else:
			dd(idname, "doesnt exists")
	return i

#removes key shortcuts assigned to invalid operators
def clear_keyboard():
	print("cleaning keyboard")
	for map in kc.keymaps:
		for k in map.keymap_items:
			idname = k.idname
			if idname and not operator_exists(idname):
				print("removing", idname)
				map.keymap_items.remove(k)

def setup_keyboard(self):
	config = load_json("data.json")
	if isinstance(config, str):
		self.report({"ERROR"}, config)
		return
	data = config['keyboard']
	count = loadkeys(data)
	self.report({"INFO"}, "Keyboard loaded.")
	
if __name__ == "__main__":
	from ui_tune_up.utils import load_json
	data = load_json("data.json")
	kdata = data['keyboard']
#	dd(kdata)
#	k = findkey(kdata[0])


	