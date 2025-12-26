🎥 Moving Object Detection using Python

A real-time moving object detection system built using Python and OpenCV.
The project uses frame differencing and contour detection to identify motion from a live camera feed.

🚀 Features

📷 Real-time webcam motion detection

🟩 Bounding box around moving objects

⚡ Lightweight and fast processing

🧠 Background frame comparison

⌨️ Press Q to quit the application

🛠️ Technologies Used

Python 3

OpenCV (cv2)

imutils

📂 Project Structure
MovingObject/
│
├── ai_camera.py
└── README.md

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/TamilarasiG3/MovingObject.git

2️⃣ Navigate to the project folder
cd MovingObject

3️⃣ Install dependencies
pip install opencv-python imutils

4️⃣ Run the application
python ai_camera.py

🧠 How It Works

Captures video frames from the webcam.

Converts frames to grayscale.

Applies Gaussian blur to reduce noise.

Stores the first frame as background.

Compares current frame with background.

Detects contours where movement occurs.

Draws bounding boxes around moving objects.

🎯 Controls
Key	Action
Q	Quit application
📸 Output Example (Optional)

Add a screenshot or GIF here for better visualization.

![Moving Object Detection](output.png)

🌱 Future Enhancements

Background updating for dynamic environments

Multiple object tracking

Object classification

Save motion clips automatically

⚠️ Limitations

Sensitive to lighting changes

Works best with a static camera

Not optimized for crowded scenes

👩‍💻 Author

Tamilarasi G
GitHub: @TamilarasiG3

📜 License

This project is open-source and free to use for educational purposes.
