from tellienstruman import TelliEnstruman
from playsound import playsound

class Gitar(TelliEnstruman):
    def __init__(self,akortdurum,fiyat,yapilan_malzeme,tel_sayisi,sap_uzunlugu,elektro_destegi,pena_kalinligi):
        super().__init__(akortdurum,fiyat,yapilan_malzeme,tel_sayisi,sap_uzunlugu,elektro_destegi)
        self.pena_kalinligi = pena_kalinligi
    
    def cal(self):
        playsound('guitar.WAV')