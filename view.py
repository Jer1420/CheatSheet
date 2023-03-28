from tkinter import *

import ttkbootstrap
import ttkbootstrap as ttk
import time


class ProgressBar(ttk.Window):
    def __init__(self):
        super().__init__(themename="solar")
        self.title("Chargement")
        self.geometry("521x397")
        self.iconbitmap("Logo.ico")

        self.my_fond = PhotoImage(file="Logo_tfe.png")
        self.my_background = ttk.Label(self, image=self.my_fond)
        self.my_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.my_progress = ttk.Progressbar(self, style="warning-striped", maximum=100, mode="determinate", length=300, value=0)
        self.my_progress.pack(pady=190)

    def progression(self):
        for i in range(100):
            self.my_progress["value"] = i
            time.sleep(0.02)
            self.my_progress.update()
            self.update_idletasks()
        else:
            self.withdraw()
            sheet_cheat_window = Sheetcheat()

    def start_progress_bar(self):
        self.mainloop()


class Sheetcheat(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("SheetCheat")
        self.iconbitmap("Logo.ico")
        self.geometry("800x400")
        self.qbutt = ttk.Button(self, command=self.exit_program)
        self.qbutt.pack()

    def exit_program(self):
        exit(0)


if __name__ == '__main__':
    app = ProgressBar()
    app.progression()
    app.start_progress_bar()

