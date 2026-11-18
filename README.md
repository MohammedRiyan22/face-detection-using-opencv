# Real-Time Face Detection using OpenCV

A real-time face detection application developed using Python and OpenCV. The application uses the Haar Cascade Classifier to identify and locate human faces from live webcam video streams.

## Features

- **Real-Time Face Detection:** Detects faces continuously through a webcam.
- **Haar Cascade Classifier:** Uses a pre-trained frontal-face detection model.
- **Grayscale Image Processing:** Converts video frames into grayscale before detection.
- **Face Localization:** Draws rectangular bounding boxes around detected faces.
- **Live Video Processing:** Displays processed webcam frames in real time.
- **Keyboard Control:** Press Q to terminate the application.

## Technologies Used

- Python
- OpenCV
- Haar Cascade Classifier
- Computer Vision
- Image Processing

## Project Structure

```text
FaceDetection/
│
├── FaceDetect.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd face-detection-using-opencv
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python FaceDetect.py
```

## How It Works

1. Loads the pre-trained Haar Cascade frontal-face classifier.
2. Initializes the webcam using OpenCV.
3. Captures video frames continuously.
4. Converts each frame into grayscale.
5. Applies the `detectMultiScale()` method to identify faces.
6. Draws rectangular bounding boxes around detected faces.
7. Displays the processed video stream.
8. Releases the webcam when the user presses Q.

## Haar Cascade Configuration

The face detection algorithm uses the following parameters:

| Parameter | Value | Purpose |
|---|---:|---|
| scaleFactor | 1.1 | Controls image scaling between detection stages |
| minNeighbors | 7 | Controls detection strictness |
| minSize | (80, 80) | Minimum face detection size |
| maxSize | (300, 300) | Maximum face detection size |

## Learning Outcomes

- Understanding fundamental computer vision concepts.
- Working with OpenCV for real-time video processing.
- Implementing Haar Cascade-based face detection.
- Understanding grayscale image conversion.
- Capturing and processing webcam video streams.
- Working with image localization and bounding boxes.