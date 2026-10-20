from stand import Stand

class StandPreseElettriche(Stand):
    def __init__(self, codice_stand, supMetriQuadri, numeroPadiglione, prezzoBase, preseAggiuntive):
        prezzo_finale = round(prezzoBase * (1 + 0.07 * preseAggiuntive), 2)
        super().__init__(codice_stand, supMetriQuadri, numeroPadiglione, prezzo_finale)
        self.__preseAggiuntive = preseAggiuntive

    def __str__(self):
        return f"{super().__str__()} Prese Extra:{self.__preseAggiuntive}"