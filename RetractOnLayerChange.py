#Name: Retract on Layer Change
#Info: Enable this plugin to automatically create a retract on each layer change, wrapping the z height change/first travel layer in a retract and recover sandwich
#Help: RetractOnLayerChange
#Depend: GCode
#Type: postprocess

## Written by Suz Hinton, suz@noopkat.com
## The bulk of this is borrowed from Steven Morloc https://github.com/smorloc/CuraPlugins
## This script is licensed under the Creative Commons - Attribution - Share Alike (CC BY-SA) terms

import re

def getValue(line, key, default = None):
	if not key in line or (';' in line and line.find(key) > line.find(';')):
		return default
	subPart = line[line.find(key) + 1:]
	m = re.search('^[0-9]+\.?[0-9]*', subPart)
	if m == None:
		return default
	try:
		return float(m.group(0))
	except:
		return default

with open(filename, "r") as f:
	lines = f.readlines()

z = 0
pauseState = 0
with open(filename, "w") as f:
	for line in lines:
		if getValue(line, 'G', None) in (0, 1):
			newZ = getValue(line, 'Z', z)
			if newZ != z:			
				line = "G10\n" + line + "G11\n"		# wrap z change line in a retract/recover sandwich
		f.write(line)