import cv2

# Open a video capture object
video_path = "TS.mp4"
cap = cv2.VideoCapture(video_path)

# Check if the video capture object is successfully opened
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if the video has ended
    if not ret:
        break

    # Convert the frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the grayscale frame
    cv2.imshow("Video Frame", frame_gray)

    # Check for user key press; 27 is the ASCII code for the 'Esc' key
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
