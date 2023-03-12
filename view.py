from tkinter import *

import ttkbootstrap
import ttkbootstrap as tb
import time


class ProgressBar(tb.Window):
    def __init__(self):
        super().__init__(themename="solar")
        self.title("Chargement")
        self.geometry("521x397")
        self.iconbitmap("Logo.ico")

        self.my_fond = PhotoImage(file="Logo_tfe.png")
        self.my_background = tb.Label(self, image=self.my_fond)
        self.my_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.my_progress = tb.Progressbar(self, style="warning-striped", maximum=100, mode="determinate", length=300, value=0)
        self.my_progress.pack(pady=190)

    def progression(self):
        for i in range(100):
            self.my_progress["value"] = i
            time.sleep(0.02)
            self.my_progress.update()
            self.update_idletasks()
        else:
            self.destroy()
            window_app = Sheetcheat()
            window_app.start_sheetcheat()
            exit(0)

    def start_progress_bar(self):
        self.mainloop()

class Sheetcheat(tb.Window):
    def __init__(self):
        super().__init__()
        self.title("SheetCheat")
        self.iconbitmap("Logo.ico")
        self.geometry("800x400")

    def start_sheetcheat(self):
        self.mainloop()

if __name__ == '__main__':
    app = ProgressBar()
    app.progression()
    app.start_progress_bar()

