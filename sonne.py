import tkinter as tk
import os

def play_video():
    video_path = os.path.join(os.path.dirname(__file__), 'assets', 'sonnecat.mp4')
    try:
        os.startfile(video_path)
    except Exception as e:
        print("Error:", e)

root = tk.Tk()
root.title("Sonne Player")
root.geometry("300x200")
root.configure(bg="#222")

btn = tk.Button(root, text="▶️ Play Video", font=("Helvetica", 14), bg="#ffaa00", command=play_video)
btn.pack(expand=True)

root.mainloop()
