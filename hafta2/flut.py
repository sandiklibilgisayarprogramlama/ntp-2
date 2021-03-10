from enstruman import Enstruman

class Flut(Enstruman):
    def __init__(self,akortdurum,fiyat,yapilan_malzeme,flut_turu):
        super().__init__(akortdurum,fiyat,yapilan_malzeme)
        self.flut_turu = flut_turu
    
    def cal(self,nota):
        print(__name__+" "+nota)