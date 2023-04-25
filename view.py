from ttkbootstrap.scrolled import ScrolledText
from tkinter import *
import ttkbootstrap as ttk
from controller import Commandes, CommandeModel
from exit import Exit
from info import About
from edit import Edit
from progress import Progress
from select_com import Select_com
from entry_word import Word



class Main_Window(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.withdraw()
        self.title("CheatSheet")
        self.iconbitmap("images/Logo.ico")
        self.geometry("1000x600")

        # Create frames
        self.topbar = ttk.Frame(self)
        self.topbar.columnconfigure(4, weight=1)
        self.pack_propagate(False)
        self.rech = ttk.Frame(self)
        self.listb = ttk.Frame(self)

        # Create frames
        self._recherche = ttk.StringVar()
        self.recherche = ttk.Entry(
            self.rech, textvariable=self._recherche, width=70, style="dark"
        )
        self.recherche.grid(column=0, row=0, pady=5, padx=5, sticky=ttk.W)

        # Create button about
        self.new = ttk.Button(
            self.topbar,
            command=About,
            text="A propos",
            style="warning-outline",
            width=20,
        )
        self.new.grid(column=3, row=0, pady=5, padx=5, sticky=ttk.W)

        # Create button editing
        self.edit = ttk.Button(
            self.topbar,
            command=self.show_editions,
            text="Edition",
            style="warning-outline",
            width=20,
        )
        self.edit.grid(column=0, row=0, pady=5, padx=5, sticky=ttk.W)

        # Create button modified
        self.new = ttk.Button(
            self.topbar,
            command=self.show_modif,
            text="Modifier",
            style="warning-outline",
            width=20,
        )
        self.new.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.W)

        # Create button delete
        self.new = ttk.Button(
            self.topbar,
            command=self.delete,
            text="Supprimer",
            style="warning-outline",
            width=20,
        )
        self.new.grid(column=2, row=0, pady=5, padx=5, sticky=ttk.W)

        # Create button research
        self.rechercher = ttk.Button(
            self.rech,
            command=self.search,
            text="Rechercher",
            style="warning-outline",
            width=17,
        )
        self.rechercher.grid(column=2, row=0, pady=5, padx=5, sticky=ttk.E)

        # Create button exit
        self.exit = ttk.Button(
            self.topbar,
            command=Exit,
            text="Quitter",
            style="danger-outline",
            width=17,
        )
        self.exit.grid(column=5, row=0, pady=5, padx=5, sticky=ttk.E)

        # Create combobox Windows & Linux
        self.os_type = ttk.StringVar()
        self.cb = ttk.Combobox(
            self.rech,
            values=["Windows", "Linux"],
            state=ttk.READONLY,
            textvariable=self.os_type,
            style="dark.TCombobox",
        )
        self.cb.current(0)
        self.cb.bind("<<ComboboxSelected>>", self.construct_list_command)
        self.cb.grid(column=1, row=0, pady=5, padx=5, sticky=ttk.E)

        # Create list box
        self.listb.rowconfigure(1, weight=1)
        scrollbar = ttk.Scrollbar(self.listb)
        scrollbar.grid(column=2, row=1, sticky=ttk.NS)

        self.mylist = Listbox(self.listb, yscrollcommand=scrollbar.set)
        self.mylist.bind("<Double-1>", self.show_details_command)

        self.mylist.grid(column=1, row=1, sticky=ttk.NS)
        scrollbar.config(command=self.mylist.yview)

        lb_command = ttk.Label(self.listb, text="Liste des commandes", style="warning")
        lb_command.grid(columnspan=2, row=0, sticky=ttk.EW, pady=10, padx=10)

        # Create ScrolledText
        self.texte = ScrolledText(
            self, padding=5, autohide=True, hbar=False, wrap=ttk.WORD
        )
        self.texte.text.bind(
            "<Key>", lambda e: "break"
        )  # Permet de bloquer l'écriture dans le ScrolledText
        # Place Frame
        self.topbar.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.rech.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        self.listb.pack(expand=False, fill=ttk.Y, side=ttk.RIGHT, anchor=ttk.N)
        self.texte.pack(expand=True, fill=ttk.BOTH)

    def search(self):
        if str(self._recherche.get()) != "":
            self.mylist.delete(0, END)
            all_commande_name_search = controller.search(
                str(self._recherche.get()), str(self.os_type.get())
            )
            for command_name in all_commande_name_search:
                self.mylist.insert(END, command_name[0])
        else:
            wrd = Word()

    def get_list(self):
        list_commande = controller.get_name_command(str(self.os_type.get()))
        new_list_commands = []
        for command in list_commande:
            new_list_commands.append(command[0])
        return new_list_commands

    def delete(self):
        try:
            command_selected_index = self.mylist.curselection()
            command_selected_name = self.mylist.get(command_selected_index[0])
            all_command = controller.get_detail_command(
                self.os_type.get(), command_selected_name
            )
            for command in all_command:
                controller.delete(command.id_commandes)
            self.construct_list_command()
        except IndexError:
            sel_com = Select_com()

    def show_details_command(self, event):
        self.texte.delete("1.0", END)
        command_selected_index = self.mylist.curselection()
        command_selected_name = self.mylist.get(command_selected_index[0])
        all_commands_details: list[CommandeModel] = controller.get_detail_command(
            self.os_type.get(), command_selected_name
        )
        for command in all_commands_details:
            self.texte.insert(ttk.INSERT, f"Nom :\n{command.nom_commandes}\n\n")
            self.texte.insert(ttk.INSERT, f"Syntaxe :\n{command.syntaxe_commandes}\n\n")
            self.texte.insert(ttk.INSERT, f"Synopsys :\n{command.synopsys_commandes}\n")
            self.texte.insert(
                ttk.INSERT, f"Paramètres :\n{command.parametre_commandes}\n"
            )
            self.texte.insert(ttk.INSERT, f"Exemples :\n{command.exemple_commandes}\n")

    def construct_list_command(self, event=None):
        self.mylist.delete(0, END)
        for command in self.get_list():
            self.mylist.insert(END, command)

    def show_editions(self):
        edit = Edit(parent=self)
        edit.controller = self.controller

    def show_modif(self):
        command_selected_index = self.mylist.curselection()
        try:
            command_selected_name = self.mylist.get(command_selected_index[0])
            all_commands_details: list[CommandeModel] = controller.get_detail_command(
                self.os_type.get(), command_selected_name
            )
            edit = Edit(parent=self, command_to_modif=all_commands_details[0])
            edit.controller = self.controller
        except IndexError:
            sel = Select_com()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, value):
        self._controller = value


if __name__ == "__main__":
    app = Main_Window()
    controller = Commandes()
    app.controller = controller
    app.construct_list_command()
    progression = Progress(app)
    progression.mainloop()
