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
                    json_dict = {'Reading for English Language Learning': self.var_sub1.get(),
                                 'नेपाली व्याकरण र पाठ बोध': self.var_sub2.get(),
                                 'Foundations of Public Service': self.var_sub3.get(),
                                 'Administrative Studies': self.var_sub4.get(),
                                 'Context of Public Service I': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 2:
                    json_dict = {'Professional English': self.var_sub1.get(),
                                 'सामान्य नेपाली र प्रकर्यपरक लेखन': self.var_sub2.get(),
                                 'Fundamentals of Computer Application': self.var_sub3.get(),
                                 'Context of Public Service II': self.var_sub4.get(),
                                 'Public Services Management-I': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 3:
                    json_dict = {'Competencies for Public Service Profession  I': self.var_sub1.get(),
                                 'Human Resource Management': self.var_sub2.get(),
                                 'Applied Mathematics and Statistics': self.var_sub3.get(),
                                 'Research Methodology': self.var_sub4.get(),
                                 'Microeconomics': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 4:
                    json_dict = {'Fundamentals of  Psychology': self.var_sub1.get(),
                                 'Macroeconomics and Policy Analysis': self.var_sub2.get(),
                                 'Public Policy and National Policies of Nepal': self.var_sub3.get(),
                                 'Design and Delivery of Development': self.var_sub4.get(),
                                 'Internship–I': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 5:
                    json_dict = {'Nepalese Administration System': self.var_sub1.get(),
                                 'Dynamics of Population, Gender and Development': self.var_sub2.get(),
                                 'Work Psychology and Application': self.var_sub3.get(),
                                 'Revenue Governance and Taxation': self.var_sub4.get(),
                                 'Political Philosophies': self.var_sub5.get(),
                                 'Research Seminar Paper II': self.var_sub6.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 6:
                    json_dict = {'Corporate Governance': self.var_sub1.get(),
                                 'Public Service Accounting and Auditing': self.var_sub2.get(),
                                 'Nepalese Society, Cultural Heritage and Tourism': self.var_sub3.get(),
                                 'Ethics for Public Service Professionals': self.var_sub4.get(),
                                 'Internship-II': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 7:
                    json_dict = {'Nepalese Administrative Laws': self.var_sub1.get(),
                                 'Public Services Management - II': self.var_sub2.get(),
                                 'International Relations': self.var_sub3.get(),
                                 'Issues in Public Service Management': self.var_sub4.get(),
                                 'Research Seminar Paper III': self.var_sub5.get()
                                 }
                    self.json_marks = json.dumps(json_dict)

                if args == 8:
                    json_dict = {'Natural Resources Management': self.var_sub1.get(),
                                 'Nepalese Fiscal Laws': self.var_sub2.get(),
                                 'Comparative Governance': self.var_sub3.get(),
                                 'Internship - III': self.var_sub3.get()
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
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BPSG' and "
                                "semester='First' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 2:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BPSG' and "
                                "semester='Second' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 3:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BPSG' and "
                                "semester='Third' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 4:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BPSG' and "
                                "semester='Fourth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 5:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BPSG' and "
                                "semester='Fifth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 6:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BPSG' and "
                                "semester='Sixth' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 7:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BPSG' and "
                                "semester='Seventh' and profession=2 and permission=1", (self.var_tu_id.get(),))
                if args == 8:
                    cur.execute("select name,roll from users where tu_registered_id=? and faculty='BPSG' and "
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

        # ==== BPSG first semester ====
        if args == 1:
            json_subs = {'Reading for English Language Learning': self.var_sub1,
                         'नेपाली व्याकरण र पाठ बोध': self.var_sub2,
                         'Foundations of Public Service': self.var_sub3,
                         'Administrative Studies': self.var_sub4,
                         'Context of Public Service I': self.var_sub5
                         }

        # ==== BPSG second semester ====
        if args == 2:
            json_subs = {'Professional English': self.var_sub1,
                         'सामान्य नेपाली र प्रकर्यपरक लेखन': self.var_sub2,
                         'Fundamentals of Computer Application': self.var_sub3,
                         'Context of Public Service II': self.var_sub4,
                         'Public Services Management-I': self.var_sub5
                         }

        # ==== BPSG third semester ====
        if args == 3:
            json_subs = {'Competencies for Public Service Profession  I': self.var_sub1,
                         'Human Resource Management': self.var_sub2,
                         'Applied Mathematics and Statistics': self.var_sub3,
                         'Research Methodology': self.var_sub4,
                         'Microeconomics': self.var_sub5
                         }

        # ==== BPSG fourth semester ====
        if args == 4:
            json_subs = {'Fundamentals of  Psychology': self.var_sub1,
                         'Macroeconomics and Policy Analysis': self.var_sub2,
                         'Public Policy and National Policies of Nepal': self.var_sub3,
                         'Design and Delivery of Development': self.var_sub4,
                         'Internship–I': self.var_sub5
                         }

        # ==== BPSG fifth semester ====
        if args == 5:
            json_subs = {'Nepalese Administration System': self.var_sub1,
                         'Dynamics of Population, Gender and Development': self.var_sub2,
                         'Work Psychology and Application': self.var_sub3,
                         'Revenue Governance and Taxation': self.var_sub4,
                         'Political Philosophies': self.var_sub5,
                         'Research Seminar Paper II': self.var_sub6
                         }

        # ==== BPSG sixth semester ====
        if args == 6:
            json_subs = {'Corporate Governance': self.var_sub1,
                         'Public Service Accounting and Auditing': self.var_sub2,
                         'Nepalese Society, Cultural Heritage and Tourism': self.var_sub3,
                         'Ethics for Public Service Professionals': self.var_sub4,
                         'Internship-II': self.var_sub5
                         }

        # ==== BPSG seventh semester ====
        if args == 7:
            json_subs = {'Nepalese Administrative Laws': self.var_sub1,
                         'Public Services Management - II': self.var_sub2,
                         'International Relations': self.var_sub3,
                         'Issues in Public Service Management': self.var_sub4,
                         'Research Seminar Paper III': self.var_sub5
                         }

        # ==== BPSG eighth semester ====
        if args == 8:
            json_subs = {'Natural Resources Management': self.var_sub1,
                         'Nepalese Fiscal Laws': self.var_sub2,
                         'Comparative Governance': self.var_sub3,
                         'Internship - III': self.var_sub3
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
