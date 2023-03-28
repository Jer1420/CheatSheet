import sqlite3
from contextlib import closing
import ttkbootstrap as ttk


class My_app(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title("Welcome")
        self.geometry("500x350")

        self.data = sqlite3.connect("users.db")  # creation de la base de donnée
        # self.create_table()

        self._log = ttk.StringVar()
        self._pass = ttk.StringVar()

        top_frame = ttk.Frame(self)
        button_frame = ttk.Frame(self)

        # Création des boutons
        bt_login = ttk.Button(button_frame, text="Login", command="", style="info-outline", )
        bt_add = ttk.Button(button_frame, text="Add", command="", style="success-outline", )
        bt_del = ttk.Button(button_frame, text="Delete", command="", style="danger-outline", )
        bt_up = ttk.Button(button_frame, text="Update", command="", style="warning-outline", )

        # Création des entrées
        entry_log = ttk.Entry(top_frame, textvariable=self._log)
        entry_pass = ttk.Entry(top_frame, textvariable=self._pass)

        # Création des labels
        lb_log = ttk.Label(top_frame, text="Login")
        lb_pass = ttk.Label(top_frame, text="Password")

        # Placement des widgets
        top_frame.pack(side=ttk.TOP, expand=True, fill=ttk.BOTH, pady=1)
        lb_log.pack(pady=20)
        entry_log.pack(expand=False, fill=ttk.X, pady=1, padx=20)
        lb_pass.pack(pady=20)
        entry_pass.pack(expand=False, fill=ttk.X, pady=1, padx=20)

        button_frame.pack(expand=True, fill=ttk.X, pady=5, padx=5)
        bt_login.pack(side=ttk.LEFT, expand=True, fill=ttk.X, padx=5, pady=20)
        bt_add.pack(side=ttk.LEFT, expand=True, fill=ttk.X, padx=5)
        bt_del.pack(side=ttk.LEFT, expand=True, fill=ttk.X, padx=5)
        bt_up.pack(side=ttk.LEFT, expand=True, fill=ttk.X, padx=5)

        self.mainloop()



if __name__ == "__main__":
    app = My_app()