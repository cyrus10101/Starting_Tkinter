import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('400x500')
root.title('example')

def verify():
    names = name.get()
    ages = age.get()
    genders = gender.get()
    passwords = password.get()
    confirm_password = confirm_password_entry.get()
    if passwords != confirm_password:
        showinfo(
            title = 'Password Error!',
            message = 'Password did not match'
        )
        return
    
    if not names or not ages or not genders:
        showinfo(
            title = 'Error', 
            message = 'Fields cannot be submit empty'
        )
    else:
        showinfo(
            title = 'Succesfull',
            message = 'Submitted succesfully.'
        )
        return names, ages, genders

def display():
    names, ages, genders = verify()
    show_label.config(text=f'Name: {names}\nAges: {ages}\nGender: {genders}')

name_label = ttk.Label(root, text='Name: ')
name_label.pack(pady=4)
name = ttk.Entry(root)
name.pack()
name.focus()

age_label = ttk.Label(root, text='Age: ')
age_label.pack(pady = 4)
age = ttk.Entry(root)
age.pack()

gender_label = ttk.Label(root, text='Gender: ')
gender_label.pack(pady = 4)
gender = ttk.Entry(root)
gender.pack()

password_label = ttk.Label(root, text='Password: ')
password_label.pack(pady = 4)
password = ttk.Entry(root, show='*')
password.pack()

confirm_password_label = ttk.Label(root, text = 'Confirm Password: ')
confirm_password_label.pack(pady = 4)
confirm_password_entry = ttk.Entry(root, show = '*')
confirm_password_entry.pack()

submit = ttk.Button(root, text='Submit', command = lambda: verify())
submit.pack()

show = ttk.Button(root, text='Display', command = lambda: display())
show.pack()

show_label = ttk.Label(root, text='')
show_label.pack(pady = 10)

root.mainloop()