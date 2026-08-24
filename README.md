# 🤖 HandControlled Robotic Arm

A **computer vision-based robotic arm** controlled in real time using **hand gestures**.

The system uses a camera to detect hand landmarks with **MediaPipe**, analyzes the position of the fingers using **Python**, and sends the detected gesture to an **Arduino** through serial communication to control a robotic arm with **5 servo motors**.

## ✨ Features

* 🖐️ Real-time hand gesture detection
* 📷 Camera-based computer vision
* 🤖 Control of a 5-servo robotic arm
* 🧠 Hand landmark detection using MediaPipe
* 🐍 Python-based gesture processing
* 🔌 Serial communication between Python and Arduino
* ⚡ Real-time response to hand movements
* 👁️ Visual display of detected hand landmarks and commands

## 🛠️ Technologies

* **Python**
* **OpenCV**
* **MediaPipe**
* **Arduino**
* **C++**
* **Servo Motors**
* **Serial Communication**

## 🔄 How It Works

```text
        ✋ Hand Gesture
              ↓
          📷 Camera
              ↓
       OpenCV + MediaPipe
              ↓
      Finger Detection
              ↓
      Gesture → Binary Code
              ↓
       Serial Communication
              ↓
           Arduino
              ↓
       ⚙️ Servo Motors
              ↓
       🤖 Robotic Arm
```

## 🖐️ Gesture Detection

The system detects the state of the five fingers:

```text
Thumb   → 0 / 1
Index   → 0 / 1
Middle  → 0 / 1
Ring    → 0 / 1
Pinky   → 0 / 1
```

The detected fingers are converted into a binary command.

For example:

```text
00000
```

means all fingers are closed.

While:

```text
11111
```

means all fingers are open.

The command is then sent from Python to the Arduino.

## ⚙️ Hardware

* Arduino board
* 5 × Servo Motors
* Robotic Arm structure
* USB cable
* Computer/Laptop
* Webcam

### Servo Pins

| Servo   | Arduino Pin |
| ------- | ----------- |
| Servo 1 | 10          |
| Servo 2 | 9           |
| Servo 3 | 3           |
| Servo 4 | 5           |
| Servo 5 | 6           |

## 💻 Software Requirements

Install Python and the required libraries:

```bash
pip install opencv-python mediapipe pyserial
```

## 📁 Project Structure

```text
HandControlled-Robotic-Arm/
│
├── hand_control.py
├── arduino.ino
├── hand_landmarker.task
├── README.md
└── demo/
```

> Make sure `hand_landmarker.task` is located in the same directory as the Python script.

## 🚀 How to Run

### 1. Connect the Arduino

Connect the Arduino to your computer and check the assigned COM port.

For example:

```python
arduino = serial.Serial("COM10", 9600, timeout=1)
```

Change `COM10` if your Arduino uses another port.

### 2. Upload the Arduino Code

Open the Arduino sketch in the **Arduino IDE**, select your board and COM port, then upload the code.

### 3. Start the Python Program

Run:

```bash
python hand_control.py
```

The camera window will open and start detecting your hand.

### 4. Control the Arm

Move your fingers in front of the camera.

The detected gesture will be converted into a binary command and sent to the Arduino.

## 📊 Real-Time Output

The program displays:

```text
Command: 10110
```

on the camera window while simultaneously sending the command to the Arduino.

## 🎯 Project Goal

The goal of this project is to create a **natural and intuitive human-robot interaction system**, allowing users to control a robotic arm using their own hand movements instead of traditional controllers.

## 🔮 Future Improvements

* Add more complex hand gestures
* Improve finger detection accuracy
* Add wireless communication using Bluetooth
* Add more robotic arm movements
* Create a graphical user interface
* Add gesture customization
* Improve servo movement synchronization
