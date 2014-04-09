#!/bin/bash

root=/home/yipeiw/Documents

tool=$root/Research-2013fall/Tool/opensmile-1.0.1/bin/SMILExtract_standalone_32bit_generic
config=$root/Research-2013fall/Tool/opensmile-1.0.1/config/prosodyShs.conf

dataPath=$root/Research-2014spring/vo/wav

ftrPath=$root/Research-2014spring/vo/prosody_feat
mkdir -p $ftrPath

for wavfile in $dataPath/*.wav;
do
	filename=$(basename $wavfile)
	filename="${filename%.*}"
	output="$ftrPath/$filename.csv"
	
	echo "$tool -C $config -I $wavfile -O $output"
	$tool -C $config -I $wavfile -O $output
done
