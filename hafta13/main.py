from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#export DISPLAY=:1.0
#xhost +local:

class Program(App):
    title = "Selam"

    def on_start(self):
        #self.lbl.text = "Yazbel"
        # bir takım işlemler...
        pass

    def on_stop(self):
        # Uygulama kapatılırken...
        pass

    def on_pause(self):
        # Uygulama arkaplana alınırken...
        # Burda return True yapmanız gerekiyor
        return True

    def on_resume(self):
        # Tekrar giriş yapıldığında yazımızı değiştiriyoruz
        #self.lbl.text = "Programa tekrar hoşgeldiniz"
        pass
    
    def build(self):
        self.anaDuzen = BoxLayout(orientation = "vertical")
        self.ilkSatir = BoxLayout()
        self.ikinciSatir = BoxLayout()

        self.nick = Label(text = "Nick")
        self.nickKutu = TextInput()

        self.sifre = Label(text = "Şifre")
        self.sifreKutu = TextInput()

        self.buton = Button(text = "Giriş Yap")


        self.ilkSatir.add_widget(self.nick)
        self.ilkSatir.add_widget(self.nickKutu)

        self.ikinciSatir.add_widget(self.sifre)
        self.ikinciSatir.add_widget(self.sifreKutu)

        # Şimdi hepsini ana düzene yerleştiriyoruz

        self.anaDuzen.add_widget(self.ilkSatir)
        self.anaDuzen.add_widget(self.ikinciSatir)
        self.anaDuzen.add_widget(self.buton)

        return self.anaDuzen


Program().run()