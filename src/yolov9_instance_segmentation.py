import argparse
from ultralytics import YOLO
import cv2

# Construct the argument parser to parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, default="0",
                help="path to input video file or camera index (default is 0)")
ap.add_argument("-m", "--model", type=str, required=True,
                help="path to YOLOv9 segmentation model file (e.g., yolov9t-seg.pt, yolov9s-seg.pt, yolov9m-seg.pt, yolov9c-seg.pt, yolov9e-seg.pt)")
args = vars(ap.parse_args())

# Load YOLOv9 model
model = YOLO(args["model"])

# Open the video file or camera stream
video_path = args["video"]
# Convert video path to an integer if it is a camera index
if video_path.isdigit():
    video_path = int(video_path)
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv9 object detection on the frame
        results = model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("Object Detection", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()