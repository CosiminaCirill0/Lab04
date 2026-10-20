from espositore import Espositore
from stand import Stand
from standPreseElettriche import StandPreseElettriche
from standPremium import StandPremium

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.stand = []
        self.espositori = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        with open(file_path, "r", encoding="utf-8") as filecsv:
            righe = filecsv.readlines()

        for riga in righe:
            riga = riga.strip()
            if riga == "":
                continue

            campi = [c.strip() for c in riga.split(",")]

            if campi[0].startswith("ES"):
                codice_espositore = campi[0]
                nome = campi[1]
                cognome = campi[2]

                espositore = Espositore(codice_espositore, nome, cognome)
                self.espositori.append(espositore)

            elif campi[0].startswith("ST"):
                codice_stand = campi[0]
                supMetriQuadri = int(campi[1])
                numeroPadiglione = int(campi[2])
                prezzoBase = float(campi[3])

                if len(campi) == 4 or (len(campi) == 5 and campi[4] == ""):
                    stand = Stand(codice_stand, supMetriQuadri, numeroPadiglione, prezzoBase)
                    self.stand.append(stand)

                elif len(campi) == 5 and campi[4] != "":
                    campo_extra = campi[4]

                    if campo_extra.isdigit():
                        prese = int(campo_extra)
                        stand = StandPreseElettriche(codice_stand, supMetriQuadri, numeroPadiglione, prezzoBase, prese)
                        self.stand.append(stand)
                    else:
                        posizione = campo_extra
                        stand = StandPremium(codice_stand,supMetriQuadri, numeroPadiglione, prezzoBase, posizione)
                        self.stand.append(stand)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        standSelezionato = None
        for s in self.stand:
            if s.codice_stand == codice_stand:
                standSelezionato = s
                break

        if not standSelezionato:
            raise Exception("Lo Stand non è stato trovato")

        espositoreSelezionato = None
        for e in self.espositori:
            if e.codice_espositore == codice_espositore:
                espositoreSelezionato = e
                break

        if not espositoreSelezionato:
            raise Exception("L'espositore non è stato trovato")

        if standSelezionato.espositore is not None:
            raise Exception("Lo stand richiesto è già stato assegnato a un altro espositore.")

        for s in self.stand:
            if s.espositore == espositoreSelezionato:
                raise Exception("All'espositore è già stato assegnato uno stand")

        standSelezionato.espositore = espositoreSelezionato



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        if not self.espositori:
            print("Nessun espositore presente a sistema.")
            return

        for e in self.espositori:
            # Cerchiamo lo stand assegnato a questo espositore
            stand_assegnato = None
            for s in self.stand:
                if s.espositore == e:
                    stand_assegnato = s
                    break

            if stand_assegnato:
                print(f"{e} -> Assegnato a: {stand_assegnato.codice_stand}")
            else:
                print(f"{e} -> Nessuno stand assegnato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        stand_ordinati = sorted(self.stand)
        return stand_ordinati


