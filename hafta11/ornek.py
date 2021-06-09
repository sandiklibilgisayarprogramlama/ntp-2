# os modülü
# operating system -> os


import os
"""
listdir
path.join
mkdir
rmdir
remove
"""

# listdir -> klasör içindeki tüm dosyaları listelemek amaclı kullanılır.
#print(os.listdir("klasor"))

#for k in os.listdir("klasor"):
#    print(k)

# path.join -> dosya veya klasör yollarını birleştirmek ve yol üretmek amacıyla kullanılır.

yol = os.path.join("klasor","yeniklasor")
print(yol)

"""dosya=open(yol,"r")
icerik=dosya.readline()
dosya.close()"""

print(os.listdir(yol))

# pythonda os.path.join metodunun yaptığı işlevi gerçekleştiren kendi metodunuzu yazınız.

def ozelyol(liste):
    return "/".join(liste)

print(ozelyol(["klasor","yeniklasor"]))


# os içinde bulunan mkdir fonksiyonu yeni klasor oluşturmaya yarar.
# not: os.path.exist(param) parametre olarak verilen yol var mı yok mu kontrolu yapar.
"""print(os.listdir("klasor"))

os.mkdir(os.path.join("klasor","yenibirklasor"))
print(os.listdir("klasor"))
"""
# 
print(os.listdir("klasor"))
olusturacak_yol=os.path.join("klasor","ahmet")
if (not os.path.exists(olusturacak_yol)): # bu şekilde file exist error hatasından kurtuluruz.
    os.mkdir(olusturacak_yol)
print(os.listdir("klasor"))

# rmdir klasor silmek için kullanılır.
silinecek_yol = os.path.join("klasor","ahmet4")
if(os.path.exists(silinecek_yol)): # bu şekilde file not found hatasından kurtuluruz.
    os.rmdir(silinecek_yol)

# remove dosya silmek için kullanılır.

if(os.path.exists(os.path.join("klasor","deneme2"))): # bu şekilde file not found hatasından kurtuluruz.
    os.remove(os.path.join("klasor","deneme2"))
