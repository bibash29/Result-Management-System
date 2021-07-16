from tkinter import *
from modu import top_canvas
import os


class Faculties:
    def BSc_CSIT(self):
        # self.root.destroy()
        os.system('python bsc_csit.py')

    def BASW(self):
        os.system('python basw.py')

    def BPSG(self):
        os.system('python bpsg.py')

    def BBM(self):
        os.system('python bbm.py')

    def BBS(self):
        os.system('python bbs.py')

    def BCA(self):
        os.system('python bca.py')

    def __init__(self, root1):
        self.root = root1
        self.root.title("Faculties Selection Window")
        self.root.geometry("1520x775+1+5")
        self.root.attributes("-toolwindow", 1)

        # self.root.config(bg="blue")

        # ==== Top canvas part ====
        top_canvas(self)

        # ==== Left canvas part ====
        canvas1 = Canvas(self.root, width=390, bd=2, height=667, bg="#5900a6")
        canvas1.place(x=0, y=97)

        text = Label(canvas1, text="Faculty selection section", font=("times", 25, "bold"), bg="#5900a6", fg="white")
        text.place(x=20, y=20)

        text = Label(canvas1, text="Select the faculty below:", font=("times", 16), bg="#5900a6", fg="white")
        text.place(x=90, y=100)

        # ==== Faculties Buttons =====
        faculty1 = Button(canvas1, text="BSc.CSIT", command=self.BSc_CSIT, font=("times", 15, "bold"), fg="black", bd=2, cursor="hand2")
        faculty1.place(x=145, y=150, width=100)

        faculty2 = Button(canvas1, text="BASW", command=self.BASW, font=("times", 15, "bold"), fg="black", bd=2, cursor="hand2")
        faculty2.place(x=145, y=220, width=100)

        faculty3 = Button(canvas1, text="BPSG", command=self.BPSG, font=("times", 15, "bold"), fg="black", bd=2, cursor="hand2")
        faculty3.place(x=145, y=290, width=100)

        faculty4 = Button(canvas1, text="BBM", command=self.BBM, font=("times", 15, "bold"), fg="black", bd=2, cursor="hand2")
        faculty4.place(x=145, y=360, width=100)

        faculty5 = Button(canvas1, text="BBS", command=self.BBS, font=("times", 15, "bold"), fg="black", bd=2, cursor="hand2")
        faculty5.place(x=145, y=430, width=100)

        faculty6 = Button(canvas1, text="BCA", command=self.BCA, font=("times", 15, "bold"), fg="black", bd=2, cursor="hand2")
        faculty6.place(x=145, y=500, width=100)


if __name__ == "__main__":  # to deal with multiple file
    root = Tk()
    obj = Faculties(root)
    root.mainloop()
