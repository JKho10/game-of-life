from random import randint
from celle import Celle

class Spillebrett:
    # The constructor will have four instance variables notably self._rader which
    # initiates the rows, self._kolonner which initiates the columns,
    # self._rutenett which is an empty list and self._generasjonsnummer
    # which is set to zero at the beginning and increases as the board updates.
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjonsnummer = 0

    # A nested list is made by going through 2 for-loops where it runs through the
    # columns and rows accordingly. A list is appended to the board. A cell object
    # is appended to the list. The method _generer is then called in which 1/3
    # of the cells become alive.

        for rad in range(self._rader):
            list = []
            for kolonne in range(self._kolonner):
                list.append(Celle())
            self._rutenett.append(list)

        self._generer()

    # Nested for-loop that goes through the board and tells about the status of each
    # cell. A new line is printed at the start of the next row.
    def tegnBrett(self):
        for i in range(3):
            print("\n")
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                print(self._rutenett[rad][kolonne].hentStatusTegn(), end="")
            print()

    # Two lists: skalLeve (contain dead cells that will become alive)
    # and skalDoed (contain living cells that will die) are created.
    # The method will go through the board via a nested for-loop to find the cell´s
    # coordinates. It will check if the neighbouring cells around the selected
    # cell are alive or dead. Depending on the status of the neighbouring cells,
    # it will determine whether the current cell will continue to live or die.
    def oppdatering(self):
        skalLeve = []
        skalDoe = []

        for rad in range(self._rader):
            for kolonne in range(self._kolonner):

                celleKoordinater = self._rutenett[rad][kolonne]

                # A new list is created and will contain all living neighbouring cells
                # around the current cell.
                naboer = self.finnNabo(rad, kolonne)
                naboerSomErLevende = []

                # For each neighbour, if the neighbouring cell is alive, it is appended
                # to the list.
                for nabo in naboer:
                    if nabo.erLevende():
                        naboerSomErLevende.append(nabo)

                if celleKoordinater.erLevende():
                    # With 2 or 3 neighbours, cell remains alive
                    if len(naboerSomErLevende) in range(2, 4):
                        skalLeve.append(celleKoordinater)
                    # cell dies if it has less than 2 (underpop.) or
                    # more than 3 (overpop.) neighbours
                    elif len(naboerSomErLevende) < 2 or len(naboerSomErLevende) > 3:
                        skalDoe.append(celleKoordinater)
                    # cell revives if it has 3 neighbouring cell that are alive
                else:
                    if len(naboerSomErLevende) == 3:
                        skalLeve.append(celleKoordinater)

         # Status of the cells are changed in the given list
        for celleStatus in skalLeve:
            celleStatus.settLevende()

        for celleStatus in skalDoe:
            celleStatus.settDoed()

        # When the board updates, it is incremeted by 1.
        self._generasjonsnummer += 1

    # For each living cell in the board, increment levende by 1.
    def finnAntallLevende(self):
        levendeCelle = 0
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                if self._rutenett[rad][kolonne].erLevende():
                    levendeCelle += 1
        return levendeCelle

    # The method _generer goes through the rows and columns through a nested
    # loop. The variable tilfeldigTall is created where a random number
    # between 0 and 2 is selected. If the random number is 0, the cell at that
    # particular coordinate will be set to alive.
    def _generer(self):
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                tilfeldigTall = randint(0,2)
                if tilfeldigTall == 0:
                    self._rutenett[rad][kolonne].settLevende()

    # The method finnNabo was adapted from the live koding video from Uke 10.
    # The cell will live or die depending on the neighbouring cells´ status.
    # An empty list, naboer, for the neighbouring cells is created. A nested
    # for-loop checks for the neighbouring cells from -1, 0 and 1, i.e.
    # one cell before the actual cell, the current cell and one cell after
    # the actual cell. The if statements check for the corners and edges to
    # make sure the cells are within the board and are not equal to the
    # current cell. Once all the criteria are fulfilled, the neighbours are
    # appended to the list.
    def finnNabo(self, rad, kolonne):
        naboer = []
        for r in range(-1, 2):
            for k in range(-1, 2):
                naboRad = rad + r
                naboKolonne = kolonne + k
                gyldigNabo = True

                if naboRad < 0 or naboRad >= self._rader:
                    gyldigNabo = False

                if naboKolonne < 0 or naboKolonne >= self._kolonner:
                    gyldigNabo = False

                if naboRad == rad and naboKolonne == kolonne:
                    gyldigNabo = False

                if gyldigNabo:
                    naboer.append(self._rutenett[naboRad][naboKolonne])
        return naboer
