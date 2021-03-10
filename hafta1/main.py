from calisan import calisan
from musteri import Musteri
from ogrenci import Ogrenci
"""
ogr=Ogrenci("Ahmet","Uzun",241312312313,"324234234",[])
ogr.ogrenci_ekrana_yazdir()
"""
musteri = Musteri("Ahmet","Uzun",241312312313,600)

musteri.bilgiler_ekrana_yazdir()

print(musteri.__class__.__name__ )
