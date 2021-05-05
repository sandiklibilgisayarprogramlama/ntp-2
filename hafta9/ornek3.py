# 0 ile 100 arasında girilen 2 sayıyı toplayan programı kodlayınız.

s1 = int(input(" 0 ile 100 arasında bir değer giriniz"))
s2 = int(input("0 ile 100 arasında bir değer giriniz"))
assert s1 < 0 or s2 < 0, "girilen ifadeler 0 dan büyük olmalı"
assert s1>100 or s2>100, "girilen ifadeler 100den küçük olmalı"

print("toplam sonucu :"+str(s1+s2))