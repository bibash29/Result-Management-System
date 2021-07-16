from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os


class Admin:
    # ==== Pending Button ====
    def pending(self):
        self.var_mail = []
        self.btn3.place(x=600, y=600)
        self.btn4.place(x=700, y=600)
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        try:
            cur.execute("select name,contact,email,faculty,semester,year,profession from users where permission is Null")
            rows = cur.fetchall()
            self.lists.delete(*self.lists.get_children())
            if not rows:
                self.lists.insert('', END, values='No\ data')
            else:
                for row in rows:
                    self.lists.insert('', END, values=row)
            db.commit()
            db.close()
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    # ==== Registered Teachers Button Function ====
    def reg_teachers(self):
        self.var_mail = []
        self.btn3.place_forget()
        self.btn4.place(x=700, y=600)
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        try:
            cur.execute("select name,contact,email,faculty,semester,year,profession from users where profession=1 "
                        "and permission=1")
            rows = cur.fetchall()
            self.lists.delete(*self.lists.get_children())
            if not rows:
                self.lists.insert('', END, values='No\ data')
            else:
                for row in rows:
                    self.lists.insert('', END, values=row)
            db.commit()
            db.close()
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    # ==== Registered students button function ====
    def reg_students(self):
        self.var_mail = []
        self.btn3.place_forget()
        self.btn4.place(x=700, y=600)
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        try:
            cur.execute("select name,contact,email,faculty,semester,year,profession from users where profession=2 "
                        "and permission=1")
            rows = cur.fetchall()
            self.lists.delete(*self.lists.get_children())
            if not rows:
                self.lists.insert('', END, values='No\ data')
            else:
                for row in rows:
                    self.lists.insert('', END, values=row)
            db.commit()
            db.close()
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    # # ==== Rejected users button function ====
    # def rejected_users(self):
    #     self.var_mail = []
    #     self.btn3.place(x=600, y=600)
    #     self.btn4.place_forget()
    #     db = sql.connect(host='localhost', user='root', passwd='', database='srms')
    #     cur = db.cursor()
    #     try:
    #         cur.execute("select id,name,contact,email,faculty,semester,year,profession from users where permission=0")
    #         rows = cur.fetchall()
    #         self.lists.delete(*self.lists.get_children())
    #         if not rows:
    #             self.lists.insert('', END, values='No\ data')
    #         else:
    #             for row in rows:
    #                 self.lists.insert('', END, values=row)
    #         db.commit()
    #         db.close()
    #     except Exception as e:
    #         messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    def search(self):
        self.var_mail = []
        self.btn3.place(x=600, y=600)
        self.btn4.place(x=700, y=600)
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        if self.var_name.get() == "":
            messagebox.showinfo('Info', 'Please enter some search keywords', parent=self.root)
        else:
            try:
                cur.execute(f"select name,contact,email,faculty,semester,year,profession from users where name "
                            f"like '{self.var_name.get()}%'")
                rows = cur.fetchall()
                self.lists.delete(*self.lists.get_children())
                if not rows:
                    self.lists.insert('', END, values='No\ data')
                else:
                    for row in rows:
                        self.lists.insert('', END, values=row)
                db.commit()
                db.close()
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    # ===== Selected rows of treeview event ====
    def to_accept(self, event):
        # r = self.lists.focus()
        # content = self.lists.item(r, 'values')
        # row = content["values"]
        content_list = []
        for row in self.lists.selection():
            content = self.lists.item(row, "values")
            if row:
                content_list.append(content[2])
            else:
                content_list.pop(content[2])
        self.var_mail = content_list
        # print(self.var_mail)
        # row = self.lists.identify('row', event.x, event.y)
        # content = self.lists.item(row, 'values')
        # if content[3] not in self.var_mail:
        #     self.var_mail.append(content[3])
        # print(self.var_mail)

    def call_dashboard(self):
        self.root.destroy()
        os.system('python dashboard.py')
    # ==== Accept Button ====
    def accept(self):
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        try:
            if len(self.var_mail) == 0:
                messagebox.showerror('Error', 'Please select some rows first', parent=self.root)
            else:
                cur.execute("select * from users where permission=1 and email in({})".format(str(self.var_mail)[1:-1]))
                z = cur.fetchall()
                if not z:
                    option = messagebox.askokcancel('Confirm', 'Are you sure you want to register selected users?')
                    if option:
                        cur.execute(
                            "update users set permission=1 where email in ({})".format(str(self.var_mail)[1:-1]))
                        db.commit()
                        messagebox.showinfo("Confirmation message", "Selected users have been registered successfully")
                        self.pending()
                        db.close()
                else:
                    messagebox.showinfo('Info', 'Some users selected above have already been registered. Please '
                                                'check the list and try again.', parent=self.root)
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    # ==== Reject Button ====
    def reject(self):
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        try:
            if len(self.var_mail) == 0:
                messagebox.showerror('Error', 'Please select some rows first', parent=self.root)
            else:
                cur.execute("select * from users where email in({})".format(str(self.var_mail)[1:-1]))
                z = cur.fetchall()
                if z is not None:
                    op = messagebox.askokcancel('Confirm', 'Rejecting will delete all its corresponding information.'
                                                'Are you sure you want to delete selected users? ', parent=self.root)
                    if op:
                        cur.execute("delete from users where email in ({})".format(str(self.var_mail)[1:-1]))
                        db.commit()
                        messagebox.showinfo('Confirmation message', 'Selected users have been deleted successfully.')
                        self.pending()
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    def __init__(self, root2):
        self.root = root2
        self.root.title("Admin page")
        self.root.geometry("1300x700+100+30")
        self.root.configure(bg='purple')
        self.root.attributes("-toolwindow", 1)

        # canvas = Canvas(self.root, bg='purple')
        # canvas.pack(fill=BOTH, expand=True)

        lbl1 = Label(self.root, text="Users Management Section", font=("times", 20, "bold"), fg='white', bg="purple", )
        lbl1.place(x=500, y=5)

        self.var_name = StringVar()
        name = Label(self.root, text='Name:', font=('times', 15, 'bold'), fg='white', bg='purple')
        name.place(x=800, y=90)
        f_name = Entry(self.root, textvariable=self.var_name, font=('times', 15))
        f_name.place(x=870, y=90)
        btn = Button(self.root, text="search", command=self.search, font=('times', 13, 'bold'), bg='white',
                     relief=RIDGE, bd=3, cursor='hand2',)
        btn.place(x=1100, y=85)

        frame = Frame(self.root, bd=4, relief=SUNKEN)
        frame.place(x=300, y=140, width=950, height=400)

        self.var_mail = []

        btn1 = Button(self.root, text="Pending", command=self.pending, font=('times', 13, 'bold'), bg='yellow',
                      relief=RIDGE, bd=3, cursor='hand2', activebackground='yellow')
        btn1.place(x=135, y=200, width=100)
        btn2 = Button(self.root, text="Registered Teachers", command=self.reg_teachers, font=('times', 13, 'bold'),
                      bg='green', relief=RIDGE, bd=3, cursor='hand2', activebackground='green')
        btn2.place(x=100, y=270)
        btn5 = Button(self.root, text="Registered Students", command=self.reg_students, font=('times', 13, 'bold'),
                      bg='green', relief=RIDGE, bd=3, cursor='hand2', activebackground='green')
        btn5.place(x=100, y=340)
        # btn6 = Button(self.root, text="Rejected Users", command=self.rejected_users, font=('times', 13, 'bold'),
        #               bg='red', relief=RIDGE, bd=3, cursor='hand2', activebackground='red')
        # btn6.place(x=120, y=410)
        self.btn3 = Button(self.root, text="Accept", command=self.accept, font=('times', 13, 'bold'), bg='green',
                           fg='white', relief=RIDGE, bd=3, cursor='hand2', activebackground='green')
        self.btn3.place(x=600, y=600)
        self.btn4 = Button(self.root, text="Reject", command=self.reject, font=('times', 13, 'bold'), bg='red',
                           fg='white', relief=RIDGE, bd=3, cursor='hand2', activebackground='red')
        self.btn4.place(x=700, y=600)

        self.btn5 = Button(self.root, text="Go to dashboard page >>>", command=self.call_dashboard, font=('times', 13, 'bold'),
                           bg='blue', fg='white', relief=RIDGE, bd=3, cursor='hand2', activebackground='blue')
        self.btn5.place(x=1050, y=600)

        scroll_vertical = Scrollbar(frame, orient=VERTICAL)
        scroll_horizontal = Scrollbar(frame, orient=HORIZONTAL)

        style = ttk.Style()
        style.configure("style1.Treeview.Heading", font=('times', 15, 'bold'))
        style.configure("style1.Treeview", font=('times', 15, 'italic'))

        self.lists = ttk.Treeview(frame, columns=("name", "contact", "email", "faculty", "semester", "year",
                                  "profession"), selectmode="extended", xscrollcommand=scroll_horizontal.set,
                                  yscrollcommand=scroll_vertical.set, style="style1.Treeview")

        scroll_vertical.pack(side=RIGHT, fill=Y)
        scroll_vertical.config(command=self.lists.yview)
        scroll_horizontal.pack(side=BOTTOM, fill=X)
        scroll_horizontal.config(command=self.lists.xview)

        self.lists.heading("name", anchor="nw", text="Name")
        self.lists.heading("contact", anchor="nw", text="Contact")
        self.lists.heading("email", anchor="nw", text="Email")
        self.lists.heading("faculty", anchor="nw", text="Faculty")
        self.lists.heading("semester", anchor="nw", text="Semester")
        self.lists.heading("year", anchor="nw", text="Year")
        self.lists.heading("profession", anchor="nw", text="Profession")
        self.lists["show"] = 'headings'
        self.lists.column("name", width=200)
        self.lists.column("contact", width=150)
        self.lists.column("email", width=350)
        self.lists.column("faculty", width=100)
        self.lists.column("semester", width=100)
        self.lists.column("year", width=100)
        self.lists.column("profession", width=100)

        self.lists.pack(fill=BOTH, expand=1)
        # self.lists.bind("<Button-1>", self.to_accept)
        self.lists.bind("<<TreeviewSelect>>", self.to_accept)


if __name__ == "__main__":
    root = Tk()
    obj = Admin(root)
    root.mainloop()
