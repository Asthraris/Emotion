# Real-Time Emotion Detection using OpenCV & DeepFace

## 📌 Project Overview

This project is a real-time emotion detection system that uses your webcam feed to detect human faces and analyze their emotions. It leverages **OpenCV** for face detection and **DeepFace** for emotion recognition powered by deep learning.

This is a lightweight prototype of how computer vision and deep learning can be integrated to build emotion-aware systems such as smart surveillance, human-computer interaction tools, or sentiment-aware applications.

---

## 🚀 How It Works

1. **Video Feed Capture**: The webcam is accessed using OpenCV's `VideoCapture`.
2. **Face Detection**: Faces are identified using Haar Cascade classifiers.
3. **Emotion Analysis**: Detected faces are passed to the DeepFace library which uses a pre-trained deep neural network to classify emotions (e.g., happy, sad, angry, etc.).
4. **Display Output**: Bounding boxes and the predicted dominant emotion are overlaid on the video stream in real time.

---

## 🛠️ Installation Guide

> ⚠️ Python 3.7 – 3.10 is recommended due to DeepFace's dependencies.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/emotion-detector
cd emotion-detector
````

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

* The webcam window will pop up.
* Real-time bounding boxes and emotions will be displayed on detected faces.
* Press `q` to exit the program.

---

## 📚 What I Learned

This project taught me the following:

* ✅ How to use OpenCV for real-time video capture and face detection.
* ✅ How to integrate DeepFace for high-level emotion recognition using deep learning models.
* ✅ How to handle frame-by-frame analysis efficiently and deal with practical runtime issues like:

  * Missing Haar cascade files
  * TensorFlow GPU warnings (I will recomend u install tensorFlow -CPU version for not getting Cuda errors)
  * Frame synchronization
* ✅ Debugging common computer vision issues (e.g., wrong image formats, empty classifier errors).
* ✅ Importance of modularizing code for readability and robustness.

---

## 🧠 Future Improvements

* Use a more efficient face detector like MTCNN or RetinaFace
* Store emotion logs for analysis over time

---

## 📸 Demo



---

