import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Get screen resolution for mapping
screen_w, screen_h = pyautogui.size()

# Set up MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Set up webcam capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
frame_w, frame_h = 640, 480

click_delay = time.time()  # Click delay timer

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get the coordinates of the index finger tip (landmark 8) and thumb tip (landmark 4)
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            
            # Convert normalized coordinates to pixel coordinates
            x_index = int(index_tip.x * frame_w)
            y_index = int(index_tip.y * frame_h)
            x_thumb = int(thumb_tip.x * frame_w)
            y_thumb = int(thumb_tip.y * frame_h)
            
            # Map index finger position to screen coordinates
            screen_x = np.interp(x_index, (0, frame_w), (0, screen_w))
            screen_y = np.interp(y_index, (0, frame_h), (0, screen_h))

            # Move the mouse pointer to the mapped position (faster & direct)
            pyautogui.moveTo(screen_x, screen_y)

            # Calculate distance between thumb tip and index finger tip for click detection
            distance = np.hypot(x_index - x_thumb, y_index - y_thumb)

            # Faster click response with lower delay
            if distance < 35 and time.time() - click_delay > 0.2:  # Faster response
                pyautogui.click()
                click_delay = time.time()  # Reset click delay timer
                cv2.putText(frame, "Click", (x_index, y_index - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the video feed
    cv2.imshow("Hand Gesture Mouse Control (Fast)", frame)

    # Exit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
