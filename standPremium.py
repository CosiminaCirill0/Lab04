from stand import Stand

class StandPremium(Stand):
    def __init__(self, codice_stand, supMetriQuadri, numeroPadiglione, prezzoBase, posizione):
        prezzo_finale = round((prezzoBase * 1.30), 2)
        super().__init__(codice_stand, supMetriQuadri, numeroPadiglione, prezzo_finale)
        self.__posizione = posizione

    def __str__(self):
        return f"{super().__str__()} Posizione:{self.__posizione}"
