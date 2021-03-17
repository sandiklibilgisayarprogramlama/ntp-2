from ev import Ev


class Daire(Ev):
    def __init__(self, mahallead, adres, sahipad, balkonsay, siteinindemi, m2alani, fiyat,kacincikat,asansorvarmi) -> None:
        super().__init__(mahallead, adres, sahipad, balkonsay, siteinindemi, m2alani, fiyat)
        self.kacincikat = kacincikat
        self.asansorvarmi = asansorvarmi