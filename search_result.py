from tkinter import *
import pygetwindow as gw
import pyautogui as ag
from PIL import Image
import sqlite3
from tkinter import messagebox, filedialog
import json
import os


class Result:
    def view_result(self):
        if self.var_tu_registered_id.get() == "" or self.var_password.get() == "":
            messagebox.showerror('Error', 'Please enter tu registration id and your login password.', parent=self.root)
        else:
            try:
                db = sqlite3.connect(database="srms.db")
                cur = db.cursor()
                cur.execute("select name from users where password=? and tu_registered_id=?",
                            (self.var_password.get(), self.var_tu_registered_id.get(),))
                info = cur.fetchone()
                if info is None:
                    messagebox.showerror('Error', 'Please enter valid tu registration id and corresponding password',
                                         parent=self.root)
                else:
                    cur.execute("select a.name,a.email,a.password,a.roll,a.semester,a.year,a.tu_registered_id,"
                                "b.marks from users as a inner join result as b on a.email=b.email where a.password=? "
                                "and a.tu_registered_id=?",
                                (self.var_password.get(), self.var_tu_registered_id.get(),))
                    row = cur.fetchone()
                    if row is None:
                        messagebox.showinfo('Information', f'Sorry Mr./Mrs {str(info[0])}, your result has not been '
                                                           'published yet.', parent=self.root)
                    else:
                        self.show_result(row)
            except Exception as e:
                messagebox.showerror('Error', f'Error due to {str(e)}', parent=self.root)

    def show_result(self, row):
        self.root2 = Toplevel()
        self.root2.title('Result')
        self.root2.geometry('1000x940+450+5')
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.attributes("-toolwindow", 1)

        frame = Frame(self.root2, bg='yellow').place(x=0, y=0, relwidth=1, relheight=1)
        lbl1 = Label(self.root2, text='Kathmandu Bernhardt College', font=('dolphin', 25, 'bold'), bg='yellow')
        lbl1.place(x=270, y=5)

        if row[5] == 'Select':
            sem_name = Label(self.root2, textvariable=self.var_semester, font=('times', 20), bg='yellow', anchor=E).place(x=390, y=60, width=100)
            self.var_semester.set(row[4])
            sem = Label(self.root2, text='semester', font=('times', 20), bg='yellow', anchor=W).place(x=495, y=60)

        if row[4] == 'Select':
            year_name = Label(self.root2, textvariable=self.var_year, font=('times', 20), bg='yellow', anchor=E).place(x=390, y=60, width=100)
            self.var_year.set(row[5])
            year = Label(self.root2, text='year', font=('times', 20), bg='yellow', anchor=W).place(x=495, y=60)

        tu_id = Label(self.root2, text='TU Registration id:', font=('times', 13), bg='yellow').place(x=730, y=140)
        v_tu_id = Label(self.root2, textvariable=self.var_tu_registered_id, font=('times', 13), anchor=W,
                        bg='yellow').place(x=900, y=140)
        self.var_tu_registered_id.set(row[6])

        name = Label(self.root2, text='Name:', font=('times', 13), bg='yellow').place(x=40, y=220)
        v_name = Label(self.root2, textvariable=self.var_name, font=('times', 13), anchor=W,
                       bg='yellow').place(x=110, y=220)
        self.var_name.set(row[0])

        roll = Label(self.root2, text='Roll no:', font=('times', 13), bg='yellow').place(x=40, y=260)
        v_roll = Label(self.root2, textvariable=self.var_roll, font=('times', 13), anchor=W,
                       bg='yellow').place(x=135, y=260)
        self.var_roll.set(row[3])

        sn = Label(self.root2, text='S.N.', font=('times', 15, 'bold'), bd=2, bg='yellow',
                   relief=RIDGE).place(x=100, y=360, width=55, height=40)
        courses = Label(self.root2, text='Courses', font=('times', 15, 'bold'), bd=2, relief=RIDGE, padx=7,
                        bg='yellow').place(x=150, y=360, width=630, height=40)
        marks = Label(self.root2, text='Marks', font=('times', 15, 'bold'), bd=2, bg='yellow',
                      relief=RIDGE).place(x=775, y=360, width=100, height=40)

        sub_list = row[7]
        sub_dict = json.loads(sub_list)
        z = 395
        for k in range(1, len(sub_dict)+1):
            num = Label(self.root2, text=k, font=('times', 15), bd=2, relief=RIDGE, anchor=W, padx=7,
                        bg='yellow').place(x=100, y=z, width=55, height=40)
            z = z + 35

        a, total = 395, 0
        for i, j in sub_dict.items():
            sub = Label(self.root2, text=i, font=('times', 12), bd=2, relief=RIDGE, anchor=W, padx=7,
                        bg='yellow').place(x=150, y=a, width=630, height=40)
            marks = Label(self.root2, text=j, font=('times', 15), bd=2, relief=RIDGE, padx=7,
                          bg='yellow').place(x=775, y=a, width=100, height=40)
            total = total+int(j)
            a = a + 35

        p = StringVar()
        percentage = (format(total/len(sub_dict), ".2f"))
        per = Label(self.root2, text='Percentage:', font=('times', 13), bg='yellow').place(x=40, y=700)
        percent = Label(self.root2, textvariable=p, font=('times', 13), bg='yellow').place(x=155, y=700)
        p.set(str(percentage)+' %')
        num = int(round(float(percentage)))
        rem_dict = {'Fail': range(0, 40), 'Poor': range(40, 55), 'Good': range(55, 70), 'Very good': range(70, 85),
                    'Excellent': range(85, 100)}
        rem = Label(self.root2, text='Remarks:', font=('times', 13), bg='yellow').place(x=40, y=740)

        for l, m in rem_dict.items():   
            if num in m:
                Label(self.root2, text=l, font=('times', 13), bg='yellow').place(x=140, y=740)

        Button(self.root2, text='Download', font=('times', 13, 'bold'), cursor='hand2', command=self.download_result,
               bg='red', activebackground='red').place(x=435, y=880)

    def download_result(self):
        hor, ver = gw.getActiveWindow().topleft
        width, height = gw.getActiveWindow().size
        x1 = hor + 10
        y1 = ver + 40

        x2 = x1 + width-20
        y2 = y1 + height-120

        ag.screenshot(r'C:/Users/user/Desktop/result.png')

        im = Image.open(r'C:/Users/user/Desktop/result.png')
        im = im.crop((x1, y1, x2, y2))

        # converting the cropped image to pdf
        im1 = im.convert('RGB')
        im1.save(r'C:/Users/user/Desktop/result.pdf')

        os.remove(r'C:/Users/user/Desktop/result.png')
        messagebox.showinfo('Information', 'Result has been saved in your desktop.', parent=self.root2)

    def __init__(self, root1):
        self.root = root1
        self.root.title('View Result')
        self.root.geometry('500x250+700+100')
        self.root.attributes("-toolwindow", 1)

        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_roll = StringVar()
        self.var_semester = StringVar()
        self.var_year = StringVar()
        self.var_tu_registered_id = StringVar()
        self.var_marks = StringVar()

        tu_id = Label(self.root, text='TU registration id:', font=('times', 13)).place(x=40, y=50)
        f_tu_id = Entry(self.root, text='enter tu id', textvariable=self.var_tu_registered_id, font=('times', 13))
        f_tu_id.place(x=220, y=50)
        password = Label(self.root, text='Password:', font=('times', 13)).place(x=40, y=90)
        f_password = Entry(self.root, text='password:', show="*", textvariable=self.var_password, font=('times', 13))
        f_password.place(x=220, y=90)
        btn = Button(self.root, text='View Result', command=self.view_result, font=('times', 15, 'bold'),
                     cursor='hand2').place(x=150, y=160)


if __name__ == "__main__":
    root = Tk()
    obj = Result(root)
    root.mainloop()

