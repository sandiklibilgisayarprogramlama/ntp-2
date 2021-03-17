from daire import Daire
from mustakil import Mustakil
from emlakci import Emlakci
from musteri import Musteri

daire1 = Daire("cumhuriyet mah.","sandıklı","İsmail koç",2,False,120,200,2,True)
daire2 = Daire("hızırbey mah.","sandıklı","Veli koç",3,False,120,200,4,True)

mustakil1 = Mustakil("bahcelievler mah","ankara","Ayşe Uzun",4,True,600,1000,150,3,"Triplex")

satilik_liste = [daire1,daire2,mustakil1]

emlakci = Emlakci("ankara","hüseyin kisa","genel",satilik_liste)

musteri1 = Musteri("Mehmet çamlı","592898492",130,190)

sonuc = emlakci.aramaYap(musteri1.istenenboyut,musteri1.istenenfiyat)

for k in sonuc:
    ev_ozellikleri =k[0]
    kriter = k[1]
    print(kriter)
    print(ev_ozellikleri.adres)
    print(ev_ozellikleri.mahallead)

""" arsa sınıfı ekleyip müşteri kriterlerine göre bulmaya çalışın.
"""