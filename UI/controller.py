import flet as ft

from model import corso


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI

        self._ddCodinsValue = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_cerca_iscritti(self, e):
        codice_corso=self._view.dd_sel_corso.value
        self._view.txt_result.controls.clear()

        if codice_corso is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return

        # recupero gli studenti
        studenti = self._model.getStudentiCorso(codice_corso)

        if not studenti:
            self._view.txt_result.controls.append(
                ft.Text("Nessuno studente iscritto a questo corso."))
        else:
            self._view.txt_result.controls.append(
                ft.Text(f"Ci sono {len(studenti)} iscritti al corso:"))
            for s in studenti:
                self._view.txt_result.controls.append(ft.Text(s))
        self._view.update_page()

    def handle_cerca_studente(self, e):
        matricola=self._view.txt_matricola.value
        if not matricola:
            self._view.create_alert("Per favore inserisci una matricola valida.")
            return

        studente=self._model.getStudenteMatricola(matricola)
        if studente is None:
            self._view.create_alert("Matricola non trovata nel database.")
            self._view.txt_nome.value = ""
            self._view.txt_cognome.value = ""
            self._view.update_page()
            return
        self._view.txt_nome.value = studente.nome
        self._view.txt_cognome.value = studente.cognome

        self._view.update_page()



    def handle_cerca_corsi(self, e):
        matricola = self._view.txt_matricola.value
        if not matricola:
            self._view.create_alert("Per favore inserisci una matricola valida.")
            return
        corsi=self._model.getCorsiStudente(matricola)
        if corsi is None:
            self._view.txt_result.controls.append(ft.Text("Questo studente non frequenta nessun corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Risultano{len(corsi)}corsi:"))
            for c in corsi:
                self._view.txt_result.controls.append(ft.Text(c))
        self._view.update_page()

    def handle_iscrivi(self, e):
        codins=self._view.dd_sel_corso.value
        matricola = self._view.txt_matricola.value
        if codins is None or codins == "":
            self._view.create_alert("Seleziona un corso prima di procedere.")
            return
        if not matricola:
            self._view.create_alert("Inserisci la matricola dello studente.")
            return
        risultato = self._model.iscrivi_studente(matricola, codins)
        if risultato:
            self._view.create_alert("Studente iscritto con successo!")
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Iscrizione completata."))
        else:
            self._view.create_alert("Errore nell'iscrizione. Lo studente potrebbe essere già iscritto.")

        self._view.update_page()


    def filldd_sel_corso(self):
        # for cod in self._model.getCodins():
        #     self._view.ddCodins.options.append(
        #         ft.dropdown.Option(cod)
        #     )

        for c in self._model.getAllCorsi():
            self._view.dd_sel_corso.options.append(ft.dropdown.Option(
                key = c.codins,
                text=c.__str__()
            ))
            pass