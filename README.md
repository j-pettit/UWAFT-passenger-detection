# Sentry Mode
UWAFT Passenger Detection Project

For instructions related to the base Python wrapper or YOLOv3 code, see the associated repositories.
https://github.com/pjreddie/darknet
https://github.com/madhawav/YOLO3-4-Py

### Setup Instructions
##### New Host
1. Clone the repository
2. Install the weights file manually:
	`
wget https://pjreddie.com/media/files/yolov3.weights
`
or
`bash YOLO3-4-Py/download_models.sh`
3. Update system OpenCV:
	`bash YOLO3-4-Py/tools/install_opencv34.sh`
4. Run the wrapper file, selecting the appropriate plugin based on the connection order

##### Update Only
1.`cd Documents/CAV/sentrymode`
2. `sudo apt-get update && sudo apt-get upgrade`
3. `git pull`
4. `cd ..`
5. `bash run.sh <parameter>`
