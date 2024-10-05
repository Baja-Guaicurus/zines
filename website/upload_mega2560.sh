#!/usr/bin/env bash

set -x

if (( $# != 2 )); then
	exit 1
fi


port="$1"
filename="$2"
fqbn="arduino:avr:mega"

dir="${filename//.ino/}"

test ! -d $dir && mkdir $dir
cp "$filename" "$dir"

arduino-cli compile --fqbn $fqbn $dir && \
	arduino-cli upload -p $port --fqbn $fqbn $dir 

rm -rf "$dir"
