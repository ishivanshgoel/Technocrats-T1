# Technocrats Task 1
The webpage displays the camera feed from the webcam(or video/URL).

## After cloning
* open `http://127.0.0.1:5000/` in the browser.

## To use a video or URL 
* simply replace `self.video = cv2.VideoCapture(0)` by 
`self.video = cv2.VideoCapture('URL/filename/path')` in **camera.py**.

* _Note_- 0 represents the default camera.
## Libraries used
* numpy
* opencv

## Framework used
* flask

