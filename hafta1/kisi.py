"""
Base Class
python' da tüm sınıflar ön tanımlı object sınıfından miras alır ! 
"""
class Kisi:
    def __init__(self,ad,soyad,tcno):
        self.ad=ad
        self.soyad=soyad
        self.tcno=tcno

    def ekrana_yazdir(self):
        print(self.ad)
        print(self.soyad)
        print(self.tcno)