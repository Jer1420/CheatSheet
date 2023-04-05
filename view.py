import sys
import time
import webbrowser
from tkinter import PhotoImage, messagebox
from ttkbootstrap.scrolled import ScrolledText
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.icons import Emoji


class Menu_principal(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.withdraw()
        self.title("SheetCheat")
        self.iconbitmap("Logo.ico")
        self.geometry("1000x600")

        # Création des Frame
        self.topbar = ttk.Frame(self)
        self.topbar.columnconfigure(4, weight=1)
        self.pack_propagate(False)
        self.rech = ttk.Frame(self)
        self.listb = ttk.Frame(self)

        # Création de l'Entry
        self._recherche = ttk.StringVar()
        self.recherche = ttk.Entry(
            self.rech, textvariable=self._recherche, width=70, style="dark"
        )
        self.recherche.grid(column=0, row=0, pady=5, padx=5, sticky=ttk.W)

        # Création du bouton À propos
        self.new = ttk.Button(
            self.topbar,
            command=Apropos,
            text="A propos",
            style="warning-outline",
            width=20,
        )
        self.new.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)

        # Création du bouton Edition
        self.edit = ttk.Button(
            self.topbar, command=Editions, text="Edition", style="warning-outline", width=20
        )
        self.edit.grid(column=0, row=0, pady=5, padx=5, sticky=ttk.W)

        # Création du bouton Rechercher
        self.rechercher = ttk.Button(
            self.rech, command="", text="Rechercher", style="warning-outline", width=17
        )
        self.rechercher.grid(column=2, row=0, pady=5, padx=5, sticky=ttk.E)

        # Création du bouton Exit
        self.exit = ttk.Button(
            self.topbar,
            command=Exit,
            text="Quitter",
            style="danger-outline",
            width=17,
        )
        self.exit.grid(column=5, row=0, pady=5, padx=5, sticky=ttk.E)

        # Création la combobox Windows & Linux
        self.os_type = ttk.StringVar()
        self.cb = ttk.Combobox(
            self.rech,
            values=["Windows", "Linux"],
            state=ttk.READONLY,
            textvariable=self.os_type,
            style="dark",
        )
        self.cb.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.E)

        # Creation de la list box
        self.listb.rowconfigure(1, weight=1)
        scrollbar = Scrollbar(self.listb)
        scrollbar.grid(column=2, row=1, sticky=ttk.NS)

        mylist = Listbox(self.listb, yscrollcommand=scrollbar.set)
        for line in range(100):
            mylist.insert(END, "This is line number " + str(line))

        mylist.grid(column=1, row=1, sticky=ttk.NS)
        scrollbar.config(command=mylist.yview)

        lb_command = ttk.Label(self.listb, text="Liste des commandes", style="warning")
        lb_command.grid(columnspan=2, row=0, sticky=ttk.EW, pady=10, padx=10)

        # Création de la ScrolledText
        self.texte = ScrolledText(self, padding=5, autohide=True, hbar=True)

        # Placement des Frame
        self.topbar.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.rech.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.listb.pack(expand=False, fill=ttk.Y, side=ttk.RIGHT, anchor=ttk.N)
        self.texte.pack(expand=True, fill=ttk.BOTH)

class Exit(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("")
        self.iconbitmap("Logo.ico")
        self.geometry("260x125")
        self.lb1 = ttk.Frame(self)
        self.bouton = ttk.Frame(self)

        # Création du bouton Ok
        self.oui = ttk.Button(
            self.bouton,
            command=self.sortir,
            text="Oui",
            style="warning-outline",
            width=10
        )

        self.non = ttk.Button(
            self.bouton,
            command=self.destroy,
            text="Non",
            style="warning-outline",
            width=10
        )

        lb_pseudo = ttk.Label(self.lb1, text="Voulez vous quitter l'application ?".center(33," "), style="warning")
        lb_pseudo.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.lb1.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        self.oui.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.non.grid(column=1, row=0, sticky=ttk.N, pady=10, padx=10)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)


    def sortir(self):
        sys.exit(0)

