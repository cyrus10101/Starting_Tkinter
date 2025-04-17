#ttk is themed widgets so it is good practice to used themed widgets

#importing ttk
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry('600x400')

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

root.mainloop()

