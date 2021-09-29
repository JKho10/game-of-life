class Celle:
    # Konstruktør with cell´s status initialized to dead
    def __init__(self):
        self._status = "doed"

    # Change status to dead
    def settDoed(self):
        self._status = "doed"

    # Change status to alive
    def settLevende(self):
        self._status = "levende"

    # ErLevende returns the cell´s status, True if it is alive and false if it is dead
    def erLevende(self):
        if self._status == "levende":
            return True
        return False

    # hentStatusTegn returns O is the cell is alive and . if the cell is dead.
    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        else:
            return "."

    def __str__(self):
        return self._status


