#!/usr/bin/env python

import os.path as path
import os

alignPath = '/home/yipeiw/Documents/Research-2014spring/vo/align'
ftrPath = '/home/yipeiw/Documents/Research-2014spring/vo/prosody_feat'
outputPath = '/home/yipeiw/Documents/Research-2014spring/vo/prosody_word_feat'

scriptfile = '/home/yipeiw/Documents/Research-2014spring/vo/analysis/GetWordFeat.sh'

tool="./CalculateFtr.py"

def LoadData(filepath):
	utter_list = []
	timeinfo = {}
	for line in open(filepath):
		linelist = line.strip().split()
		word = linelist[3]
 		utter_list += [word]
		start = linelist[5]
		end = linelist[6]
		timeinfo[word] = (start, end)
	return timeinfo, " ".join(utter_list)

def ExtractWord(utter, timeinfo):
	global match_dict
	targets = match_dict[utter]
	start = timeinfo[targets[0]][0]
	end = timeinfo[targets[len(targets)-1]][1]
	return start, end


match_dict = {'I want this one':['this', 'one'],
'Uh I like the coffee there':['there'],
"It's here":['here'],
'Turn left here':['here']}

fout = open(scriptfile, 'w')
fout.write("#!/bin/bash\n")

for alignfile in os.listdir(alignPath):
	filepath = path.join(alignPath, alignfile)
	filename = path.splitext(alignfile)[0]

	timeinfo, utter = LoadData(filepath)
	start, end = ExtractWord(utter, timeinfo)

	ftrfile = path.join(ftrPath, filename + '.csv')
	outputfile = path.join(outputPath, filename+ '.txt')
	fout.write("%s %s %s %s %s\n" % (tool, ftrfile, outputfile, start, end))
	fout.write("echo \"%s %s %s %s %s\"\n" % (tool, ftrfile, outputfile, start, end))

fout.close()
