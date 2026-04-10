# Add whatever it is needed to interface with the DB Table studente
import mysql

from database.DB_connect import DBConnect
from model.studente import Studente


class DAOs():
    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT s.*
                        FROM studente s, iscrizione i 
                        WHERE s.matricola = i.matricola 
                        and i.codins = %s"""

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudenteMatricola(matricola):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT *
                        FROM studente s
                        WHERE s.matricola = %s"""

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def iscrivi_studente(matricola, codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()

        query = """INSERT INTO iscrizione (matricola, codins) 
                   VALUES (%s, %s)"""

        try:
            cursor.execute(query, (matricola, codins))
            cnx.commit()  #conferma l'inserimento nel DB
            success = True
        except mysql.connector.Error as err:
            print(f"Errore: {err}")
            success = False

        cursor.close()
        cnx.close()
        return success