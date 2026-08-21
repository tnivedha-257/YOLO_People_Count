# YOLO People Counter

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
   git clone https://github.com/your-username/4YOLOPeopleCount.git
   cd 4YOLOPeopleCount
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python ultralytics pillow
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