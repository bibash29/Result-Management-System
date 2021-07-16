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

    def submit_marks(self, args):
        db = sqlite3.connect(database="srms.db")
        cur = db.cursor()
        try:
            cur.execute("select marks from result where email = (select email from users where tu_registered_id=?)",
                        (self.var_tu_id.get(),))
            record = cur.fetchone()
            if record is None:
                if args == 1:
                    json_dict = {'Introduction to Social Work': self.var_sub1.get(),
                                 'Basic Sociology for Social Work:': self.var_sub2.get(),
                                 'Reading and Writing in English': self.var_sub3.get(),
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 2:
                    json_dict = {'Basic Psychology for Social Work': self.var_sub1.get(),
                                 'Social Case Work Practice': self.var_sub2.get(),
                                 'Social Work Practice With Groups': self.var_sub3.get(),
                                 'Compulsory Nepali': self.var_sub4.get(),
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 3:
                    json_dict = {'Social Issues and Leadership Development': self.var_sub1.get(),
                                 'Social Issues and Leadership Development (Elective)': self.var_sub2.get(),
                                 'Reading and Writing Across the Disciplines': self.var_sub3.get(),
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 4:
                    json_dict = {'Theoretical Ideologies of Social Work': self.var_sub1.get(),
                                 'Social Problem, Identifications, and Interventions': self.var_sub2.get(),
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
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BASW' and "
                                "year='First' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 2:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BASW' and "
                                "year='Second' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 3:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BASW' and "
                                "year='Third' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 4:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BASW' and "
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
        # ==== BASW first year ====
        if args == 1:
            json_subs = {'Introduction to Social Work': self.var_sub1,
                         'Basic Sociology for Social Work:': self.var_sub2,
                         'Reading and Writing in English': self.var_sub3,
                         }
        # ==== BASW second year ====
        if args == 2:
            json_subs = {'Basic Psychology for Social Work': self.var_sub1,
                         'Social Case Work Practice': self.var_sub2,
                         'Social Work Practice With Groups': self.var_sub3,
                         'Compulsory Nepali': self.var_sub4,
                         }

        # ==== BASW Third year ====
        if args == 3:
            json_subs = {'Social Issues and Leadership Development': self.var_sub1,
                         'Social Issues and Leadership Development (Elective)': self.var_sub2,
                         'Reading and Writing Across the Disciplines': self.var_sub3,
                         }

        # ==== BASW Fourth year ====
        if args == 4:
            json_subs = {'Theoretical Ideologies of Social Work': self.var_sub1,
                         'Social Problem, Identifications, and Interventions': self.var_sub2,
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
        # self.root.title("Year selection")
        # self.root.geometry("1520x775+1+5")

        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_tu_id = StringVar()

        self.var_sub1 = StringVar()
        self.var_sub2 = StringVar()
        self.var_sub3 = StringVar()
        self.var_sub4 = StringVar()

        top_canvas(self)
        left_year(self)


if __name__ == "__main__":
    root = Tk()
    obj = Year(root)
    root.mainloop()
