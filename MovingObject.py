import cv2
import imutils

# Use 0 for default webcam, 1 if you have multiple cameras
cam = cv2.VideoCapture(0)  
firstframe = None
area = 500

while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    text = "Normal"

    # Resize frame
    img = imutils.resize(img, width=500)

    # Convert to grayscale
    grayingimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    gaussianimg = cv2.GaussianBlur(grayingimg, (21, 21), 0)

    # Initialize first frame
    if firstframe is None:
        firstframe = gaussianimg
        continue

    # Compute difference
    imgdiff = cv2.absdiff(firstframe, gaussianimg)
    _, threshimg = cv2.threshold(imgdiff, 25, 255, cv2.THRESH_BINARY)
    threshimg = cv2.dilate(threshimg, None, iterations=2)

    # Find contours
    cnts = cv2.findContours(threshimg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving object detected"

    print(text)
    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Camera Feed", img)

    key = cv2.waitKey(10) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
