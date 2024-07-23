# Lilipow Screen Sharing Across Web

This project captures the screen using `mss` and streams the frames over a Flask web server. The frames are encoded as JPEG images and served as a video feed.

## Read Before Using!

This project is **unreliable** and isn't meant to be a full-fledged program. It is an experimental program for learning about streaming a feed across networks. You may use this for simple tasks in a closed network as **this program provides no encryption; anything on the host computer screen will be shared across your local network.**

## Requirements

- Python 3.6+
- Flask
- OpenCV
- numpy
- mss

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/screen-capture-streaming.git
    cd screen-capture-streaming
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. To view on your host machine, open your web browser and navigate to `http://localhost:7360`.

3. To view on a second device, open your web browser and navigate to `http://192.168.xxx.xxx:7360`, where the `xxx.xxx` represents your host machine's IP address.

## Project Structure

- `app.py`: Main application file containing the Flask server and screen capture logic.
- `templates/index.html`: HTML template for the home page.
- `README.md`: Project documentation.

## Notes

- The screen capture resolution is set to 1920x1080. Modify the `monitor` dictionary in the `gen_frames` function if you need a different resolution.
- The frame rate is set to 30 FPS. Adjust the delay calculation if you need a different frame rate.

## License

This project is licensed under the MIT License.
