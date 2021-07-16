from tkinter import *
from modu import top_canvas, left_year, result_format
import sqlite3
from tkinter import messagebox
import json


class Year:
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
                    json_dict = {'English': self.var_sub1.get(),
                                 'Business Studies': self.var_sub2.get(),
                                 'Micro Economics': self.var_sub3.get(),
                                 'Cost and Management Accountancy': self.var_sub4.get(),
                                 'Principles of Management': self.var_sub5.get(),
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 2:
                    json_dict = {'Business Communication': self.var_sub1.get(),
                                 'Macro Economics': self.var_sub2.get(),
                                 'Cost and Management Accounting': self.var_sub3.get(),
                                 'Fundamentals of Marketing': self.var_sub4.get(),
                                 'Fundamentals of Human Resource Management': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 3:
                    json_dict = {'Business Environment Strategy': self.var_sub1.get(),
                                 'Fundamental of Financial Management': self.var_sub2.get(),
                                 'Business Law': self.var_sub3.get(),
                                 'Taxation and Auditing': self.var_sub4.get(),
                                 'Organizational Behavior': self.var_sub5.get(),
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 4:
                    json_dict = {'Entrepreneurship and Enterprise Development': self.var_sub1.get(),
                                 'Business Research Methods-50/Final Project-50': self.var_sub2.get(),
                                 'Concentration I': self.var_sub3.get(),
                                 'Concentration II': self.var_sub4.get(),
                                 }
                    self.json_marks = json.dumps(json_dict)

                cur.execute("insert into result (email,marks) values((select email from users where tu_registered_id=?), "
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
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBS' and "
                                "year='First' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 2:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBS' and "
                                "year='Second' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 3:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBS' and "
                                "year='Third' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 4:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BBS' and "
                                "year='Fourth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                info = cur.fetchone()
                if info is None:
                    messagebox.showerror("Error", "Please select valid TU registration id of student for selected "
                                                  "year.", parent=self.root2)
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
        # ==== BBS first year ====
        if args == 1:
            json_subs = {'English': self.var_sub1,
                         'Business Studies': self.var_sub2,
                         'Micro Economics': self.var_sub3,
                         'Cost and Management Accountancy': self.var_sub4,
                         'Principles of Management': self.var_sub5,
                         }
        # ==== BBS second year ====
        if args == 2:
            json_subs = {'Business Communication': self.var_sub1,
                         'Macro Economics': self.var_sub2,
                         'Cost and Management Accounting': self.var_sub3,
                         'Fundamentals of Marketing': self.var_sub4,
                         'Fundamentals of Human Resource Management': self.var_sub5
                         }
        # ==== BBS Third year ====
        if args == 3:
            json_subs = {'Business Environment Strategy': self.var_sub1,
                         'Fundamental of Financial Management': self.var_sub2,
                         'Business Law': self.var_sub3,
                         'Taxation and Auditing': self.var_sub4,
                         'Organizational Behavior': self.var_sub5,
                         }

        # ==== BBS Fourth year ====
        if args == 4:
            json_subs = {'Entrepreneurship and Enterprise Development': self.var_sub1,
                         'Business Research Methods-50/Final Project-50': self.var_sub2,
                         'Concentration I': self.var_sub3,
                         'Concentration II': self.var_sub4,
                         }

        a = 290
        for i, j in json_subs.items():
            lbl = Label(self.root2, text=i, font=("times", 15,))
            lbl.place(x=90, y=a)
            sub = Entry(self.root2, textvariable=j, font=("times", 15,))
            sub.place(x=650, y=a, width=50)
            a = a + 50

        btn = Button(self.root2, text='search', command=lambda: self.search_tu_id(args), font=('times', 12, 'bold'),
                     cursor='hand2', bg='light gray', relief=RIDGE, activebackground='gray').place(x=1110, y=57,
                                                                                                   width=80)

        btn1 = Button(self.root2, text='submit', command=lambda: self.submit_marks(args), font=('times', 12, 'bold'),
                      cursor='hand2', bg='green', relief=RIDGE, activebackground='green').place(x=350, y=610, width=100)

    def __init__(self, root1):
        self.root = root1
        # self.root.title("Year selection")
        # self.root.geometry("1520x775+1+5")

        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_tu_id = StringVar()

        self.var_sub1 = StringVar()
        self.var_sub2 = StringVar()
        self.var_sub3 = StringVar()
        self.var_sub4 = StringVar()
        self.var_sub5 = StringVar()

        top_canvas(self)
        left_year(self)


if __name__ == "__main__":
    root = Tk()
    obj = Year(root)
    root.mainloop()
