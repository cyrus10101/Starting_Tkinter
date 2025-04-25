import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
import os

root = tk.Tk()

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "logo.png")

root.geometry('400x500')
def myfun():
    print('Hello, World!')

def myfun1(para):
    print(para)
# Button to call function
btn = ttk.Button(
    root, 
    text = 'Button 1',
    command=myfun
)
btn1 = ttk.Button(
    root, 
    text = 'Button 2', 
    command = lambda: myfun1('Parameter')
)
btn.pack(
    ipadx = 6,
    ipady = 6, 
)
btn1.pack()

# Creating exit button
exit_btn = ttk.Button(
    root, 
    text='Exit',
    command=lambda: root.quit()
)
exit_btn.pack(
    ipadx = 5, 
    ipady = 5, 
    expand = True
)

# Image button example
def handle_click():
    showinfo(
        title = 'information', 
        message = 'Instagram button clicked!'
    )

download_button = ttk.Button(
    root, 
    text='hell',
    command = handle_click
)
download_button.pack(
    ipadx = 5,
    ipady = 5,
    expand = True
)
root.mainloop()