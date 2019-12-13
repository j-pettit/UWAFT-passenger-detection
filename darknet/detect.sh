#!/bin/sh
# ./darknet detect cfg/yolov3.cfg yolov3.weights data/realsense1.png
./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights data/cam.mp4
