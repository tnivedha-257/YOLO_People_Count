# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 08:44:59 2025

@author: THYAGHARAJAN
"""

import cv2
from ultralytics import YOLO
from tkinter import *
from PIL import Image, ImageTk
import threading

# Load the YOLO model
model = YOLO("yolo11n.pt")

# Initialize GUI window
root = Tk()
root.title("YOLO Person Tracker")
root.geometry("1200x600")
root.configure(bg="white")

# Global variables
captured_frame = None
video_running = True

# --------- Layout Setup --------- #
main_frame = Frame(root, bg="white")
main_frame.pack(pady=10)

# Video Feed Display
video_panel = Label(main_frame, bg="black")
video_panel.grid(row=0, column=0, padx=10)

# Captured Image Display
capture_panel = Label(main_frame, bg="grey")
capture_panel.grid(row=0, column=1, padx=10)

# Text for Person Count
count_text = Text(main_frame, height=1, width=20, font=("Arial", 14))
count_text.grid(row=1, column=1, pady=10)

# --------- Functions --------- #
def update_video():
    cap = cv2.VideoCapture(0)

    def loop():
        global captured_frame, video_running
        while video_running:
            ret, frame = cap.read()
            if not ret:
                continue
            results = model(frame)
            annotated = results[0].plot()
            captured_frame = annotated.copy()

            # Convert frame to ImageTk for display
            img = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = img.resize((500, 375))
            imgtk = ImageTk.PhotoImage(image=img)

            # Update video panel
            video_panel.imgtk = imgtk
            video_panel.configure(image=imgtk)
    
    threading.Thread(target=loop, daemon=True).start()

def capture_frame():
    global captured_frame
    if captured_frame is not None:
        img = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((500, 375))
        imgtk = ImageTk.PhotoImage(image=img)
        capture_panel.imgtk = imgtk
        capture_panel.configure(image=imgtk)

def count_persons():
    global captured_frame
    if captured_frame is not None:
        results = model(captured_frame)
        count = 0
        for r in results:
            for cls in r.boxes.cls:
                if model.names[int(cls)] == "person":
                    count += 1
        count_text.delete("1.0", END)
        count_text.insert(END, f"Persons: {count}")

def quit_app():
    global video_running
    video_running = False
    root.destroy()

# --------- Buttons --------- #
button_frame = Frame(root, bg="white")
button_frame.pack(pady=10)

Button(button_frame, text="Capture", font=("Arial", 14), command=capture_frame).grid(row=0, column=0, padx=10)
Button(button_frame, text="Count", font=("Arial", 14), command=count_persons).grid(row=0, column=1, padx=10)
Button(button_frame, text="Quit", font=("Arial", 14), bg="red", fg="white", command=quit_app).grid(row=0, column=2, padx=10)

# --------- Start Everything --------- #
update_video()
root.mainloop()
