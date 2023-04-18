import time
import ttkbootstrap as ttk


class Progress(ttk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.title("Chargement")
        self.geometry("521x397")
        self.iconbitmap("images/Logo.ico")
        self.app = app
        self.position_center()

        self.my_fond = ttk.PhotoImage(file="images/Logo_tfe.png")
        self.my_background = ttk.Label(self, image=self.my_fond)
        self.my_background.place(x=0, y=0, relwidth=1, relheight=1)
        self.my_progress = ttk.Progressbar(
            self,
            style="warning-striped",
            maximum=100,
            mode="determinate",
            length=300,
            value=0,
        )
        self.my_progress.pack(pady=190)
        self.progression()

    def progression(self):
        for i in range(100):
            self.my_progress["value"] = i
            time.sleep(0.02)
            self.my_progress.update()
            self.update_idletasks()
        else:
            self.done()


    def done(self):
        self.destroy()
        self.app.deiconify()
