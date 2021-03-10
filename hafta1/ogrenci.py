from kisi import Kisi


class Ogrenci(Kisi):

    def __init__(self,ad,soyad,tcno,ogrno,dersler):
        super().__init__(ad,soyad,tcno)
        self.ogrno=ogrno
        self.dersler=dersler
        # super -> base sınıfa veri aktarımı

    def ogrno_ekrana_yazdir(self):
        print(self.ogrno)

    def ad_ekrana_yazdir(self):
        print(self.ad)

    def ogrenci_ekrana_yazdir(self):
        self.ekrana_yazdir()
        print(self.ogrno)
        print(self.dersler)