from tkinter import *
from tkinter import messagebox
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="login_gui"
)

cursor = connection.cursor()

def login():
    username = entry_one.get()
    password = entry_two.get()
    cursor.execute("SELECT * FROM USERS WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if (username == "" or password == ""):
        messagebox.showinfo("", "Invalid Input")
    elif (result):
        messagebox.showinfo("", "Login Success")
    else:
        messagebox.showinfo("", "Invalid Credentials")

root = Tk()
root.title("Login Application")
root.geometry("300x200")

global entry_one
global entry_two

Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

entry_one = Entry(root, bd=5)
entry_one.place(x=140, y=20)

entry_two = Entry(root, bd=5)
entry_two.place(x=140, y=70)

Button(root, text="Login", command=login, height=3, width=13, bd=6).place(x=100, y=120)

root.mainloop()

cursor.close()
connection.close()