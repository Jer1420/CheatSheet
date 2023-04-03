import time
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
            command=self.editeur,
            text="A propos",
            style="info-outline",
            width=20,
        )
        self.new.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)

        # Création du bouton Edition
        self.edit = ttk.Button(
            self.topbar, command=Editions, text="Edition", style="success-outline", width=20
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
            command=self.exitapp,
            text="Exit",
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

        lb_command = ttk.Label(self.listb, text="Liste des commandes", style="primary")
        lb_command.grid(columnspan=2, row=0, sticky=ttk.EW, pady=10, padx=10)

        # Création de la ScrolledText
        self.texte = ScrolledText(self, padding=5, autohide=True, hbar=True)

        # Placement des Frame
        self.topbar.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.rech.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.listb.pack(expand=False, fill=ttk.Y, side=ttk.RIGHT, anchor=ttk.N)
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

    @staticmethod
    def editeur():
        messagebox.showinfo(
            "Editeur du programme", "Créer par Jeremy\rhttps://github.com/Jer1420"
        )

class Editions(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Edition")
        self.iconbitmap("Logo.ico")
        self.geometry("1000x600")

        self._nom = ttk.StringVar() #entry
        self._synopsis = ttk.StringVar() #texte
        self._syntaxe = ttk.StringVar() #entry
        self._parametre = ttk.StringVar() #texte
        self._exemple = ttk.StringVar() #texte

        self.noms = ttk.Frame(self)
        self.syno = ttk.Frame(self)
        self.syn = ttk.Frame(self)
        self.para = ttk.Frame(self)
        self.ex = ttk.Frame(self)
        self.bouton = ttk.Frame(self)

        lb_nom = ttk.Label(self.noms, text="Nom :", style="primary")
        lb_syno = ttk.Label(self.syno, text="Synopsis :", style="primary")
        lb_syn = ttk.Label(self.syn, text="Syntaxe :", style="primary")
        lb_para = ttk.Label(self.para, text="Paramètres :", style="primary")
        lb_ex = ttk.Label(self.ex, text="Exemples :", style="primary")

        lb_nom.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_syno.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_syn.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_para.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)
        lb_ex.grid(column=0, row=0, sticky=ttk.EW, pady=10, padx=10)

        self.nom = ttk.Entry(self.noms, textvariable=self._nom, width=70, style="dark")
        self.texte_syno = ScrolledText(self.syno, padding=5, autohide=True, hbar=False, textvariable=self._synopsis)
        self.synta = ttk.Entry(self.syn, textvariable=self._syntaxe, width=70, style="dark")
        #self.texte_param = ScrolledText(self.para, padding=5, autohide=True, hbar=False)
        #self.texte_exemple = ScrolledText(self.ex, padding=5, autohide=True, hbar=False)

        self.nom.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)
        #self.texte_syno.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)
        self.synta.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)
        #self.para.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)
        #self.ex.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)

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
        self.annuler.grid(column=0, row=0, pady=5, padx=5, sticky=ttk.W)

        # Création du bouton Sauvegarder
        self.save = ttk.Button(
            self.bouton,
            command="",
            text="Sauvegarder",
            style="success-outline",
            width=20
        )
        self.save.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)



class Progress(ttk.Toplevel):
    def __init__(self, app):
        super().__init__()
        self.title("Chargement")
        self.geometry("521x397")
        self.iconbitmap("Logo.ico")
        self.app = app

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
