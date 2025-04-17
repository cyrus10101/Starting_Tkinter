import tkinter as tk

root = tk.Tk()
center = tk.Tk()
# Window name
root.title('Window name.')
center.title('Centered window')

# Changing window size and location 
root.geometry('600x400+10+10')

'''
To get window on center of secreen 
1) Get the screen dimension
2) Find the center point
3) Set the position of the window to the center of screen.
'''
window_width = 600
window_height = 400

# Center your window
# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Find the rcenter point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
# Set the position of the window to the center of the screen
center.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# Resizing
#To prevent the window from resiziing 
root.resizable(False, False)
# To specify minimum and maximun size we use minsize() and maxsize()
center.minsize(100, 200)
center.maxsize(1600, 1400)

# Transparency 
# How to control transparency
root.attributes('-alpha', 0.5)

# Window stacking order
# To keep window always on top
center.attributes('-topmost', 1)

# Changing icon
# Icon image should be in same folder 
# For .ico file
#root.iconbitmap('icon.ico')
# For .png and other 
try:
    photo = tk.PhotoImage(file='logo.png')
    center.iconphoto(False, photo)
except tk.TclError as e:
    print('\033[31mError Loading image:', e,'\033[0m')

root.mainloop()
center.mainloop()
'''
syntax for windows size:
.geometry(''width x height + x-axis + y-axis)
'''
'''
Modules:
1) title(): method to change the title of the window.
2) geometry(): method to change the size and location of the window.
3) resizable(): method to specify whether a window can be resizable horizontally or vertically.
4) window.attributes: ('-alpha',0.5) to set the transparency for the window.
5) window.attributes: ('-topmost', 1) to make the window always on top.
6) lift() and lower(): methods to move the window up and down of the window stacking order.
7) Use the iconbitmap():  method to change the default icon of the window.
'''