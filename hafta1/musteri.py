from kisi import Kisi


class Musteri(Kisi):
    
    def __init__(self, ad, soyad, tcno,kalanBakiye):
        super().__init__(ad, soyad, tcno)
        self.kalan_bakiye=kalanBakiye

    def bilgiler_ekrana_yazdir(self):
        self.ekrana_yazdir()
        print(self.kalan_bakiye)