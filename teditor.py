from tkinter import *


class Notepad:
    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisScrollBar = Scrollbar(__thisTextArea)

    def __init__(self, **kwargs):
        #text area and scrollbar
        self.__thisWidth = kwargs['width']
        self.__thisHeight = kwargs['height']
        self.__root.title("notepad")
        self.__root.geometry('%dx%d' % (self.__thisWidth, self.__thisHeight))
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thisTextArea.grid(sticky=N + E + S + W)
        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def run(self):
        self.__root.mainloop()


notepad = Notepad(width=600, height=600)
notepad.run()
