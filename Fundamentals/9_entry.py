import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x500')
root.title('Entry')

# Taking user input
name_entry = ttk.Entry(root)
name_entry.pack()

# Setting the focus
# Focus will decide the default Entry box that user will enter data
second_name = ttk.Entry(root)
second_name.pack(pady = 50)
second_name.focus()

# Creating entry with label 
label_label = ttk.Label(root, text='Done')
label_label.pack(pady = 3)
label_entry = ttk.Entry(root)
label_entry.pack()
label_entry.focus()

# Creating entry for sensetive information
password_label = ttk.Label(root, text='Password: ')
password_label.pack(pady = 4)
password_entry = ttk.Entry(root, show='.')
password_entry.pack()

# Using entry with Strvar 

data = tk.StringVar()
data_entry = ttk.Entry(root, textvariable = data)
data_entry.pack()
data_entry.focus()

output_label = ttk.Label(root)
output_label.pack()

data.trace_add(
    "write",
    lambda *args: output_label.config(text = data.get())
)
root.mainloop()