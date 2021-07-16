from tkinter import *
from PIL import ImageTk
from tkinter import ttk, messagebox
import re
import os
# import mysql.connector as sql
import sqlite3


class Register:
    @staticmethod
    # callback function for validating contact no.
    def validate_contact(user_number):
        if user_number.isdigit():
            return True
        elif user_number == "":
            return True
        else:
            messagebox.showwarning("Validate", "Contact must contain only digits.")
            return False

    ''' For email id :
        first letter should be either number or alphabet and can include 1 dot or hyphen or underscore
        followed by at least 1 alphabet or digit before and after @ symbol.
        After some character after @ hyphen can be included in between alphabets before next dot followed by
        some alphabet up to 5 digits and next dot followed by at max 5 alphabets is optional'''
    @staticmethod
    def is_valid_email(user_email):
        if len(user_email) > 7:
            if re.match(r'^([a-z0-9]+)[\.-_]?([a-z0-9]+)@([a-z0-9]+)[-]?([a-z0-9]+)\.([a-z]{2,5})([\.][a-z]{2,5})?$', user_email) is not None:
                return True
            else:
                messagebox.showerror("Error", "Please enter valid email address.")
                return False
        else:
            messagebox.showerror("Error", "Email must contain at least 8 character.")

    def clear_all(self):
        self.var_name.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_roll.set("")
        self.var_password.set("")
        self.var_confirm.set("")
        self.var_answer.set("")
        self.var_question.set("Select")
        self.var_faculty.set("Select")
        self.var_semester.set("Select")
        self.var_year.set("Select")
        self.var_gender.set("0")
        self.var_profession.set("0")
        self.var_tu_id.set("")
        self.var_chk.set("0")

    def call_login(self):
        self.start.destroy()
        os.system('python login.py')   # if this file in different location then use os.system('python login.py')
        # or import login

    def disable_entry(self):
        self.f_roll.delete("0", END)
        self.f_roll.configure(state=DISABLED)
        self.f_roll.update()
        self.f_faculty.set("Select")
        self.f_faculty.configure(state=DISABLED)
        self.f_faculty.update()
        self.f_semester.set("Select")
        self.f_semester.configure(state=DISABLED)
        self.f_semester.update()
        self.f_year.set('Select')
        self.f_year.configure(state=DISABLED)
        self.f_year.update()
        self.f_tu_id.delete("0", END)
        self.f_tu_id.configure(state=DISABLED)
        self.f_tu_id.update()

    def enable_entry(self):
        self.f_roll.configure(state=NORMAL)
        self.f_roll.update()
        self.f_faculty.configure(state=NORMAL)
        self.f_faculty.update()
        self.f_semester.configure(state=NORMAL)
        self.f_semester.update()
        self.f_year.configure(state=NORMAL)
        self.f_year.update()
        self.f_tu_id.configure(state=NORMAL)
        self.f_tu_id.update()

    def dis_or_en_sem_or_year(self, *args):
        if self.var_faculty.get() == "Select":
            self.f_year.set('Select')
            self.f_year.configure(state=NORMAL)
            self.f_year.update()
            self.f_semester.set('Select')
            self.f_semester.configure(state=NORMAL)
            self.f_semester.update()
        elif self.var_faculty.get() == "BASW" or self.var_faculty.get() == "BBS":
            self.f_semester.set("Select")
            self.f_semester.configure(state=DISABLED)
            self.f_semester.update()
            self.f_year.configure(state=NORMAL)
            self.f_year.update()
        elif self.var_faculty.get() != "BASW" or self.var_faculty.get() != "BBS":
            self.f_year.set("Select")
            self.f_year.configure(state=DISABLED)
            self.f_year.update()
            self.f_semester.configure(state=NORMAL)
            self.f_semester.update()

    def __init__(self, start):
        self.start = start  # initializing my start
        self.start.title("Register")
        self.start.geometry("1510x760+5+15")
        # self.start.resizable(False, False)
        self.start.attributes("-toolwindow", 1)

        # === background image ===
        self.bg = ImageTk.PhotoImage(file="images/library.jpg")  # object of class
        bg = Label(self.start, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)  # object of main window

        # === Front Image ===
        self.front = ImageTk.PhotoImage(file="images/book2.jpg")
        front = Label(self.start, image=self.front).place(x=160, y=80, width=450, height=650)

        # === Register Frame ===
        register_frame = Frame(self.start, bg="white")
        register_frame.place(x=610, y=80, width=700, height=650)

        topic = Label(register_frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white",
                      fg="green").place(x=50, y=15)

        ''' To fetch data in python we have 2 methods:
            1) Create any variable and pass it to entry field and fetch the data with that variable
            2) Fetch the data with the help of object of entry field we created
        '''

        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_roll = StringVar()
        self.var_password = StringVar()
        self.var_confirm = StringVar()
        self.var_question = StringVar()
        self.var_answer = StringVar()
        self.var_faculty = StringVar()
        self.var_semester = StringVar()
        self.var_year = StringVar()
        self.var_tu_id = StringVar()

        self.var_profession = IntVar()
        prof = Label(register_frame, text="Profession", font=("times new roman", 15, "bold"), bg="white",
                     fg="gray").place(x=50, y=65)
        Radiobutton(register_frame, text="Teacher", font=("times new roman", 14), bg="white",
                    variable=self.var_profession, value=1, command=self.disable_entry).place(x=150, y=65)
        Radiobutton(register_frame, text="Student", font=("times new roman", 14), bg="white",
                    variable=self.var_profession, value=2, command=self.enable_entry).place(x=250, y=65)

        tu_id = Label(register_frame, text="TU Registered no:", font=("times new roman", 12, 'bold'), bg="white", fg="gray")
        tu_id.place(x=380, y=65)
        self.f_tu_id = Entry(register_frame, font=("times new roman", 15), textvariable=self.var_tu_id, bd=0, bg="light gray")
        self.f_tu_id.place(x=510, y=65, width=120)

        # === First row ===
        name = Label(register_frame, text="Full Name", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        name.place(x=50, y=105)
        f_name = Entry(register_frame, font=("times new roman", 15), textvariable=self.var_name, bd=0, bg="light gray")
        f_name.place(x=50, y=135, width=250)

        contact = Label(register_frame, text="Contact", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        contact.place(x=380, y=105)
        f_contact = Entry(register_frame, textvariable=self.var_contact, font=("times new roman", 15), bd=0, bg="light gray")
        f_contact.place(x=380, y=135, width=250)

        """ For field validation, follow below steps:
                        1) Create a call back function
                        2) Register callback function (in this case :validate_contact)
                        3) Give the option values
                            a) validate(when to validate)
                            b) validate command(what function to call)
                            c) invalid command(optional)
                """

        # Register callback function validate_contact created above
        valid_contact = self.start.register(self.validate_contact)
        # pass option values:
        # %P is a ?pecifier used to pass input to callback function(in this case when key is pressed)
        f_contact.config(validate="key", validatecommand=(valid_contact, '%P'))

        # === Second row ===
        email = Label(register_frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        email.place(x=50, y=175)
        f_email = Entry(register_frame, textvariable=self.var_email, font=("times new roman", 15),
                        bd=0, bg="light gray")
        f_email.place(x=50, y=205, width=250)

        roll = Label(register_frame, text="Roll no.", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        roll.place(x=380, y=175)
        self.f_roll = Entry(register_frame, textvariable=self.var_roll, font=("times new roman", 15), bd=0, bg='light gray')
        self.f_roll.place(x=380, y=205, width=250)

        # === Third row ===
        password = Label(register_frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray")
        password.place(x=50, y=245)
        f_password = Entry(register_frame, textvariable=self.var_password, show="*", font=("times new roman", 15),
                           bd=0, bg="light gray")
        f_password.place(x=50, y=275, width=250)

        confirm = Label(register_frame, text="Confirm password", font=("times new roman", 15, "bold"), bg="white",
                        fg="gray")
        confirm.place(x=380, y=245)
        f_confirm = Entry(register_frame, textvariable=self.var_confirm, show="*", font=("times new roman", 15),
                          bd=0, bg="light gray")
        f_confirm.place(x=380, y=275, width=250)

        # === Fourth row === next way to add drop down list
        security_question = Label(register_frame, text="Security question", font=("times new roman", 15, "bold"),
                                  bg="white", fg="gray").place(x=50, y=315)
        list_question = ["Your birth place?", "Your favourite food?", "Your true love?"]
        c_question = OptionMenu(register_frame, self.var_question, *list_question)
        self.var_question.set("Select")
        c_question.place(x=50, y=345, width=250)

        security_answer = Label(register_frame, text="Answer", font=("times new roman", 15, "bold"), bg="white",
                                fg="gray").place(x=380, y=315)
        f_answer = Entry(register_frame, textvariable=self.var_answer, font=("times new roman", 15,), bd=0, bg="light gray")
        f_answer.place(x=380, y=345, width=250)

        faculty = Label(register_frame, text="Faculty", font=('times', 15, 'bold'), bg='white', fg='gray').place(x=50, y=385)
        self.f_faculty = ttk.Combobox(register_frame, textvariable=self.var_faculty, font=('times', 13),
                                      state='readonly', justify=CENTER)
        self.f_faculty['values'] = ('Select', 'BSc.CSIT', 'BPSG', 'BA', 'BBM', 'BBS', 'BCA')
        self.f_faculty.place(x=50, y=415, width=250)
        self.f_faculty.current(0)
        self.f_faculty.bind('<<ComboboxSelected>>', self.dis_or_en_sem_or_year)

        semester = Label(register_frame, text="Semester", font=('times', 15, 'bold'), bg='white', fg='gray').place(x=380, y=385)
        self.f_semester = ttk.Combobox(register_frame, textvariable=self.var_semester, font=('times', 13), state='readonly',
                                       justify=CENTER)
        self.f_semester['values'] = ('Select', 'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth')
        self.f_semester.place(x=380, y=415, width=110)
        self.f_semester.current(0)

        year = Label(register_frame, text="Year", font=('times', 15, 'bold'), bg='white', fg='gray').place(
            x=520, y=385)
        self.f_year = ttk.Combobox(register_frame, textvariable=self.var_year, font=('times', 13),
                                   state='readonly', justify=CENTER)
        self.f_year['values'] = ('Select', 'First', 'Second', 'Third', 'Fourth')
        self.f_year.place(x=520, y=415, width=110)
        self.f_year.current(0)

        # radio button
        gender = Label(register_frame, text="Gender", font=("times new roman", 15, "bold"), bg="white",
                       fg="gray").place(x=50, y=460)
        self.var_gender = IntVar()
        Radiobutton(register_frame, text="Male", font=("times new roman", 14), bg="white", variable=self.var_gender,
                    value=1).place(x=140, y=460)
        Radiobutton(register_frame, text="Female", font=("times new roman", 14), bg="white", variable=self.var_gender,
                    value=2).place(x=240, y=460)

        # terms and conditions
        self.var_chk = IntVar()
        chk = Checkbutton(register_frame, text="I Agree all Terms and Conditions", variable=self.var_chk,
                          onvalue=1, offvalue=0, font=("times new roman", 11), bg="white").place(x=50, y=510)
        # register button
        btn_register = Button(register_frame, text="Register now", font=("dolphin", 12), fg="white", bd=0,
                              cursor="hand2", command=self.register_data, bg="green",
                              activebackground="green").place(x=50, y=550, width=120)

        # clear button
        btn_clear = Button(register_frame, text="Clear all", font=("dolphin", 12), fg="white", bd=0,
                           cursor="hand2", command=self.clear_all, bg="red",
                           activebackground="red").place(x=200, y=550, width=100)

        # sign in
        btn_sign_in = Button(register_frame, command=self.call_login, text="Go to sign in -->", font=("dolphin", 12),
                             bg="blue", fg="white", bd=0, cursor="hand2",
                             activebackground="blue").place(x=480, y=550, width=150)

    def register_data(self):
        a = {'Tu registered no.': self.var_tu_id.get(),
             'Fullname': self.var_name.get(),
             'Contact': self.var_contact.get(),
             'Email': self.var_email.get(),
             'Roll no.': self.var_roll.get(),
             'Password': self.var_password.get(),
             'Confirm Password': self.var_confirm.get(),
             'Security question': self.var_question.get(),
             'Answer': self.var_answer.get(),
             'faculty': self.var_faculty.get(),
             'Semester': self.var_semester.get(),
             'year': self.var_year.get()
             }
        exc = set(('Tu registered no.', 'Roll no.', 'faculty', 'Semester', 'year'))
        exc1, exc2 = 'Semester', 'year'
        if self.var_profession.get() != 1 and self.var_profession.get() != 2:
            messagebox.showerror("Error", "Please select your profession.", parent=self.start)
        elif self.var_profession.get() == 1:
            for x, y in a.items():
                if x not in exc:
                    if y == "" or y == "Select":
                        messagebox.showerror("Error", f"{x} field is required.", parent=self.start)
                        return False
        elif self.var_profession.get() == 2:
            if self.var_faculty.get() == 'BASW' or self.var_faculty.get() == 'BBS':
                for x, y in a.items():
                    if x not in exc1:
                        if y == "" or y == "Select":
                            messagebox.showerror("Error", f"{x} field is required.", parent=self.start)
                            return False
            elif self.var_faculty.get() != 'BASW' and self.var_faculty.get() != 'BBS':
                for x, y in a.items():
                    if x not in exc2:
                        if y == "" or y == "Select":
                            messagebox.showerror("Error", f"{x} field is required.", parent=self.start)
                            return False
        if len(self.var_contact.get()) != 10:
            messagebox.showwarning("Warning", "Contact must be of 10 digits", parent=self.start)
        elif len(self.var_password.get()) < 8:
            messagebox.showwarning("Warning", "Password must be at least 8 character.", parent=self.start)
        elif self.var_password.get() != self.var_confirm.get():
            messagebox.showerror("Error", "Password did not match.", parent=self.start)
        elif self.var_gender.get() != 1 and self.var_gender.get() != 2:
            messagebox.showerror("Error", "Please select your gender.", parent=self.start)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree terms and conditions.", parent=self.start)
        else:
            # if self.var_email.get() != "":
            status = self.is_valid_email(self.var_email.get())
            if status:
                try:  # database transactions and table users have been created in database
                    db = sqlite3.connect(database="srms.db")
                    cur = db.cursor()
                    cur.execute("select * from users where email=? or tu_registered_id=?",
                                (self.var_email.get(), self.var_tu_id.get()),)
                    row = cur.fetchone()
                    if row is not None:
                        messagebox.showerror("Error", "Email or TU id already exists.Please try your own valid email "
                                             "or TU registration id.")
                        return False
                    if self.var_year.get() == 'Select':
                        cur.execute("select * from users where roll=? and faculty=? and semester=? and profession=2",
                                    (self.var_roll.get(), self.var_faculty.get(), self.var_semester.get(),))
                        row1 = cur.fetchone()
                        if row1 is not None:
                            messagebox.showerror("Error","Roll number already assigned.Please try your own roll number.")
                            return False
                    elif self.var_semester.get() == 'Select':
                        cur.execute("select * from users where roll=? and faculty=? and year=? and profession=2",
                                    (self.var_roll.get(), self.var_faculty.get(), self.var_year.get(),))
                        row2 = cur.fetchone()
                        if row2 is not None:
                            messagebox.showerror("Error","Roll number already assigned.Please try your own roll number.")
                            return False
                    sql2 = "insert into users(name,contact,email,roll,password,question,answer,faculty," \
                           "semester,year,gender,profession,tu_registered_id) " \
                           "values(?,?,?,?,?,?,?,?,?,?,?,?,?)"
                    val = (self.var_name.get(),
                           self.var_contact.get(),
                           self.var_email.get(),
                           self.var_roll.get(),
                           self.var_password.get(),
                           self.var_question.get(),
                           self.var_answer.get(),
                           self.var_faculty.get(),
                           self.var_semester.get(),
                           self.var_year.get(),
                           self.var_gender.get(),
                           self.var_profession.get(),
                           self.var_tu_id.get(),)
                    cur.execute(sql2, val)
                    db.commit()
                    db.close()
                    messagebox.showinfo("Pending", "Registration pending.Wait for the response from admin.You will "
                                        "be shortly notified after admin accepts your request", parent=self.start)
                    self.clear_all()
                except Exception as e:
                    messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.start)


start = Tk()
obj = Register(start)
start.mainloop()
