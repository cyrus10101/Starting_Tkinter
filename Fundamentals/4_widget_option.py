import tkinter as tk
from tkinter import ttk

'''
There are 3 ways to set Options for a Tk Themed Widget:
1) Using the widget constructor when creating the widget
2) Set a property value using dictornary index after creating the widget.
3) Call the config() method with keyword argument.
'''
root = tk.Tk()
root1 = tk.Tk()
root2 = tk.Tk()

# Using the widget constructor when creating the widget
ttk.Label(root, text='Hi, There').pack()

# Using the dictionary index after widget creation
label = ttk.Label(root1)
label['text'] = 'Hi, there'
label.pack()

# Using the config() method with keyword arguments
label = ttk.Label(root2)
label.config(text='Hi, There')
label.pack()

root.mainloop()
root1.mainloop()
root2.mainloop()