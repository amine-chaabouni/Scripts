#!/bin/sh

input_video=$1
output_video=$2
frame_rate=$3

ffmpeg -i $input_video -c:v libx264 -preset slow -crf $frame_rate -c:a copy $output_video
