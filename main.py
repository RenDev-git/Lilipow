import cv2
import numpy as np
from flask import Flask, Response, render_template
import time
import mss

app = Flask(__name__)

def gen_frames():
    """Capture screen frames and yield them as JPEG images."""
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
        while True:
            start_time = time.time()  # Start time of frame capture

            # Capture the screen
            img = np.array(sct.grab(monitor))
            img = cv2.resize(img, (1920, 1080))  # Resize to 1920x1080 you may have to adjust this to your needs

            # Encode frame as JPEG
            success, buffer = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 70]) # 70 is the image compression quality (100 being higher quality)
            frame = buffer.tobytes()

            # Yield frame with necessary headers
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            # Calculate and maintain the frame rate of 30 FPS
            time_elapsed = time.time() - start_time
            delay = max(0, 1/30 - time_elapsed)
            time.sleep(delay)

@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/timestamp')
def timestamp():
    """Return the current timestamp."""
    return str(time.time())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7360, debug=True)
