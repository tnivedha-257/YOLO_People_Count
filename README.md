# YOLO People Counter

<a href="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square" target="_blank">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=flat-square" alt="Python 3.8+"/>
</a>
<a href="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" target="_blank">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License: MIT"/>
</a>
<a href="https://img.shields.io/badge/ultralytics-%237733BB?style=flat-square&logo=python" target="_blank">
  <img src="https://img.shields.io/badge/ultralytics-%237733BB?style=flat-square&logo=python" alt="ultralytics"/>
</a>
<a href="https://img.shields.io/badge/YOLO-v11-%237733BB?style=flat-square" target="_blank">
  <img src="https://img.shields.io/badge/YOLO-v11-%237733BB?style=flat-square" alt="YOLOv11"/>
</a>
<a href="https://img.shields.io/badge/Tkinter-8.6-%23646464?style=flat-square" target="_blank">
  <img src="https://img.shields.io/badge/Tkinter-8.6-%23646464?style=flat-square" alt="Tkinter"/>
</a>
<a href="https://img.shields.io/badge/cv2-4.x-%23007ACC?style=flat-square&logo=opencv" target="_blank">
  <img src="https://img.shields.io/badge/cv2-4.x-%23007ACC?style=flat-square&logo=opencv" alt="OpenCV"/>
</a>

A GUI application for real-time people counting using YOLOv11.

## Features

- Real-time video feed display with person detection
- Capture and save frames
- Automatic person counting on captured frames
- Simple tkinter-based GUI

## Requirements

- Python 3.8+
- OpenCV (`opencv-python`)
- Ultralytics YOLO (`ultralytics`)
- Pillow (`PIL`)
- Tkinter (usually included with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tnivedha-257/YOLO_People_Count.git
   cd YOLO_People_Count
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure `yolo11n.pt` model file is present in the project directory.

## Usage

Run the application:
```bash
python Camera_PeopleCount.py
```

### Controls

- **Capture** - Capture the current frame from the video feed
- **Count** - Count persons in the captured frame and display the count
- **Quit** - Exit the application

## How It Works

1. The application opens your default camera (index 0)
2. YOLOv11 model performs real-time person detection on each frame
3. Detected persons are highlighted with bounding boxes
4. Click "Capture" to save a frame, then "Count" to detect and count persons in the captured image

## Model

The application uses the YOLOv11 nano model (`yolo11n.pt`) which is included in the project directory. You can download a different YOLO model and replace the file if needed.