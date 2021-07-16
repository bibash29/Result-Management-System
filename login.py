from tkinter import *
from PIL import ImageTk
from tkinter import messagebox, ttk
import os
import sqlite3
import email_pass
import smtplib
import random


class Login:
    def call_register(self):
        self.root.destroy()
        os.system('python register.py')

    def __init__(self, root1):
        self.root = root1
        self.root.title("Login")
        self.root.geometry("1510x760+5+15")
        self.root.attributes("-toolwindow", 1)

        self.bg = ImageTk.PhotoImage(file="images/class2.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        frame = Label(self.root, bg="black")
        frame.place(x=570, y=150, width=400, height=350)

        self.var_email = StringVar()
        self.var_password = StringVar()

        # ==== for changing password using security question ====
        self.var_question = StringVar()
        self.var_answer = StringVar()
        self.var_new_password = StringVar()

        # ==== for changing password using otp ====
        self.var_reset_option = IntVar()
        self.var_otp = StringVar()
        self.otp = ''

        login = Label(frame, text="Login", font=("times new roman", 20, "bold"), fg="green", bg="black")
        login.place(x=50, y=30)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="black")
        email.place(x=50, y=80)
        f_email = Entry(frame, textvariable=self.var_email, font=("times new roman", 13), bd=0, bg="light gray")
        f_email.place(x=50, y=120, width=250)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=50, y=160)
        f_pass = Entry(frame, textvariable=self.var_password, show="*", font=("times new roman", 13), bd=0,
                       bg="light gray")
        f_pass.place(x=50, y=200, width=250)

        # forget password
        forget = Button(frame, text="Forget password?", command=self.forget_password, font=("times new roman", 11),
                        bd=0, cursor="hand2", fg="white", bg="black", activebackground="black")
        forget.place(x=46, y=230)

        btn_login = Button(frame, text="Login", command=self.login_data, font=("dolphin", 13), bd=0, fg="white",
                           bg="green", activebackground="green", cursor="hand2")
        btn_login.place(x=50, y=260, width=100)

        btn_new_user = Button(frame, text="New user?", command=self.call_register, font=("dolphin", 13), bd=0,
                              cursor="hand2", fg="white", bg="blue", activebackground="blue")
        btn_new_user.place(x=200, y=260, width=100)

    # ==== when pressed forget password ====
    def forget_password(self):
        if self.var_email.get() == "":
            messagebox.showerror("Error", "Please enter your email address to proceed", parent=self.root)
        else:
            try:
                db = sqlite3.connect(database="srms.db")
                cur = db.cursor()
                cur.execute("select * from users where email=?", (self.var_email.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid email.Please try with valid email address",
                                         parent=self.root)
                else:
                    self.call_reset_window()
                db.commit()
                db.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

    # ==== reset window ====
    def call_reset_window(self):
        self.root2 = Toplevel()
        self.root2.title("Forget password options")
        self.root2.geometry("450x400+550+150")
        self.root2.configure(bg='white')
        self.root2.focus_force()  # this makes the new window focused
        self.root2.grab_set()  # when login window is clicked this window doesn't get lost
        # self.root2.resizable(False, False)  # this makes maximize button disabled
        self.root2.attributes("-toolwindow", 1)

        title = Label(self.root2, text='How do you want to reset your password?', font=('times new roman', 17, 'bold'),
                      bg="white", activebackground='white').place(x=15, y=30)
        Radiobutton(self.root2, text='by sending otp to my gmail', font=('times new roman', 13), bg='white',
                    value=1, variable=self.var_reset_option, cursor='hand2').place(x=15, y=110)
        Radiobutton(self.root2, text='by security question and answer', font=('times new roman', 13), bg='white',
                    value=2, variable=self.var_reset_option, cursor='hand2').place(x=15, y=150)
        Button(self.root2, text='Next', font=('times new roman', 13), fg='white', bg='blue', activebackground='blue',
               cursor='hand2', command=self.call_reset_password).place(x=150, y=260, width=150)

    # ==== function to either open otp or security question dialog box ====
    def call_reset_password(self):
        if self.var_reset_option.get() == 0:
            messagebox.showinfo('Info', 'Please select one of the above options.', parent=self.root2)
            return False
        self.root3 = Toplevel()
        self.root3.title("Forget password")
        self.root3.geometry("450x450+550+150")
        self.root3.focus_force()  # this makes the new window focused
        self.root3.grab_set()  # when login window is clicked this window doesn't get lost
        self.root3.attributes("-toolwindow", 1)
        if self.var_reset_option.get() == 1:
            try:
                db = sqlite3.connect(database='srms.db')
                cur = db.cursor()
                cur.execute("select email from users where email=?", (self.var_email.get(),))
                rec = cur.fetchone()
                check = self.send_email(rec[0])
                if check == 'f':
                    messagebox.showerror('Error', 'Connection error.Please tray again.', parent=self.root2)
                else:
                    title = Label(self.root3, text="Forget password?", font=("times new roman", 30, "bold"),
                                  fg="green").place(x=65, y=20)

                    self.b1 = Button(self.root3, text="Change password", command=self.change_password_otp,
                                     font=("dolphin", 13), bd=0, cursor="hand2", bg="yellow")
                    self.b1.place(x=150, y=380, width=150)
                    self.b1['state'] = DISABLED

                    Label(self.root3, text="Enter the otp that has been sent to your gmail:",
                          font=("times new roman", 15)).place(x=45, y=110)
                    self.f_otp = Entry(self.root3, textvariable=self.var_otp, font=("times new roman", 15, "bold"),
                                  bg='light gray')
                    self.f_otp.place(x=115, y=160)
                    self.b2 = Button(self.root3, text='submit', font=("times new roman", 13, "bold"), bg='sky blue',
                                     cursor='hand2', command=self.check_otp)
                    self.b2.place(x=170, y=210, width=100)
                    new_password = Label(self.root3, text="New Password", font=("times new roman", 15, "bold"),
                                         fg="gray").place(x=160, y=290)
                    self.f_password = Entry(self.root3, textvariable=self.var_new_password, font=("times new roman", 11),
                                            bd=0, bg="light gray")
                    self.f_password.place(x=95, y=330, width=250)
                    self.f_password['state'] = DISABLED

            except Exception as e:
                messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root3)

        if self.var_reset_option.get() == 2:
            title = Label(self.root3, text="Forget password?", font=("times new roman", 30, "bold"), fg="green")
            title.place(x=65, y=20)

            question = Label(self.root3, text="Security question", font=("times new roman", 15, "bold"),
                             fg="gray")
            question.place(x=145, y=110)
            c_question = ttk.Combobox(self.root3, textvariable=self.var_question, font=("times new roman", 11),
                                      state="readonly", justify=CENTER)
            c_question["values"] = ("Select", "Your birth place?", "Your favourite food?", "Your true love?")
            c_question.place(x=95, y=150, width=250)
            c_question.current(0)

            security_answer = Label(self.root3, text="Answer", font=("times new roman", 15, "bold"),
                                    fg="gray").place(x=185, y=200)
            f_answer = Entry(self.root3, textvariable=self.var_answer, font=("times new roman", 11), bd=0,
                             bg="light gray")
            f_answer.place(x=95, y=240, width=250)

            btn_reset = Button(self.root3, text="Change password", command=self.change_password_security,
                               font=("dolphin", 13),
                               bd=0, cursor="hand2", fg="white", bg="green").place(x=150, y=380, width=150)

            title = Label(self.root3, text="Forget password?", font=("times new roman", 30, "bold"), fg="green")
            title.place(x=65, y=20)
            new_password = Label(self.root3, text="New Password", font=("times new roman", 15, "bold"),
                                 fg="gray").place(x=160, y=290)
            f_password = Entry(self.root3, textvariable=self.var_new_password, font=("times new roman", 11),
                               bd=0, bg="light gray").place(x=95, y=330, width=250)

    # ==== function for submit button ====
    def check_otp(self):
        if self.var_otp.get() == "":
            messagebox.showerror('Error', 'Please enter the otp first!!!', parent=self.root3)
        elif int(self.var_otp.get()) == int(self.otp):
            messagebox.showinfo('Confirmation', 'OTP matched.Proceed now!!!', parent=self.root3)
            self.f_otp['state'] = DISABLED
            self.f_password['state'] = NORMAL
            self.b1['state'] = NORMAL
            self.b2['state'] = DISABLED
        else:
            messagebox.showinfo('Error', 'OTP incorrect.Please check your OTP and try again.', parent=self.root3)

    # change password function with security question
    def change_password_otp(self):
        try:
            db = sqlite3.connect(database='srms.db')
            cur = db.cursor()
            if self.var_new_password.get() == "":
                messagebox.showerror("Error", "New password field is required.", parent=self.root3)
            else:
                cur.execute("update users set password=? where email=?",
                            (self.var_new_password.get(), self.var_email.get(),))
                db.commit()
                db.close()
                messagebox.showinfo("Success", "Password changed successfully.Please login with new password.",
                                    parent=self.root3)
                self.var_new_password.set("")
                self.root3.destroy()
                self.root2.destroy()
                self.root.focus_force()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root3)

    # change password function with security question
    def change_password_security(self):
        if self.var_question.get() == "Select" or self.var_answer.get() == "" or self.var_new_password.get() == "":
            messagebox.showerror("Error", "All fields required.", parent=self.root3)
        else:
            try:
                db = sqlite3.connect(database="srms.db")
                cur = db.cursor()
                cur.execute("select password from users where email=? and question=? and answer=?",
                            (self.var_email.get(), self.var_question.get(), self.var_answer.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please enter valid question and answer", parent=self.root3)
                else:
                    cur.execute("update users set password=? where email=?",
                                (self.var_new_password.get(), self.var_email.get()))
                    db.commit()
                    db.close()
                    messagebox.showinfo("Success", "Password changed successfully.Please login with new password.",
                                        parent=self.root3)
                    self.var_new_password.set("")
                    self.var_answer.set("")
                    self.root3.destroy()
                    self.root2.destroy()
                    self.root.focus_force()

            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root3)

    # ==== login function ====
    def login_data(self):
        if self.var_email.get() == "" or self.var_password.get() == "":
            messagebox.showerror("Error", "Both fields required.", parent=self.root)
        elif self.var_email.get() == "admin" or self.var_password.get() == "admin":
            self.root.destroy()
            os.system('python admin.py')
        else:
            try:
                db = sqlite3.connect(database="srms.db")
                cur = db.cursor()
                cur.execute("select * from users where email=? and password=?",
                            (self.var_email.get(), self.var_password.get(),))
                result = cur.fetchone()
                if result is None:
                    messagebox.showerror("Error", "Invalid email or password.", parent=self.root)
                    return False
                else:
                    if result[11] == 1 or result[11] == 2:
                        if result[12] is None:
                            messagebox.showinfo("Pending", "Your registration request is still pending.Please wait for "
                                                           "admin to respond your request.", parent=self.root)
                        elif result[12] == 0:
                            messagebox.showerror("Failure", "Your registration request has been rejected.Please "
                                                            "register with valid information.", parent=self.root)
                        elif result[11] == 1 and result[12] == 1:
                            self.root.destroy()
                            os.system('python dashboard.py')
                        elif result[11] == 2 and result[12] == 1:
                            self.root.destroy()
                            os.system('python search_result.py')
                db.commit()
                db.close()

            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

    def send_email(self, to_):
        object = smtplib.SMTP('smtp.gmail.com', 587)
        object.starttls()
        email = email_pass.email
        password = email_pass.password

        object.login(email, password)
        self.otp = random.randint(100001, 999999)
        print(self.otp)

        sub = "SRMS-reset password!!"
        msg = f"Dear sir/madam,\n\nOTP to reset your password is {str(self.otp)}.\n\nWith regards,\nSRMS-team"
        msg = "Subject:{}\n\n{}".format(sub, msg)
        object.sendmail(email, to_, msg)
        check = object.ehlo()  # to check message sent or not if returned tuple 0 will store that
        if check[0] == 250:
            return 's'
        else:
            return 'f'


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()

