#2025 RofikKernel

import cv2
import os

# === CONFIGURATION ===
video_path = "video.mp4"
output_folder = "teka_teki_frames"

# List of timestamps in MM.SS format (minutes.seconds)
puzzle_timestamps_mmss = [
    00.04,   # Frame 1
    00.11,   # Frame 2
    00.17,   # Frame 3
    00.24,   # Frame 4
    00.40,   # Frame 5
    00.49,   # Frame 6
    00.57,   # Frame 7
    01.05,   # Frame 8  → 1 min 5 sec = 65 sec
    01.36,   # Frame 9  → 1 min 36 sec = 96 sec
    02.00,   # Frame 10 → 2 min 0 sec = 120 sec
    02.21,   # Frame 11 → 2 min 21 sec = 141 sec
    02.31,   # Frame 12 → 2 min 31 sec = 151 sec
]

# Convert MM.SS to total seconds
def mmss_to_seconds(mmss):
    mm, ss = divmod(int(mmss * 100), 100)  # extract minutes and seconds
    return mm * 60 + ss

# Convert all timestamps to seconds
puzzle_timestamps_seconds = [mmss_to_seconds(ts) for ts in puzzle_timestamps_mmss]

# === SCRIPT LOGIC ===
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Hardcode FPS since you confirmed it's 30.0
fps = 30.0
print(f"Using fixed FPS: {fps}")

for idx, timestamp in enumerate(puzzle_timestamps_seconds):
    frame_number = round(timestamp * fps)
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    
    ret, frame = cap.read()
    if not ret:
        print(f"Failed to read frame at {timestamp} seconds")
        continue
    
    output_path = os.path.join(output_folder, f"frame_{idx+1:02d}.png")
    cv2.imwrite(output_path, frame)
    print(f"Saved: {output_path}")

cap.release()
print("✅ Done capturing frames!")
