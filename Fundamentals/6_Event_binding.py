# Event Binding
# syntax:
# widget.bind(event, handler, add=None)
# when even occurs it Tkinter invoke the handler with event details. we can pass '+' to the add argument to have multiple event handlers respondint to the same event.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Game')

def click(event, para):
    print(para)

btn = ttk.Button(root, text='  ^ \n<   >\n  v', width=10)
btn.bind('<Up>',lambda event: click(event, 'Moved up'))
btn.bind('<Left>',lambda event: click(event, 'Moved left'), add='+')
btn.bind('<Right>',lambda event: click(event, 'Moved Right'), add='+')
btn.bind('<Down>',lambda event: click(event, 'Moved Down'), add='+')

btn.focus()
btn.pack(expand=True)

root.mainloop()
