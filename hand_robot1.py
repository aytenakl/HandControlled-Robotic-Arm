import cv2
import mediapipe as mp
import serial
import time

# ==========================
# Arduino
# ==========================

arduino = serial.Serial("COM11", 9600, timeout=1)
time.sleep(2)

# ==========================
# MediaPipe
# ==========================

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = "hand_landmarker.task"

base_options = python.BaseOptions(
    model_asset_path=model_path
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

detector = vision.HandLandmarker.create_from_options(options)

# ==========================
# Camera
# ==========================

camera = cv2.VideoCapture(0)

last_command = ""

while True:

    ret, frame = camera.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    if result.hand_landmarks:

        landmarks = result.hand_landmarks[0]

        fingers = []

        # Thumb
        fingers.append(
            1 if landmarks[4].x < landmarks[3].x else 0
        )

        # Index
        fingers.append(
            1 if landmarks[8].y < landmarks[6].y else 0
        )

        # Middle
        fingers.append(
            1 if landmarks[12].y < landmarks[10].y else 0
        )

        # Ring
        fingers.append(
            1 if landmarks[16].y < landmarks[14].y else 0
        )

        # Pinky
        fingers.append(
            1 if landmarks[20].y < landmarks[18].y else 0
        )

        command = "".join(map(str, fingers))

        # إرسال الأمر للأردوينو
        if command != last_command:

            arduino.write(
                (command + "\n").encode()
            )

            print("Sent:", command)

            last_command = command

        # رسم النقاط
        h, w, _ = frame.shape

        for landmark in landmarks:

            x = int(landmark.x * w)
            y = int(landmark.y * h)

            cv2.circle(
                frame,
                (x, y),
                5,
                (0, 255, 0),
                -1
            )

        cv2.putText(
            frame,
            "Command: " + command,
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    else:

        cv2.putText(
            frame,
            "No hand detected",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    cv2.imshow(
        "Hand Controlled Robotic Arm",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
arduino.close()
cv2.destroyAllWindows()