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

    def submit_marks(self, args):
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        # cur.execute("create table if not exists result(rid int(6) NOT NULL AUTO_INCREMENT, marks blob(1000), "
        #             "email varchar(50), PRIMARY KEY(rid), FOREIGN KEY(email) REFERENCES users(email))")
        try:
            cur.execute("select marks from result where email = (select email from users where tu_registered_id=?)",
                        (self.var_tu_id.get(),))
            record = cur.fetchone()
            if record is None:
                if args == 1:
                    json_dict = {'Introduction to Information Technology': self.var_sub1.get(),
                                 'C Programming': self.var_sub2.get(),
                                 'Digital Logic': self.var_sub3.get(),
                                 'Mathematics I': self.var_sub4.get(),
                                 'Physics': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 2:
                    json_dict = {'Discrete Structure': self.var_sub1.get(),
                                 'Object Oriented Programming': self.var_sub2.get(),
                                 'Microprocessor': self.var_sub3.get(),
                                 'Mathematics II': self.var_sub4.get(),
                                 'Statistics I': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 3:
                    json_dict = {'Data Structure and Algorithms': self.var_sub1.get(),
                                 'Numerical Method': self.var_sub2.get(),
                                 'Computer Architecture': self.var_sub3.get(),
                                 'Computer Graphics': self.var_sub4.get(),
                                 'Statistics II': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 4:
                    json_dict = {'Theory of Computations': self.var_sub1.get(),
                                 'Computer Networks': self.var_sub2.get(),
                                 'Operating Systems': self.var_sub3.get(),
                                 'Database Management Systems': self.var_sub4.get(),
                                 'Artificial Intelligence': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 5:
                    json_dict = {'Design and Analysis of Algorithms': self.var_sub1.get(),
                                 'System Analysis and Design': self.var_sub2.get(),
                                 'Cryptography': self.var_sub3.get(),
                                 'Simulation and Modeling': self.var_sub4.get(),
                                 'Web Technology': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 6:
                    json_dict = {'Software Engineering': self.var_sub1.get(),
                                 'Compiler Design and Construction': self.var_sub2.get(),
                                 'E-governance': self.var_sub3.get(),
                                 'Net-Centric Computing': self.var_sub4.get(),
                                 'Technical Writing': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 7:
                    json_dict = {'Advanced Java Programming': self.var_sub1.get(),
                                 'Data Warehousing and Data Mining': self.var_sub2.get(),
                                 'Database Administration': self.var_sub3.get(),
                                 'Project Work': self.var_sub4.get(),
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 8:
                    json_dict = {'Advanced Database': self.var_sub1.get(),
                                 'Introduction to Cloud Computing': self.var_sub2.get(),
                                 'Geographical Information System': self.var_sub3.get(),
                                 'Internship': self.var_sub4.get()
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
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BSc.CSIT' and "
                                "semester='First' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 2:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BSc.CSIT' and "
                                "semester='Second' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 3:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BSc.CSIT' and "
                                "semester='Third' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 4:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BSc.CSIT' and "
                                "semester='Fourth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 5:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BSc.CSIT' and "
                                "semester='Fifth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 6:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BSc.CSIT' and "
                                "semester='Sixth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 7:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BSc.CSIT' and "
                                "semester='Seventh' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 8:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BSc.CSIT' and "
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

        # ==== BSc.CSIT first semester ====
        if args == 1:
            json_subs = {'Introduction to Information Technology:': self.var_sub1,
                         'C Programming:': self.var_sub2,
                         'Digital Logic:': self.var_sub3,
                         'Mathematics I:': self.var_sub4,
                         'Physics:': self.var_sub5
                         }

        # ==== BSc.CSIT second semester ====
        if args == 2:
            json_subs = {'Discrete Structure': self.var_sub1,
                         'Object Oriented Programming': self.var_sub2,
                         'Microprocessor': self.var_sub3,
                         'Mathematics II': self.var_sub4,
                         'Statistics I': self.var_sub5
                         }

        # ==== BSc.CSIT third semester ====
        if args == 3:
            json_subs = {'Data Structure and Algorithms': self.var_sub1,
                         'Numerical Method': self.var_sub2,
                         'Computer Architecture': self.var_sub3,
                         'Computer Graphics': self.var_sub4,
                         'Statistics II': self.var_sub5
                         }

        # ==== BSc.CSIT fourth semester ====
        if args == 4:
            json_subs = {'Theory of Computations': self.var_sub1,
                         'Computer Networks': self.var_sub2,
                         'Operating Systems': self.var_sub3,
                         'Database Management Systems': self.var_sub4,
                         'Artificial Intelligence': self.var_sub5
                         }

        # ==== BSc.CSIT fifth semester ====
        if args == 5:
            json_subs = {'Design and Analysis of Algorithms': self.var_sub1,
                         'System Analysis and Design': self.var_sub2,
                         'Cryptography': self.var_sub3,
                         'Simulation and Modeling': self.var_sub4,
                         'Web Technology': self.var_sub5
                         }

        # ==== BSc.CSIT sixth semester ====
        if args == 6:
            json_subs = {'Software Engineering': self.var_sub1,
                         'Compiler Design and Construction': self.var_sub2,
                         'E-governance': self.var_sub3,
                         'Net-Centric Computing': self.var_sub4,
                         'Technical Writing': self.var_sub5
                         }

        # ==== BSc.CSIT seventh semester ====
        if args == 7:
            json_subs = {'Advanced Java Programming': self.var_sub1,
                         'Data Warehousing and Data Mining': self.var_sub2,
                         'Database Administration': self.var_sub3,
                         'Project Work': self.var_sub4,
                         }

        # ==== BSc.CSIT eighth semester ====
        if args == 8:
            json_subs = {'Advanced Database': self.var_sub1,
                         'Introduction to Cloud Computing': self.var_sub2,
                         'Geographical Information System': self.var_sub3,
                         'Internship': self.var_sub4,
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

        top_canvas(self)
        left_semester(self)


if __name__ == "__main__":
    root = Tk()
    obj = Semester(root)
    root.mainloop()
