class Tont:
    def __init__(self, nimi, vanus, elukoht):
        self.nimi = nimi
        self.vanus = vanus
        self.elukoht = elukoht

    def kummita(self, elukoht):
        print(f"{self.nimi} kummitab kohas {elukoht}!")

    def __str__(self):
        return f"Nimi: {self.nimi}, vanus {self.vanus}, elukoht: {self.elukoht}"
class Võlur(Tont):
    def nõiu(self, isend):
        print(f"{self.nimi} pani nõiduse, millega sai pihta {isend}!")
    

norbert = Tont("Norbert", 31, "Tartu")
snape = Võlur("Snape", 35, "Tartu")
harry = Võlur("Harry", 17, "Tartu")
print(norbert)
norbert.kummita("Tartu")
print(harry)
print(snape)
harry.nõiu("Snape")