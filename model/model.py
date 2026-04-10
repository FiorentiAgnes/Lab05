from database import corso_DAO
from database.corso_DAO import DAO
from database.studente_DAO import DAOs


class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getStudentiCorso(self, codins):
        studenti = DAOs.getStudentiCorso(codins)
        studenti.sort(key=lambda s: s.cognome)
        return studenti

    def getStudenteMatricola(self, matricola):
        studenti_lista = DAOs.getStudenteMatricola(matricola)
        if len(studenti_lista) > 0:
            return studenti_lista[0]  #restituisco il primo (e unico) studente trovato
        return None

    def getCorsiStudente(self, matricola):
        corsi=DAO.getCorsiStudente(matricola)
        return corsi

    def iscrivi_studente(self, matricola, codins):
        return DAOs.iscrivi_studente(matricola, codins)