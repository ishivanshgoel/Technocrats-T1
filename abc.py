from flask import Flask, render_template, Response,jsonify
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame,a = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def live(camera):
    while True:
        frame,a=camera.get_frame()
        yield(a)

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/params')
def params():
    return Response(live(VideoCamera()),mimetype='text/event-stream')

app.run(debug=True)
