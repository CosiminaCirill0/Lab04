class Espositore:
    def __init__(self, codice_espositore, nome, cognome):
        self.__codice_espositore = codice_espositore
        self.__nome = nome
        self.__cognome = cognome

    @property
    def codice_espositore(self):
        return self.__codice_espositore

    def __str__(self):
        return f"{self.__codice_espositore} {self.__nome} {self.__cognome}"