#!/usr/bin/env python

import sys

import numpy as np 
import scipy.stats


def CalculatePercent(feats):
	zero_num = 0.0
	for feat in feats:
		if abs(feat-0)<1e-10:
			zero_num += 1
	
	return 1-zero_num/float(len(feats)) 

def GetFeat(ftrdict, name, startIdx, endIdx):
	feats = [ftrdict[name][idx] for idx in range(startIdx, endIdx)]
	return feats

def LoadFtr(ftrfile):
	ftr_dict = {}

	fin = open(ftrfile)
	head = fin.readline().strip()
	headlist = head.split(';')
	for i in range(2, len(headlist)):
		ftr_dict[headlist[i]]={}

	while True:
		line = fin.readline()
		if not line:
			break
		linelist = line.strip().split(';')
		idx = int(linelist[0])

		for i in range(2, len(linelist)):
			name = headlist[i]
			ftr_dict[name][idx] = float(linelist[i])

	fin.close()

	return ftr_dict, headlist[2:len(headlist)]


ftrfile = sys.argv[1]
outputfile = sys.argv[2]
start = float(sys.argv[3])
end = float(sys.argv[4])

ftr_dict, namelist = LoadFtr(ftrfile)
total = len(ftr_dict[namelist[0]].keys())

startIdx = int(start/0.01)
endIdx = min(int(end/0.01), total)

if int(end/0.01) >= total:
	print "longer than file:", start, end, len(ftr_dict[namelist[0]].keys())

x_list = range(startIdx, endIdx)

#normalization

#f0 feature
f0_list = GetFeat(ftr_dict, namelist[0], startIdx, endIdx)
f0_mean = np.mean(f0_list)
f0_var = np.var(f0_list)
f0_percent = CalculatePercent(f0_list)
f0_slope, f0_intercept, f0_r_value, f0_p_value, f0_std_err = scipy.stats.linregress(x_list, f0_list)

f0_feat = [f0_mean, f0_var, f0_percent, f0_slope, f0_r_value]

#voice quality feature
voc_list = GetFeat(ftr_dict, namelist[1], startIdx, endIdx)
voc_mean = np.mean(voc_list)
voc_var = np.var(voc_list)
voc_percent = CalculatePercent(voc_list)

voc_feat = [voc_mean, voc_var, voc_percent]

#loudness feature
loud_list = GetFeat(ftr_dict, namelist[2], startIdx, endIdx)
loud_mean = np.mean(loud_list)
loud_var = np.var(loud_list)
l_slope, l_intercept, l_r_value, l_p_value, l_std_err = scipy.stats.linregress(x_list, loud_list)

loud_feat = [loud_mean, loud_var, l_slope, l_r_value]

all_feats = f0_feat + voc_feat + loud_feat

fout = open(outputfile, 'w')
outputline = ",".join(["%.6f" % ftr for ftr in all_feats])
fout.write(outputline + '\n')
fout.close()

