from tkinter import *
from modu import top_canvas, left_semester, result_format
import sqlite3
from tkinter import messagebox
import json


class Semester:
    def clear(self):
        self.var_sub1.set("")
        self.var_sub2.set("")
        self.var_sub3.set("")
        self.var_sub4.set("")
        self.var_sub5.set("")
        self.var_sub6.set("")

    def submit_marks(self, args):
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        try:
            cur.execute("select marks from result where email = (select email from users where tu_registered_id=?)",
                        (self.var_tu_id.get(),))
            record = cur.fetchone()
            if record is None:
                if args == 1:
                    json_dict = {'Computer Fundamentals and Applications': self.var_sub1.get(),
                                 'Society and Technology': self.var_sub2.get(),
                                 'English I': self.var_sub3.get(),
                                 'Mathematics I': self.var_sub4.get(),
                                 'Digital Logic': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 2:
                    json_dict = {'C programming': self.var_sub1.get(),
                                 'Financial Accounting': self.var_sub2.get(),
                                 'English II': self.var_sub3.get(),
                                 'Mathematics II': self.var_sub4.get(),
                                 'Microprocessor and Comp. Architecture': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 3:
                    json_dict = {'Data Structure and Algorithms': self.var_sub1.get(),
                                 'Probability and Statistics': self.var_sub2.get(),
                                 'System Analysis and Design': self.var_sub3.get(),
                                 'OOP in Java': self.var_sub4.get(),
                                 'Web Technology': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 4:
                    json_dict = {'Operating System': self.var_sub1.get(),
                                 'Numerical Methods': self.var_sub2.get(),
                                 'Software Engineering': self.var_sub3.get(),
                                 'Scripting Language': self.var_sub4.get(),
                                 'Database Management System': self.var_sub5.get(),
                                 'Project I': self.var_sub6.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 5:
                    json_dict = {'MIS and e-Business': self.var_sub1.get(),
                                 'DotNet Technology': self.var_sub2.get(),
                                 'Computer Networking': self.var_sub3.get(),
                                 'Introduction to Management': self.var_sub4.get(),
                                 'Computer Graphics and Animation': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 6:
                    json_dict = {'Mobile Programming': self.var_sub1.get(),
                                 'Distributed System': self.var_sub2.get(),
                                 'Applied Economics': self.var_sub3.get(),
                                 'Advanced Java Programming': self.var_sub4.get(),
                                 'Network Programming': self.var_sub5.get(),
                                 'Project II': self.var_sub6.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 7:
                    json_dict = {'Cyber Law and Professional Ethics': self.var_sub1.get(),
                                 'Cloud Computing': self.var_sub2.get(),
                                 'Internship': self.var_sub3.get(),
                                 'Elective Course I': self.var_sub4.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 8:
                    json_dict = {'Operations Research': self.var_sub1.get(),
                                 'Project III': self.var_sub2.get(),
                                 'Elective Course II': self.var_sub3.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                cur.execute("insert into result (email,marks) values((select email from users where tu_registered_id=?),"
                            "'" + self.json_marks + "')", (self.var_tu_id.get(),))
                db.commit()
                db.close()
                messagebox.showinfo('Info', 'Marks entered successfully', parent=self.root2)
            else:
                messagebox.showinfo('Info', 'Marks for selected student have already been provided', parent=self.root2)

        except Exception as e:
            messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root2)
        self.clear()

    def search_tu_id(self, args):
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        try:
            if self.var_tu_id.get() == "":
                messagebox.showinfo('Info', 'Please enter the TU registration number first!', parent=self.root2)
            else:
                if args == 1:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BCA' and "
                                "semester='First' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 2:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BCA' and "
                                "semester='Second' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 3:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BCA' and "
                                "semester='Third' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 4:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BCA' and "
                                "semester='Fourth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 5:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BCA' and "
                                "semester='Fifth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 6:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BCA' and "
                                "semester='Sixth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 7:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BCA' and "
                                "semester='Seventh' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 8:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BCA' and "
                                "semester='Eighth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                info = cur.fetchone()
                if info is None:
                    messagebox.showerror("Error", "Please select valid TU registration id of student for selected"
                                                  " semester.", parent=self.root2)
                else:
                    self.var_name.set(info[0])
                    self.var_roll.set(info[1])
        except Exception as e:
            messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root2)
        self.clear()

    def courses(self, args):
        global json_subs
        self.root2 = Toplevel()
        result_format(self)

        # ==== BCA first semester ====
        if args == 1:
            json_subs = {'Computer Fundamentals and Applications': self.var_sub1,
                         'Society and Technology': self.var_sub2,
                         'English I': self.var_sub3,
                         'Mathematics I': self.var_sub4,
                         'Digital Logic': self.var_sub5
                         }

        # ==== BCA second semester ====
        if args == 2:
            json_subs = {'C programming': self.var_sub1,
                         'Financial Accounting': self.var_sub2,
                         'English II': self.var_sub3,
                         'Mathematics II': self.var_sub4,
                         'Microprocessor and Comp. Architecture': self.var_sub5
                         }

        # ==== BCA third semester ====
        if args == 3:
            json_subs = {'Data Structure and Algorithms': self.var_sub1,
                         'Probability and Statistics': self.var_sub2,
                         'System Analysis and Design': self.var_sub3,
                         'OOP in Java': self.var_sub4,
                         'Web Technology': self.var_sub5
                         }

        # ==== BCA fourth semester ====
        if args == 4:
            json_subs = {'Operating System': self.var_sub1,
                         'Numerical Methods': self.var_sub2,
                         'Software Engineering': self.var_sub3,
                         'Scripting Language': self.var_sub4,
                         'Database Management System': self.var_sub5,
                         'Project I': self.var_sub6
                         }

        # ==== BCA fifth semester ====
        if args == 5:
            json_subs = {'MIS and e-Business': self.var_sub1,
                         'DotNet Technology': self.var_sub2,
                         'Computer Networking': self.var_sub3,
                         'Introduction to Management': self.var_sub4,
                         'Computer Graphics and Animation': self.var_sub5
                         }
        # ==== BCA sixth semester ====
        if args == 6:
            json_subs = {'Mobile Programming': self.var_sub1,
                         'Distributed System': self.var_sub2,
                         'Applied Economics': self.var_sub3,
                         'Advanced Java Programming': self.var_sub4,
                         'Network Programming': self.var_sub5,
                         'Project II': self.var_sub6
                         }

        # ==== BCA seventh semester ====
        if args == 7:
            json_subs = {'Cyber Law and Professional Ethics': self.var_sub1,
                         'Cloud Computing': self.var_sub2,
                         'Internship': self.var_sub3,
                         'Elective Course I': self.var_sub4
                         }

        # ==== BCA eighth semester ====
        if args == 8:
            json_subs = {'Operations Research': self.var_sub1,
                         'Project III': self.var_sub2,
                         'Elective Course II': self.var_sub3
                         }
        a = 290
        for i, j in json_subs.items():
            lbl = Label(self.root2, text=i, font=("times", 15,))
            lbl.place(x=90, y=a)
            sub = Entry(self.root2, textvariable=j, font=("times", 15,))
            sub.place(x=650, y=a, width=50)
            a = a + 50

        btn = Button(self.root2, text='search', command=lambda: self.search_tu_id(args), font=('times', 12, 'bold'),
                     cursor='hand2', bg='light gray', relief=RIDGE, activebackground='gray').place(x=1110, y=57, width=80)

        btn1 = Button(self.root2, text='submit', command=lambda: self.submit_marks(args), font=('times', 12, 'bold'),
                      cursor='hand2', bg='green', relief=RIDGE, activebackground='green').place(x=350, y=610, width=100)

    def __init__(self, root1):
        self.root = root1
        # self.root.title("Semester selection")
        # self.root.geometry("1520x775+1+5")

        self.var_tu_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()

        self.var_sub1 = StringVar()
        self.var_sub2 = StringVar()
        self.var_sub3 = StringVar()
        self.var_sub4 = StringVar()
        self.var_sub5 = StringVar()
        self.var_sub6 = StringVar()

        top_canvas(self)
        left_semester(self)


if __name__ == "__main__":
    root = Tk()
    obj = Semester(root)
    root.mainloop()
