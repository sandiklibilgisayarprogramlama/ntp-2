# 0 ile 100 arasında girilen 2 sayıyı toplayan programı kodlayınız.
class KucukVeriHatasi(Exception):
    pass

class BuyukVeriHatasi(Exception):
    pass

s1 = int(input(" 0 ile 100 arasında bir değer giriniz"))
s2 = int(input("0 ile 100 arasında bir değer giriniz"))
if s1 < 0 or s2 < 0:
    raise KucukVeriHatasi("girilen veriler 0 dan küçük olamaz")

if s1>100 or s2>100:
    raise BuyukVeriHatasi("girilen veriler 100 den büyük olamaz")

print("toplam sonucu :"+str(s1+s2))

