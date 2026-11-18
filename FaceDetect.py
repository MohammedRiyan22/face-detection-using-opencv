import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Open webcam
camera = cv2.VideoCapture(0)


while True:

    # Capture frame continuously
    ret, image = camera.read()

    # Check if frame was captured
    if not ret:
        print("Could not access the webcam.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(80, 80),
        maxSize=(300, 300)
    )

    # Draw rectangle around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            2
        )

    # Display webcam
    cv2.imshow("Face Detection", image)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
camera.release()
cv2.destroyAllWindows()