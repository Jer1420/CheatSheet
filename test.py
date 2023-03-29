import time
from tkinter import PhotoImage, messagebox
from ttkbootstrap.scrolled import ScrolledText

import ttkbootstrap as ttk
from ttkbootstrap.icons import Emoji


class Test(ttk.Window):
    def __init__(self):
        super().__init__(themename="solar")
        self.withdraw()
        self.title("SheetCheat")
        self.iconbitmap("Logo.ico")
        self.geometry("800x400")
        self.topbar = ttk.Frame(self)
        self.topbar.columnconfigure(4, weight=1)
        self.pack_propagate(False)

        # Creation of the button NEW and insertion of the image in the button
        self.my_new = ttk.PhotoImage(file="images/mail.png")
        self.new = ttk.Button(self.topbar, image=self.my_new)
        self.new.grid(column=0, row=0, pady=5, padx=5, sticky=ttk.W)

        # Creation of the button SAVE and insertion of the image in the button
        self.my_save = ttk.PhotoImage(file="images/map.png")
        self.save = ttk.Button(self.topbar, image=self.my_save)
        self.save.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)

        # Creation of the button SAVE AS and insertion of the image in the button
        self.my_save_as = ttk.PhotoImage(file="images/minus.png")
        self.save_as = ttk.Button(self.topbar, image=self.my_save_as, command="")
        self.save_as.grid(column=2, row=0, pady=5, padx=5, sticky=ttk.W)

        # Creation of the button OPEN and insertion of the image in the button
        self.my_open = ttk.PhotoImage(file="images/plus.png")
        self.open = ttk.Button(self.topbar, image=self.my_open, command="")
        self.open.grid(column=3, row=0, pady=5, padx=5, sticky=ttk.W)

        # Creation of the button AP and insertion of the image in the button
        self.my_ap = ttk.PhotoImage(file="images/map.png")
        self.ap = ttk.Button(self.topbar, image=self.my_ap, command="")
        self.ap.grid(column=4, row=0, pady=5, padx=5, sticky=ttk.E)

        # Creation of the button EXIT and insertion of the image in the button
        self.my_exit = ttk.PhotoImage(file="images/plus.png")
        self.exit = ttk.Button(self.topbar, image=self.my_exit, command=self.exitapp)
        self.exit.grid(column=5, row=0, pady=5, padx=5, sticky=ttk.E)

        self.texte = ScrolledText(self, padding=5, autohide=True, hbar=True)

        self.topbar.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.texte.pack(expand=True, fill=ttk.BOTH)

    def exitapp(self) -> None:
        MsgBox = messagebox.askquestion(
            "Exit", "Voulez vous quitter l'application?", icon="info"
        )
        if MsgBox == "yes":
            messagebox.showinfo("A bientôt", "Merci d'avoir utiliser l'application")
            self.quit()
        else:
            messagebox.showinfo("Good", "Merci " + Emoji.get("winking face").char * 3)


class TopTest(ttk.Toplevel):
    def __init__(self,app):
        super().__init__()
        self.title("Chargement")
        self.geometry("521x397")
        self.iconbitmap("Logo.ico")
        self.app = app

        #self.after(2000,self.done)

        self.my_fond = PhotoImage(file="Logo_tfe.png")
        self.my_background = ttk.Label(self, image=self.my_fond)
        self.my_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.my_progress = ttk.Progressbar(self, style="warning-striped", maximum=100, mode="determinate", length=300, value=0)
        self.my_progress.pack(pady=190)

        self.progression()

    def progression(self):
        for i in range(100):
            self.my_progress["value"] = i
            time.sleep(0.02)
            self.my_progress.update()
            self.update_idletasks()
        else:
            #self.withdraw()
            #sheet_cheat_window = Sheetcheat()
            self.app.deiconify()
            self.destroy()
            #sheet_cheat_window.mainloop()

    def done(self):
        self.destroy()
        self.app.deiconify()


if __name__ == '__main__':
    test = Test()
    toptest = TopTest(test)
    toptest.mainloop()