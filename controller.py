import dataclasses
from dataclasses import dataclass, field
import sqlite3
from contextlib import closing


@dataclasses.dataclass
class CommandeModel:
    os_commandes: str
    nom_commandes: str
    synopsys_commandes: str
    syntaxe_commandes: str
    parametre_commandes: str
    exemple_commandes: str
    id_commandes: int = field(default=-1)


class Commandes:
    def __init__(self):
        self.data = sqlite3.connect("data.db")  # creation de la base de donnée
        self.create_table()

    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.data.cursor()

    # def commit(self):
    # self.database.commit()

    def create_table(self):
        sql = """ CREATE TABLE IF NOT EXISTS T_Commandes (
            id_commandes INTEGER PRIMARY KEY AUTOINCREMENT,
            os_commandes TEXT NOT NULL ,
            nom_commandes TEXT NOT NULL,
            synopsys_commandes TEXTE NOT NULL,
            syntaxe_commandes TEXT NOT NULL ,
            parametre_commandes TEXT NOT NULL ,
		    exemple_commandes TEXT NOT NULL 
            ) """

        with closing(self.cursor) as cursor:
            cursor.execute(sql)
            self.data.commit()

    def add(
        self,
        os_commandes: str,
        nom_commandes: str,
        synopsys_commandes: str,
        syntaxe_commandes: str,
        parametre_commandes: str,
        exemple_commandes: str,
    ):
        sql = """INSERT INTO T_commandes
        (os_commandes, nom_commandes, synopsys_commandes, syntaxe_commandes, parametre_commandes, exemple_commandes)
        VALUES(?, ?, ?, ?, ?, ? );
        """
        with closing(self.cursor) as cursor:
            cursor.execute(
                sql,
                [
                    os_commandes,
                    nom_commandes,
                    synopsys_commandes,
                    syntaxe_commandes,
                    parametre_commandes,
                    exemple_commandes,
                ],
            )
            self.data.commit()

    def get_name_command(self, os: str):
        sql = """SELECT nom_commandes from T_commandes where os_commandes = ?"""
        with closing(self.cursor) as cursor:
            result = cursor.execute(
                sql,
                [
                    os,
                ],
            )
            return result.fetchall()

    def get_detail_command(self, os: str, command_name: str):
        sql = """SELECT * from T_commandes where os_commandes = ? and (nom_commandes = ?)"""
        with closing(self.cursor) as cursor:
            result = cursor.execute(sql, [os, command_name])
            result.row_factory = lambda cursor, row: CommandeModel(
                id_commandes=row[0],
                os_commandes=row[1],
                nom_commandes=row[2],
                synopsys_commandes=row[3],
                syntaxe_commandes=row[4],
                parametre_commandes=row[5],
                exemple_commandes=row[6],
            )
            return result.fetchall()

    def delete(self, id_command: int):
        sql = """DELETE FROM T_Commandes WHERE id_commandes = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql, [id_command])
            self.data.commit()

    def search(self, search: str, os: str):
        search = f"%{search}%"
        sql = """SELECT nom_commandes FROM T_Commandes WHERE (os_commandes = ?) AND (nom_commandes LIKE ?) OR (synopsys_commandes LIKE ?)"""
        with closing(self.cursor) as cursor:
            sql_result = cursor.execute(sql, [os, search, search])
            return sql_result.fetchall()

    def modified(self,
        os_commandes: str,
        nom_commandes: str,
        synopsys_commandes: str,
        syntaxe_commandes: str,
        parametre_commandes: str,
        exemple_commandes: str,
        id_commandes: int):
        sql = """UPDATE T_Commandes SET os_commandes = ?, 
        nom_commandes = ?, 
        synopsys_commandes = ?, 
        syntaxe_commandes = ?, parametre_commandes = ?, exemple_commandes = ? WHERE id_commandes = ?"""
        with closing(self.cursor) as cursor:
            cursor.execute(sql, [
                os_commandes,
                nom_commandes,
                synopsys_commandes,
                syntaxe_commandes,
                parametre_commandes,
                exemple_commandes,
                id_commandes
            ])
            self.data.commit()