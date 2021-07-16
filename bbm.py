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
        try:
            cur.execute("select marks from result where email = (select email from users where tu_registered_id=?)",
                        (self.var_tu_id.get(),))
            record = cur.fetchone()
            if record is None:
                if args == 1:
                    json_dict = {'Introductory Microeconomics': self.var_sub1.get(),
                                 'English I': self.var_sub2.get(),
                                 'Principles of Management': self.var_sub3.get(),
                                 'Business Mathematics I': self.var_sub4.get(),
                                 'Sociology for Business': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 2:
                    json_dict = {'Financial Accounting': self.var_sub1.get(),
                                 'Introductory Macroeconomics': self.var_sub2.get(),
                                 'English II': self.var_sub3.get(),
                                 'Business Mathematics II': self.var_sub4.get(),
                                 'Psychology': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 3:
                    json_dict = {'Computer-Based Financial Accounting': self.var_sub1.get(),
                                 'Business Communications': self.var_sub2.get(),
                                 'Basic Finance': self.var_sub3.get(),
                                 'Nepalese Society and Politics': self.var_sub4.get(),
                                 'Business Statistics': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 4:
                    json_dict = {'Accounting for Decision Making': self.var_sub1.get(),
                                 'Financial Management': self.var_sub2.get(),
                                 'Human Resource Management': self.var_sub3.get(),
                                 'Taxation in Nepal': self.var_sub4.get(),
                                 'Business Research Methods': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 5:
                    json_dict = {'Organizational Behavior': self.var_sub1.get(),
                                 'Fundamentals of Marketing': self.var_sub2.get(),
                                 'Introduction to Operations Management': self.var_sub3.get(),
                                 'Legal Environment of Business': self.var_sub4.get(),
                                 'Focus Area Course I': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 6:
                    json_dict = {'Focus Area Course II': self.var_sub1.get(),
                                 'Database Management': self.var_sub2.get(),
                                 'Business Environment in Nepal': self.var_sub3.get(),
                                 'Introduction to International Business': self.var_sub4.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 7:
                    json_dict = {'Elective Course I': self.var_sub1.get(),
                                 'Focus Area Course III': self.var_sub2.get(),
                                 'E-commerce': self.var_sub3.get(),
                                 'Business Ethics and Social Responsibility': self.var_sub4.get(),
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 8:
                    json_dict = {'Business Strategy': self.var_sub1.get(),
                                 'Elective Course II': self.var_sub2.get(),
                                 'Elective Course III': self.var_sub3.get(),
                                 'Focus Area Course IV': self.var_sub4.get(),
                                 'Internship': self.var_sub5.get()
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
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBM' and "
                                "semester='First' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 2:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBM' and "
                                "semester='Second' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 3:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBM' and "
                                "semester='Third' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 4:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBM' and "
                                "semester='Fourth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 5:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBM' and "
                                "semester='Fifth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 6:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBM' and "
                                "semester='Sixth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 7:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBM' and "
                                "semester='Seventh' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 8:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBM' and "
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

        # ==== BBM first semester ====
        if args == 1:
            json_subs = {'Introductory Microeconomics': self.var_sub1,
                         'English I': self.var_sub2,
                         'Principles of Management': self.var_sub3,
                         'Business Mathematics I': self.var_sub4,
                         'Sociology for Business': self.var_sub5
                         }

        # ==== BBM second semester ====
        if args == 2:
            json_subs = {'Financial Accounting': self.var_sub1,
                         'Introductory Macroeconomics': self.var_sub2,
                         'English II': self.var_sub3,
                         'Business Mathematics II': self.var_sub4,
                         'Psychology': self.var_sub5
                         }

        # ==== BBM third semester ====
        if args == 3:
            json_subs = {'Computer-Based Financial Accounting': self.var_sub1,
                         'Business Communications': self.var_sub2,
                         'Basic Finance': self.var_sub3,
                         'Nepalese Society and Politics': self.var_sub4,
                         'Business Statistics': self.var_sub5
                         }

        # ==== BBM fourth semester ====
        if args == 4:
            json_subs = {'Accounting for Decision Making': self.var_sub1,
                         'Financial Management': self.var_sub2,
                         'Human Resource Management': self.var_sub3,
                         'Taxation in Nepal': self.var_sub4,
                         'Business Research Methods': self.var_sub5
                         }

        # ==== BBM fifth semester ====
        if args == 5:
            json_subs = {'Organizational Behavior': self.var_sub1,
                         'Fundamentals of Marketing': self.var_sub2,
                         'Introduction to Operations Management': self.var_sub3,
                         'Legal Environment of Business': self.var_sub4,
                         'Focus Area Course I': self.var_sub5
                         }
        # ==== BBM sixth semester ====
        if args == 6:
            json_subs = {'Focus Area Course II': self.var_sub1,
                         'Database Management': self.var_sub2,
                         'Business Environment in Nepal': self.var_sub3,
                         'Introduction to International Business': self.var_sub4
                         }

        # ==== BBM seventh semester ====
        if args == 7:
            json_subs = {'Elective Course I': self.var_sub1,
                         'Focus Area Course III': self.var_sub2,
                         'E-commerce': self.var_sub3,
                         'Business Ethics and Social Responsibility': self.var_sub4,
                         }

        # ==== BBM eighth semester ====
        if args == 8:
            json_subs = {'Business Strategy': self.var_sub1,
                         'Elective Course II': self.var_sub2,
                         'Elective Course III': self.var_sub3,
                         'Focus Area Course IV': self.var_sub4,
                         'Internship': self.var_sub5
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
