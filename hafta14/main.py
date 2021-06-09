from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import requests
from bs4 import BeautifulSoup

#export DISPLAY=:1.0
#xhost +local:

class RootWidget(BoxLayout):
    def ara(self):
        print(self.txt_il.text)
        self.get_html(self.txt_il.text)
    
    def get_html(self,il):
        r = requests.get("https://www.hurriyet.com.tr/hava-durumu/"+il+"/")
        print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        self.lbl_sonuc.text=soup.find_all("p", class_="weather-detail-hightemp")[0].text



class HavaDurumu(App):
    title="Hava durumu"
    def build(self):
        return RootWidget()

   
HavaDurumu().run()