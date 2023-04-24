import ttkbootstrap as ttk


class Save(ttk.Toplevel):
    def __init__(self):
        super().__init__(resizable=(False, False))
        self.title("")
        self.iconbitmap("images/Logo.ico")
        self.geometry("245x120")
        self.lb1 = ttk.Frame(self)
        self.bouton = ttk.Frame(self)

        # Create button ok
        self.ok = ttk.Button(
            self.bouton,
            command=self.destroy,
            text="Ok",
            style="warning-outline",
            width=10,
        )

        lb_pseudo = ttk.Label(
            self.lb1,
            text="La commande est sauvegardée".center(33, " "),
            style="warning",
        )
        lb_pseudo.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.lb1.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        self.ok.grid(column=1, row=0, sticky=ttk.N, pady=10, padx=10)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        lb_vide = ttk.Label(self.bouton, text="          ")
        lb_vide.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)

        self.position_center()
