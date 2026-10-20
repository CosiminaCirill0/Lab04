class Stand:
    def __init__(self, codice_stand, supMetriQuadri, numeroPadiglione, prezzoBase):
        self.__codice_stand = codice_stand
        self.__supMetriQuadri = supMetriQuadri
        self.__numeroPadiglione = numeroPadiglione
        self.__prezzoBase = float(prezzoBase)
        self.__espositore = None

    @property
    def codice_stand(self):
        return self.__codice_stand

    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self, nuovoEspositore):
        self.__espositore = nuovoEspositore

    def __str__(self):
        stato = "Disponibile" if self.__espositore is None else f"Assegnato a {self.__espositore.codice_espositore}"
        return f"{self.__codice_stand} | {self.__supMetriQuadri} mq - Padiglione {self.__numeroPadiglione} - {self.__prezzoBase:.2f}€ - {stato}"

    def __lt__(self, other):
        # dice a python come confrontare DUE STAND
        return self.__prezzoBase < other.__prezzoBase
