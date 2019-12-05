from tkinter.filedialog import *


class Notepad:
    __root = Tk()

    __thisWidth = 600
    __thisHeight = 600
    __thisTextArea = Text(__root)
    __thisControlArea = Frame(__root)
    __thisButton = Button(__thisControlArea, text="click")

    def __init__(self):
        self.__root.title("Notepad")
        self.__root.geometry("%dx%d" % (self.__thisWidth,
                                        self.__thisHeight))
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thisTextArea.grid(sticky=N + E + S + W, row=0,
                                 column=0)
        self.__thisControlArea.grid(row=1, column=0)
        self.__thisButton.pack()

    def run(self):
        self.__root.mainloop()


notepad = Notepad()
notepad.run()
