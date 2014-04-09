#!/usr/bin/env python

import os
import os.path as path

inputPath = '/home/yipeiw/Documents/Research-2014spring/vo/prosody_word_feat'
trainfile = '/home/yipeiw/Documents/Research-2014spring/vo/prosody.train.txt'

fout = open(trainfile, 'w')
for filename in os.listdir(inputPath):
	filepath = path.join(inputPath, filename)
	tag = filename.split('_')[1]

	fin = open(filepath)
	line = fin.readline()
	fin.close()	

	fout.write("%s,%s" % (tag, line))	

fout.close()
