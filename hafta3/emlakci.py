class Emlakci:
    def __init__(self,subead,adsoyad,mevki,satilikevler):
        self.subead= subead
        self.adsoyad= adsoyad
        self.mevki= mevki
        self.satilikevler= satilikevler
    
    def aramaYap(self,istenenboyut,istenenfiyat):
        bosListe=[]
        for ev in self.satilikevler:
            if (ev.m2alani - istenenboyut <=10 and istenenboyut - ev.m2alani <=10) and ev.fiyat- istenenfiyat<10:
                bosListe.append((ev,"Tüm isteklerinize uyuyor"))
            elif (ev.m2alani - istenenboyut <=10 and istenenboyut - ev.m2alani <=10):
                bosListe.append((ev,"boyut bakımından isteğinize yakın"))
            elif ev.fiyat - istenenfiyat<=10:
                bosListe.append((ev,"fiyat bakımından isteğinize yakın"))

        return bosListe


            