class Apropos(ttk.Toplevel):
    def __init__(self):
        super().__init__(resizable=(False,False))
        self.title("")
        self.iconbitmap("Logo.ico")
        self.geometry("220x155")
        self.lb1 = ttk.Frame(self)
        self.lb2 = ttk.Frame(self)
        self.bouton = ttk.Frame(self)

        # Création du bouton Ok
        self.ok = ttk.Button(
            self.bouton,
            command=self.destroy,
            text="Ok",
            style="warning-outline",
            width=10
        )

        lb_pseudo = ttk.Label(self.lb1, text="Créé par Jeremy".center(33," "), style="warning")
        lb_pseudo.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.lb1.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        lb_pseudo = ttk.Label(self.lb2, text="https://github.com/Jer1420".center(10," "), style="warning")
        lb_pseudo.bind("<Button-1>",self.do_open_url)
        lb_pseudo.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.lb2.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        self.ok.grid(column=1, row=0, sticky=ttk.N, pady=10, padx=10)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        lb_vide = ttk.Label(self.bouton, text="      ")
        lb_vide.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.position_center()

    def do_open_url(self,event):
        webbrowser.open("https://github.com/Jer1420")


class Editions(ttk.Toplevel):
    def __init__(self):
        super().__init__(resizable=(False,False))
        self.title("Edition")
        self.iconbitmap("Logo.ico")
        self.geometry("1250x830")


        self._nom = ttk.StringVar()
        self._syntaxe = ttk.StringVar()

        self.noms = ttk.Frame(self)
        self.syno = ttk.Frame(self)
        self.syn = ttk.Frame(self)
        self.para = ttk.Frame(self)
        self.ex = ttk.Frame(self)
        self.bouton = ttk.Frame(self)

        lb_nom = ttk.Label(self.noms, text= "Nom :        ", style="warning")
        lb_syno = ttk.Label(self.syno, text="Synopsis :   ", style="warning")
        lb_syn = ttk.Label(self.syn, text=  "Syntaxe :    ", style="warning")
        lb_para = ttk.Label(self.para, text="Paramètres :", style="warning")
        lb_ex = ttk.Label(self.ex, text=    "Exemples :  ", style="warning")
        lb_invisible = ttk.Label(self.bouton, text="")

        lb_nom.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_syno.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_syn.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_para.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_ex.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_invisible.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)

        self.nom = ttk.Entry(self.noms, textvariable=self._nom, width=115, style="dark")
        self.synta = ttk.Entry(self.syn, textvariable=self._syntaxe, width=141, style="dark")

        self.nom.columnconfigure(1, weight=1)
        self.syno.columnconfigure(1,weight=1)
        self.synta.columnconfigure(1,weight=1)
        self.para.columnconfigure(1,weight=1)
        self.ex.columnconfigure(1,weight=1)

        self.txt_synopsis = Text(self.syno)
        self.txt_synopsis.config(height=10)
        self.txt_synopsis.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.NSEW)

        self.txt_parametre = Text(self.para)
        self.txt_parametre.config(height=10)
        self.txt_parametre.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.NSEW)

        self.txt_exemples = Text(self.ex)
        self.txt_exemples.config(height=10)
        self.txt_exemples.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.NSEW)


        self.nom.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)
        self.synta.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)

        self.noms.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.syno.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.syn.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.para.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.ex.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        # Création la combobox Windows & Linux
        self.os_type = ttk.StringVar()
        self.cb = ttk.Combobox(
            self.noms,
            values=["Windows", "Linux"],
            state=ttk.READONLY,
            textvariable=self.os_type,
            style="dark",
        )
        self.cb.grid(column=2, row=0, pady=5, padx=5, sticky=ttk.E)

        # Création du bouton Annuler
        self.annuler = ttk.Button(
            self.bouton,
            command=self.destroy,
            text="Annuler",
            style="danger-outline",
            width=20
        )
        self.annuler.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.E)

        # Création du bouton Sauvegarder
        self.save = ttk.Button(
            self.bouton,
            command="",
            text="Sauvegarder",
            style="warning-outline",
            width=20
        )
        self.save.grid(column=2, row=0, pady=10, padx=5, sticky=ttk.E)

        self.position_center()



class Progress(ttk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.title("Chargement")
        self.geometry("521x397")
        self.iconbitmap("Logo.ico")
        self.app = app
        self.position_center()

        self.my_fond = PhotoImage(file="Logo_tfe.png")
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
            self.app.deiconify()
            self.destroy()

    def done(self):
        self.destroy()
        self.app.deiconify()



if __name__ == "__main__":
    test = Menu_principal()
    progression = Progress(test)
    progression.mainloop()
