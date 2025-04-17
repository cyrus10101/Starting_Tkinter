# Program to print in Tkinter

# import tkinter module as tk
import tkinter as tk

# Create instance of tk.Tk() class that will create applictaion window
root = tk.Tk()

# place a label on the root window and pack it.
message = tk.Label(root, text="Hello World!")
message.pack() 

# Method of the main window object. it's like running window infinitely.
root.mainloop()