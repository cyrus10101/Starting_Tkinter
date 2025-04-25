import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x500')

# Creating label
label1 = ttk.Label(root, text='Start').pack()

# Label with font
label2 = ttk.Label(root, text='hello world', font=('Helvetica, 15')).pack()

# Creating image Label
photo = tk.PhotoImage(file='"C:/Users/cyrus/Starting_Tkinter/Fundamentals/logo.png"')
label3 = ttk.Label(
    root, 
    image=photo
    )
label3.pack()

root.mainloop()