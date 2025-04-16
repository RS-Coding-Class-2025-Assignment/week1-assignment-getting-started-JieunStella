import tkinter as tk
from tkinter import ttk
import threading
import time

stop_thread=False

Root=tk.Tk()
Root.title("Part2")

label=tk.Label(Root, text="Ready")
label.pack(pady=20)

progress=ttk.Progressbar(Root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

def gui():
    for i in range(101):
        global start_thread
        label.config(text=f"percent:{i}%")
        progress["value"] = i

start_button=tk.Button(Root, text="START", command=gui)
start_button.pack(pady=20)

Root.mainloop()




