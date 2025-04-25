import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
root = tk.Tk()
root.geometry('400x500')

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "logo.png")

image = tk.PhotoImage(file =image_path)
label = tk.Label(root, image = image).pack()

root.mainloop()