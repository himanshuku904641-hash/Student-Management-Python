from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os
from student import Student


class Login:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x900")
        self.root.title("Login System")
        base=os.path.dirname(__file__)
        img=Image.open(os.path.join(base,"backtrasing","OIP.jpg")).resize((1400,900))
        self.bg_img=ImageTk.PhotoImage(img)
        Label(self.root,image=self.bg_img).place(x=0,y=0,relwidth=1,relheight=1)

        self.var_username = StringVar()
        self.var_password = StringVar()

        Label(root, text="Enter Username and Password",
              font=("times new roman", 25, "bold")).pack(pady=30)

        Label(root, text="Username",
            #   placeholder="Enter Username",
              font=("arial", 12, "bold")).pack()

        Entry(root, textvariable=self.var_username,
              show="*",font=("arial", 12)).pack(pady=5)

        Label(root, text="Password",
              font=("arial", 12, "bold")).pack()

        Entry(root, textvariable=self.var_password,
              show="*", font=("arial", 12)).pack(pady=5)

        Button(root, text="LOGIN",
               command=self.login,
               font=("arial", 12, "bold"),
               width=15).pack(pady=20)

    def login(self):
        username = self.var_username.get()
        password = self.var_password.get()

        if username == "admin" and password == "1234":

            self.root.destroy()

            new_root = tk.Tk()
            Student(new_root)
            new_root.mainloop()

        else:
            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )


if __name__ == "__main__":
    root = tk.Tk()
    Login(root)
    root.mainloop()