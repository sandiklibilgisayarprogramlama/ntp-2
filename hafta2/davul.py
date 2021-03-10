from enstruman import Enstruman

class Davul(Enstruman):
    def __init__(self,akortdurum,fiyat,yapilan_malzeme,buyukluk):
        super().__init__(akortdurum,fiyat,yapilan_malzeme)
        self.buyukluk = buyukluk