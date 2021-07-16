from tkinter import *
from PIL import ImageTk
import os
from tkinter import messagebox
import sqlite3
from search_result import Result


class Dashboard:
    def view_result(self):
        if self.var_tu_registered_id.get() == "":
            messagebox.showerror('Error', 'Please enter tu registration id to proceed.', parent=self.root)
        else:
            try:
                db = sqlite3.connect(database="srms.db")
                cur = db.cursor()
                cur.execute("select name from users where tu_registered_id=?", (self.var_tu_registered_id.get(),))
                info = cur.fetchone()
                if info is None:
                    messagebox.showerror('Error', 'Please enter valid tu registration id.', parent=self.root)
                else:
                    cur.execute("select a.name,a.email,a.password,a.roll,a.semester,a.year,a.tu_registered_id,"
                                "b.marks from users as a inner join result as b on a.email=b.email where"
                                " a.tu_registered_id=?", (self.var_tu_registered_id.get(),))
                    row = cur.fetchone()
                    if row is None:
                        messagebox.showinfo('Information', f'Sorry,result has not yet been published for Mr/Mrs'
                                                           f' {str(info[0])}.', parent=self.root)
                    else:
                        Result.show_result(self, row)
            except Exception as e:
                if str(e) == "'Dashboard' object has no attribute 'download_result'":
                    pass
                else:
                    messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    def delete_result(self):
        if self.var_tu_registered_id.get() == "":
            messagebox.showerror('Error', 'Please enter tu registration id to proceed.', parent=self.root)
        else:
            try:
                db = sqlite3.connect(database="srms.db")
                cur = db.cursor()
                cur.execute("select name,faculty,semester,year from users where tu_registered_id=?",
                            (self.var_tu_registered_id.get(),))
                info = cur.fetchone()
                if info is None:
                    messagebox.showerror('Error', 'Please enter valid tu registration id.', parent=self.root)
                else:
                    cur.execute("select a.name,a.email,a.semester,a.year,a.tu_registered_id "
                                "from users as a inner join result as b on a.email=b.email where"
                                " a.tu_registered_id=?", (self.var_tu_registered_id.get(),))
                    row = cur.fetchone()
                    if row is None:
                        messagebox.showinfo('Information', f'Sorry,result has not yet been published for Mr/Mrs'
                                                           f'{str(info[0])}.', parent=self.root)
                    else:
                        op = messagebox.askyesno('Confirm', f'Are you sure you want to delete result for Mr./Mrs. '
                                                 f'{str(info[0])}?')
                        if op:
                            cur.execute("delete from result where email in (select a.email from users as a inner join "
                                        "result as b on a.email=b.email where a.tu_registered_id=?)",
                                        (self.var_tu_registered_id.get(),))
                            db.commit()
                            if info[3] == 'Select':
                                messagebox.showinfo('Confirmation', f'Result for {str(info[0])} pursuing {str(info[1])} in '
                                                    f'{str(info[2])} semester has been deleted successfully.', parent=self.root)
                            if info[2] == 'Select':
                                messagebox.showinfo('Confirmation', f'Result for {str(info[0])} pursuing {str(info[1])} in '
                                                    f'{str(info[3])} year has been deleted successfully.', parent=self.root)
                            db.close()
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    def enter_result(self):
        os.system('python faculty.py')

    def call_admin(self):
        self.root.destroy()
        os.system('python admin.py')

    def search(self, args):
        self.root3 = Toplevel()
        self.root3.title('Entry')
        self.root3.geometry('400x200+750+150')
        self.root3.focus_force()
        self.root3.grab_set()
        self.root3.attributes("-toolwindow", 1)

        tu_id = Label(self.root3, text='TU registration id:', font=('times', 13)).place(x=20, y=50)
        f_tu_id = Entry(self.root3, text='enter tu id', textvariable=self.var_tu_registered_id, font=('times', 13))
        f_tu_id.place(x=200, y=50, width=160)
        self.var_tu_registered_id.set("")
        if args == 1:
            btn = Button(self.root3, text='View Result', command=self.view_result, cursor='hand2',
                         font=('times', 15, 'bold')).place(x=120, y=100)
        if args == 2:
            btn = Button(self.root3, text='Delete Result', command=self.delete_result, cursor='hand2',
                         font=('times', 15, 'bold')).place(x=120, y=100)

    def logout(self):
        op = messagebox.askyesno('Info', 'Are you sure you want to logout?', parent=self.root)
        if op:
            self.root.destroy()
            os.system('python login.py')

    def exit(self):
        op = messagebox.askyesno('Info', 'Are you sure you want to exit?', parent=self.root)
        if op:
            self.root.destroy()

    def __init__(self, root1):
        self.root = root1
        self.root.title("Dashboard")
        self.root.geometry("1200x700+350+50")
        self.root.configure(bg='purple')
        self.root.focus_force()
        self.root.grab_set()
        self.root.attributes("-toolwindow", 1)

        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_roll = StringVar()
        self.var_semester = StringVar()
        self.var_year = StringVar()
        self.var_tu_registered_id = StringVar()
        self.var_marks = StringVar()

        Label(self.root, text='Result Management Section', font=("times", 20, "bold"), fg='white', bg="purple").place(x=400, y=5)
        menu = LabelFrame(self.root, text='Menus', font=("times", 15, "bold"), bg="purple")
        menu.place(x=70, y=80, width=1060, height=100)

        Button(self.root, text='Enter Result', command=self.enter_result, font=("times", 13, "bold"),
               cursor='hand2').place(x=100, y=120, width=150)

        Button(self.root, text='View Students Result', command=lambda: self.search(1), font=("times", 13, "bold"),
               cursor='hand2').place(x=290, y=120)

        Button(self.root, text='Delete Results', command=lambda: self.search(2), font=("times", 13, "bold"),
               cursor='hand2').place(x=555, y=120)

        Button(self.root, text='Logout', command=self.logout, font=("times", 13, "bold"),
               cursor='hand2').place(x=755, y=120, width=150)

        Button(self.root, text='Exit', command=self.exit,  font=("times", 13, "bold"),
               cursor='hand2').place(x=950, y=120, width=150)

        Button(self.root, text='Go to admin page >>>', command=self.call_admin, font=("times", 13, "bold"),
               cursor='hand2').place(x=500, y=640, width=250)

        self.bg = ImageTk.PhotoImage(file="images/res.jpg")
        bg = Label(self.root, image=self.bg).place(x=240, y=200)


if __name__ == "__main__":
    root = Tk()
    obj = Dashboard(root)
    root.mainloop()
