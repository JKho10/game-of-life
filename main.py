from spillebrett import Spillebrett

def main():
    # The user is asked about the dimensions of the board (rows and columns).
    rader = int(input("Skriv inn antall rader: "))
    kolonner = int(input("Skriv inn antall kolonner: "))

    # An object spill is created
    spill = Spillebrett(rader, kolonner)

    # Board is created
    spill.tegnBrett()

    # Printing out the generation number and the number of cells that are alive in that
    # particular generation
    print("Generasjon: ",spill._generasjonsnummer,
          "- Antall levende celler: ",spill.finnAntallLevende())

    # placeholder variable
    brukerRespons = ""

    # As long as the user´s response is not q, the game won´t stop. If the user
    # presses anything but enter, he will be asked to follow the input instructions again.
    # When the user presses enter, a new generation (board) is generated along with the
    # generation number being incremented by 1 and the current numner of cells alive.
    while brukerRespons != "q":
        brukerRespons = input("Press enter for å fortsette. Skriv inn q og trykk"
                              " enter for å avslutte").lower()
        if brukerRespons == "":
            spill.oppdatering()
            spill.tegnBrett()
            print("Generasjon: ",spill._generasjonsnummer,
             "- Antall levende celler: ",spill.finnAntallLevende())

# starte hovedprogrammet
main()

