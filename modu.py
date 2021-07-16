from tkinter import *
from PIL import ImageTk
import mysql.connector as sql
from tkinter import messagebox


# ==== for print kbs at top ====
def top_canvas(self):
    canvas = Canvas(self.root, width=1510, height=90, bg="yellow")
    canvas.place(x=0, y=0, relwidth=1)

    canvas.img = ImageTk.PhotoImage(file="images/kbc.png")
    # canvas.create_image(400, 46.5, image=canvas.img)

    topic = Label(canvas, text="Kathmandu Bernhardt College", padx=20, compound=LEFT, image=canvas.img, font=("dolphin", 40),
                  fg="black", bg="yellow")
    topic.place(x=0, y=0, relwidth=1, relheight=1)

    self.bg = ImageTk.PhotoImage(file="images/class1.jpg")
    bg = Label(self.root, image=self.bg).place(x=400, y=99, width=1115, height=670)


# ==== Label Frame for semester ====
def left_semester(self):
    self.root.title("Semester selection")
    self.root.geometry("1520x775+1+5")
    self.root.attributes("-toolwindow", 1)

    # ==== Left canvas part for semester ====
    # self.canvas1 = Canvas(self.root, width=390, bd=2, height=667, bg="#5900a6")
    # self.canvas1.place(x=0, y=97)

    l_semester = LabelFrame(self.root, text="Semesters", font=("times", 17, "bold"), labelanchor='n',
                            bg="#5900a6", fg="white", bd=5)
    l_semester.place(x=4, y=100, width=392, height=670)

    text = Label(self.root, text="Select the semester of the student below \n to enter the marks:",
                 font=("times", 15, "bold"), bg="#5900a6", fg="white")
    text.place(x=20, y=140)

    m = {1: 'First', 2: 'Second', 3: 'Third', 4: 'Fourth', 5: 'Fifth', 6: 'Sixth', 7: 'Seventh', 8: 'Eighth'}
    p, q = 65, 250
    btn = []
    for i, j in m.items():
        btn.append(Button(self.root, text=j, command=lambda i=i: self.courses(i), font=('times', 13, 'bold'),
                          fg='black', bg='white', bd=3, cursor='hand2').place(x=p, y=q, width=100))
        if i % 2 == 1:
            p = p + 165
        else:
            p = p - 165
            q = q + 100


# ==== Label Frame for year ====
def left_year(self):
    self.root.title("Year selection")
    self.root.geometry("1520x775+1+5")
    self.root.attributes("-toolwindow", 1)

    # ==== Left canvas part for year ====
    # canvas1 = Canvas(self.root, width=390, bd=2, height=667, bg="#5900a6")
    # canvas1.place(x=0, y=97)

    l_year = LabelFrame(self.root, text="Year", font=("times", 17, "bold"), labelanchor='n',
                        bg="#5900a6", fg="white", takefocus=TRUE, bd=5)
    l_year.place(x=4, y=100, width=392, height=670)

    text = Label(self.root, text="Select the year of the student below \n to enter the marks:",
                 font=("times", 15, "bold"), bg="#5900a6", fg="white")
    text.place(x=40, y=140)
    m = {1: 'First', 2: 'Second', 3: 'Third', 4: 'Fourth'}
    q = 265
    btn = []
    for i, j in m.items():
        btn.append(Button(self.root, text=j, command=lambda i=i: self.courses(i), font=('times', 13, 'bold'),
                          fg='black', bg='white', bd=3, cursor='hand2').place(x=150, y=q, width=100))
        q = q + 100


def result_format(self):
    self.root2.title('Results Entry')
    self.root2.geometry('1200x670+150+70')
    self.root2.focus_force()
    self.root2.grab_set()
    self.root2.attributes("-toolwindow", 1)

    lbl = Label(self.root2, text="Result Entry Section", font=("times", 20, "bold"), fg='white', bg="purple", )
    lbl.place(x=0, y=0, relwidth=1)

    lbl_tu_id = Label(self.root2, text="TU Registration no:", font=("times", 14, "bold"))
    lbl_tu_id.place(x=800, y=60)
    f_tu_id = Entry(self.root2, textvariable=self.var_tu_id, font=("times", 15,))
    f_tu_id.place(x=980, y=60, width=120)

    lbl_name = Label(self.root2, text="Name:", font=("times", 15, "bold"))
    lbl_name.place(x=70, y=130)
    f_name = Entry(self.root2, textvariable=self.var_name, font=("times", 15,), state='readonly')
    f_name.place(x=150, y=130, width=240)

    lbl_roll = Label(self.root2, text="Roll no:", font=("times", 15, "bold"))
    lbl_roll.place(x=70, y=180)
    f_roll = Entry(self.root2, textvariable=self.var_roll, font=("times", 15,), state='readonly')
    f_roll.place(x=150, y=180, width=70)

    l_marks = LabelFrame(self.root2, text="Enter Marks for subject", font=("times", 17, "bold"), labelanchor='n', bd=5)
    l_marks.place(x=70, y=240, width=700, height=350)

    self.img = ImageTk.PhotoImage(file="images/result1.jpeg")
    img = Label(self.root2, image=self.img).place(x=785, y=250, width=400, height=340)




