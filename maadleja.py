class sportlane:
    def __init__(self, nimi: str, kaal: int) -> None:
        self.nimi = nimi
        self.kaal = kaal
    def __str__(self) -> str:
        return f"Nimi: {self.nimi}, kaal: {self.kaal} kg"
    
class maadleja(sportlane):
    def __init__(self, nimi, kaal):
        super().__init__(nimi, kaal)
        self.kaal = kaal
        if kaal <= 55:
            self.kaalukategooria = "kärbeskaal"
        elif kaal <= 66:
            self.kaalukategooria = "kergekaal"
        elif kaal <= 84:
            self.kaalukategooria = "keskkaal"
        elif kaal <= 96:
            self.kaalukategooria = "poolraskekaal"
        elif kaal > 96:
            self.kaalukategooria = "raskekaal"
        
    def muuda_kaalu(self, kaal):
        self.kaal = kaal
        if kaal <= 55:
            self.kaalukategooria = "kärbeskaal"
        elif kaal <= 66:
            self.kaalukategooria = "kergekaal"
        elif kaal <= 84:
            self.kaalukategooria = "keskkaal"
        elif kaal <= 96:
            self.kaalukategooria = "poolraskekaal"
        elif kaal > 96:
            self.kaalukategooria = "raskekaal"

    def __str__(self):
        return f"Nimi: {self.nimi}, kaal: {self.kaal} kg, kaalukategooria: {self.kaalukategooria}  "
    
sportlane = sportlane("Indrek", 105)
maadleja1 = maadleja("Georg", 83)
maadleja2 = maadleja("Kristjan", 115)
print(sportlane)
print(maadleja1)
print(maadleja2)
maadleja1.muuda_kaalu(45)
print(maadleja1)

    