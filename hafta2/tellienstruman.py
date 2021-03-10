from enstruman import Enstruman
class TelliEnstruman(Enstruman):
    def __init__(self,akortdurum,fiyat,yapilan_malzeme,tel_sayisi,sap_uzunlugu,elektro_destegi):
        super().__init__(akortdurum,fiyat,yapilan_malzeme)
        self.tel_sayisi=tel_sayisi
        self.sap_uzunlugu=sap_uzunlugu
        self.elektro_destegi=elektro_destegi