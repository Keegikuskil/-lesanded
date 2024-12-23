class tont:
    def __init__(self, nimi, vanus, elukoht):
        self.nimi = nimi
        self.vanus = vanus
        self.elukoht = elukoht
    def kummita():
        print(f"{nimi} kummitab kohas {elukoht}!")
    def __str__(self):
        return f"Nimi: {self.nimi}, vanus: {self.vanus}, elukoht{self.elukoht}"

class võlur(tont):
    def nõiu(nõiutav, nõiduja):
        print(f"{nõiduja} nõiub {nõiutav}!")


harry = võlur("Harry", 17, "Tartu", nõiduja)


#1. tont nimega Norbert, 31-aastane, elukoht Tartu;
#2. võlur nimega Harry, 17-aastane, elukoht Tartu;
#3. võlur nimega Snape, 35-aastane, elukoht Tartu.



