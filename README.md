# GestureMouse
## Mouse Tracker using OpenCV and Hand Detection

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.5-green)](https://opencv.org/)
[![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9.52-orange)](https://pyautogui.readthedocs.io/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21.2-yellow)](https://numpy.org/)

This project implements a mouse tracker using a webcam, OpenCV, and a custom hand detection module. The tracker allows you to control your mouse cursor with hand movements and perform clicks using finger gestures.

## Introduction
This project leverages computer vision and hand detection to control the mouse cursor on your computer. It uses OpenCV for image processing, PyAutoGUI for mouse control, and a custom hand tracking module.

## Features
- **Move Mouse Cursor**: Move your mouse cursor by moving your index finger.
- **Click**: Perform a left click by bringing your index finger and middle finger close together.

## Requirements
- Python 3.8+
- OpenCV 4.5.5
- PyAutoGUI 0.9.52
- NumPy 1.21.2

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/harshaparida/GestureMouse.git
   cd GestureMouse
   ```
2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```sh
   python handTracking.py
   ```
2. Ensure your webcam is connected and functional.
3. Use your hand to control the mouse cursor:
   - **Move Mouse Cursor**: Extend your index finger to move the cursor.
   - **Click**: Bring your index finger and middle finger close together to perform a click.

## Acknowledgments
- [OpenCV](https://opencv.org/) for image processing.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for mouse control.
- [NumPy](https://numpy.org/) for numerical operations.
