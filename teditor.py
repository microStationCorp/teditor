from tkinter import *


class Notepad:
    __root = Tk()

    # default window width and height
    __thisWidth = 600
    __thisHeight = 600
    __thisTextArea = Text(__root)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    def __init__(self):
        # text area and scrollbar
        self.__root.title("Notepad")
        self.__root.geometry('%dx%d' % (self.__thisWidth, self.__thisHeight))
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thisTextArea.grid(sticky=N + E + S + W)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        # menu add
        self.__root.config(menu=self.__thisMenuBar)

        # file Menu Add
        self.__thisFileMenu.add_command(label="New")
        self.__thisFileMenu.add_command(label="Open")
        self.__thisFileMenu.add_command(label="Save")
        self.__thisFileMenu.add_command(label="Exit")
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        # Edit Menu Add
        self.__thisEditMenu.add_command(label="Cut")
        self.__thisEditMenu.add_command(label="Copy")
        self.__thisEditMenu.add_command(label="Paste")
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        # help menu
        self.__thisHelpMenu.add_command(label="about")
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

    def run(self):
        self.__root.mainloop()


notepad = Notepad()
notepad.run()
