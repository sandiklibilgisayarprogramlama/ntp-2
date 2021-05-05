# print("dasdasda")
"""

print("iki sayıyı toplayan program")

try:
    kod
except e:
    print("girdiğiniz  veri tipi yanlış, tekrar deneyiniz.")

print("dasdsa")
try:
    s1=float(input("birinci sayıyı giriniz"))
    s2=int(input("ikinci sayıyı giriniz"))

    print(s1/s2)
except ValueError as e: # int -> str int -> float
    print("mail gönder. içerik : ",e)
except ZeroDivisionError as e1:
    print("bir sayıyı 0 a bölmeye çalıştınız. Böyle bir durum olamaz.")

print("selamlar...")

# programcı hatası

# programcı doğru yaptığını düşünüyor, kullanıcı yanlış karakter girdi. 0 -> O

# try - except - else
"""
# else: try - except yapılarında try içine yazılan kodda program herhangi bir hata vermiyor ise
# else blogunun içindeki kod çalıştırılır.
try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
else:
    print("program hatasız çalıştı.")

# finally: program hata versede vermesede girilen blog.

try:
    f= open("deneme.txt","w")
    f.write("dasda")
except:
    pass
finally:
    f.close()
    print("try - except sonlandı.")


bolen = 0
if bolen==0:
    raise Exception("0 a bölme hatası")

