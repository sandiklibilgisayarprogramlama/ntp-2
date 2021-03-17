from ev import Ev


class Mustakil(Ev):
    def __init__(self, mahallead, adres, sahipad, balkonsay, siteinindemi, m2alani, fiyat,bahceboyut,katsayisi,tur):
        super().__init__(mahallead, adres, sahipad, balkonsay, siteinindemi, m2alani, fiyat)
        self.bahceboyut = bahceboyut
        self.katsayisi = katsayisi
        self.tur = tur