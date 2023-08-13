import cv2

# Open a video capture object
video_path = "TS.mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video capture object is successfully opened
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the original video frame dimensions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the resized dimensions (50% smaller)
resized_width = int(frame_width * 0.5)
resized_height = int(frame_height * 0.5)

# Create a VideoWriter object to save the resized video
output_path = "resized_video.mp4"
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'XVID'), 30, (resized_width, resized_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    resized_frame = cv2.resize(frame, (resized_width, resized_height))
    out.write(resized_frame)
    cv2.imshow("Resized Video", resized_frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
