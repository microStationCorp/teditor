from tkinter import *


class teditor:

    def __init__(self, root):
        root.title("text editor")


r = Tk()
r.geometry("200x300")
TE = teditor(r)
r.mainloop()
