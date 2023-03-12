from tkinter import *

import ttkbootstrap
import ttkbootstrap as tb
import time


class ProgressBar(tb.Window):
    def __init__(self):
        super().__init__()
        self.title("Chargement")
        self.geometry("500x250")
        self.iconbitmap("Logo.ico")
        self.my_fond = PhotoImage(file="Logo_tfe.png")
        self.my_background = tb.Label(self, image=self.my_fond)
        self.my_background.place(x=0, y=0, relwidth=1, relheight=1)

    def start_progress_bar(self):
        self.mainloop()

if __name__ == '__main__':
    app = ProgressBar()

    app.start_progress_bar()