import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Joystick Player')

# Set window size
root.geometry('400x400')
root.resizable(False, False)
# Create a Label (player)
player = ttk.Label(root, text='@', font=('Arial', 24))
player.place(x=180, y=180)  # Start center

# Player position
pos_x = 180
pos_y = 180

goal = ttk.Label(root, text='*', font=('Arial', 24))
goal.place(x=100, y = 100)

# Movement function with boundaries
def move(event):
    goal_x = goal.winfo_x()
    goal_y = goal.winfo_y()
    global pos_x, pos_y

    step = 10  # movement speed
    player_size = 24  # size of the @ in pixels approx
    window_width = 400
    window_height = 400

    if event.keysym == 'Up':
        if pos_y - step >= 0:
            pos_y -= step
    elif event.keysym == 'Down':
        if pos_y + step + player_size <= window_height:
            pos_y += step
    elif event.keysym == 'Left':
        if pos_x - step >= 0:
            pos_x -= step
    elif event.keysym == 'Right':
        if pos_x + step + player_size <= window_width:
            pos_x += step
    if abs(pos_x - goal_x) < 10 and abs(pos_y - goal_y) < 10:
        print('You win.')
    player.place(x=pos_x, y=pos_y)

# Bind keys
root.bind('<Up>', move)
root.bind('<Down>', move)
root.bind('<Left>', move)
root.bind('<Right>', move)

root.mainloop()
