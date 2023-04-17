import ttkbootstrap as ttk


class Edit(ttk.Toplevel):
    def __init__(self):
        super().__init__(resizable=(False, False))
        self.title("Edition")
        self.iconbitmap("images/Logo.ico")
        self.geometry("1250x830")

        self._nom = ttk.StringVar()
        self._syntaxe = ttk.StringVar()

        # Create frame
        self.noms = ttk.Frame(self)
        self.syno = ttk.Frame(self)
        self.syn = ttk.Frame(self)
        self.para = ttk.Frame(self)
        self.ex = ttk.Frame(self)
        self.bouton = ttk.Frame(self)

        # Create label
        lb_nom = ttk.Label(self.noms, text="Nom :        ", style="warning")
        lb_syno = ttk.Label(self.syno, text="Synopsis :   ", style="warning")
        lb_syn = ttk.Label(self.syn, text="Syntaxe :    ", style="warning")
        lb_para = ttk.Label(self.para, text="Paramètres :", style="warning")
        lb_ex = ttk.Label(self.ex, text="Exemples :  ", style="warning")
        lb_invisible = ttk.Label(self.bouton, text="")

        # Place label
        lb_nom.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_syno.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_syn.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_para.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_ex.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_invisible.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)

        # Create entry
        self.nom = ttk.Entry(self.noms, textvariable=self._nom, width=115, style="dark")
        self.synta = ttk.Entry(
            self.syn, textvariable=self._syntaxe, width=141, style="dark"
        )

        self.nom.columnconfigure(1, weight=1)
        self.syno.columnconfigure(1, weight=1)
        self.synta.columnconfigure(1, weight=1)
        self.para.columnconfigure(1, weight=1)
        self.ex.columnconfigure(1, weight=1)

        # Configure text
        self.txt_synopsis = ttk.Text(self.syno)
        self.txt_synopsis.config(height=10)
        self.txt_synopsis.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.NSEW)

        # Configure text
        self.txt_parametre = ttk.Text(self.para)
        self.txt_parametre.config(height=10)
        self.txt_parametre.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.NSEW)

        # Configure text
        self.txt_exemples = ttk.Text(self.ex)
        self.txt_exemples.config(height=10)
        self.txt_exemples.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.NSEW)

        # Configure grid
        self.nom.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)
        self.synta.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)

        # Configure pack
        self.noms.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.syno.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.syn.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.para.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.ex.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        # Create combobox Windows & Linux
        self.os_type = ttk.StringVar()
        self.cb = ttk.Combobox(
            self.noms,
            values=["Windows", "Linux"],
            state=ttk.READONLY,
            textvariable=self.os_type,
            style="dark",
        )
        self.cb.grid(column=2, row=0, pady=5, padx=5, sticky=ttk.E)

        # Create button close
        self.annuler = ttk.Button(
            self.bouton,
            command=self.destroy,
            text="Fermer",
            style="danger-outline",
            width=20,
        )
        self.annuler.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.E)

        # Create button save
        self.save = ttk.Button(
            self.bouton,
            command=self.do_add,
            text="Sauvegarder",
            style="warning-outline",
            width=20,
        )
        self.save.grid(column=2, row=0, pady=10, padx=5, sticky=ttk.E)

        self.position_center()

    # Reset of inputs
    def reset(self):
        self.os_type.set("")
        self._nom.set("")
        self.txt_synopsis.delete("1.0", ttk.END)
        self._syntaxe.set("")
        self.txt_parametre.delete("1.0", ttk.END)
        self.txt_exemples.delete("1.0", ttk.END)

    # Add in DB
    def do_add(self):
        os: str = self.os_type.get()
        name: str = self._nom.get()
        synopsis: str = self.txt_synopsis.get("1.0", ttk.END)
        syntax: str = self._syntaxe.get()
        param: str = self.txt_parametre.get("1.0", ttk.END)
        exemple: str = self.txt_exemples.get("1.0", ttk.END)

        self.controller.add(os, name, synopsis, syntax, param, exemple)
        self.reset()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, value):
        self._controller = value
