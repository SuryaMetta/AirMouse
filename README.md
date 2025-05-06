# AirMouse
Hand Gesture Mouse Control Using OpenCV, MediaPipe & PyAutoGUI

Control your computer's mouse using hand gestures captured through a webcam! This project uses MediaPipe for real-time hand tracking, OpenCV for image processing, and PyAutoGUI for controlling the mouse pointer and simulating clicks.

📌 Features

Move your mouse pointer using your index finger.
Perform a mouse click by bringing your index finger and thumb together.
Real-time performance with minimal latency.
Works with any standard webcam.
Compatible with Windows, macOS, and Linux (requires Python).
🛠️ Requirements

Install the following Python libraries:

pip install opencv-python mediapipe pyautogui numpy
📄 How It Works

Captures video frames using your webcam.
Uses MediaPipe to detect your hand and track landmarks.
Tracks the index finger tip to control mouse movement.
Measures distance between index finger tip and thumb tip to detect a click gesture.
Moves and clicks the mouse using PyAutoGUI.
▶️ Usage

Clone this repository:
git clone https://github.com/your_username/hand-gesture-mouse-control.git
cd hand-gesture-mouse-control
Run the script:
python gesture_mouse_control.py
Allow camera access if prompted.
Use your hand in front of the camera:
Move your index finger to move the cursor.
Bring index finger and thumb together to click.
