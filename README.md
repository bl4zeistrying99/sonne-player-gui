🎬 Sonne Player - Python GUI Video Launcher
A simple Python desktop application that plays a local .mp4 video using a button-based graphical user interface (GUI). Built with tkinter for the GUI and os module to launch the video using the system’s default player.

📂 Project Structure
bash
Copy code
sonne_player/
├── sonne.py              # Main Python script (GUI)
└── assets/
    └── sonnecat.mp4      # Video file to be played
▶️ Features
Simple and clean Tkinter-based GUI

One-click to launch video playback

Works on any Windows machine with Python installed

No external dependencies — uses standard library only

🧪 Requirements
Python 3.6+

Windows OS (uses os.startfile() which is Windows-specific)

🚀 How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/bl4zeistrying99/video-player-gui.git
cd video-player-gui  # Or sonne_player if that's your folder
Run the app:

bash
Copy code
python sonne.py
Click the "▶️ Play Video" button to launch the video from assets/sonnecat.mp4.

🧰 Customization
Want to play your own video?

Just replace assets/sonnecat.mp4 with any .mp4 file — but keep the same name or update the path in sonne.py.

📸 Preview
(Add a screenshot of the GUI window here if you'd like)

📄 License
This project is open-source and free to use.
