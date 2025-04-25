#Thinker command binding 
# It associates a callback with an event of a widget.
# It respond to the events such as 
# Mouse clicks and Keys presses

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x600')

#normal funtion
def hello(para):
    print(para)
    print('Hello, world!')

def select(para):
    print(para)

ttk.Button(root, text='click me', command=hello('hel')).pack()
# command binding using lambda.
ttk.Button(root, text='Lambda click', command=lambda: select('rock')).pack()
ttk.Button(root, text='paper', command=lambda: select('paper')).pack()
ttk.Button(root, text='scissor', command=lambda: select('scissor')).pack()

root.mainloop()