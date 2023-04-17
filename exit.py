import ttkbootstrap as ttk
from ttkbootstrap import Toplevel
import sys


class Exit(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("")
        self.iconbitmap("images/Logo.ico")
        self.geometry("260x125")
        self.lb1 = ttk.Frame(self)
        self.bouton = ttk.Frame(self)

        # Create button yes
        self.oui = ttk.Button(
            self.bouton,
            command=self.sortir,
            text="Oui",
            style="warning-outline",
            width=10,
        )

        # Create button no
        self.non = ttk.Button(
            self.bouton,
            command=self.destroy,
            text="Non",
            style="warning-outline",
            width=10,
        )

        lb_pseudo = ttk.Label(
            self.lb1,
            text="Voulez vous quitter l'application ?".center(33, " "),
            style="warning",
        )
        lb_pseudo.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.lb1.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        self.oui.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.non.grid(column=1, row=0, sticky=ttk.N, pady=10, padx=10)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

    def sortir(self):
        sys.exit(0)
