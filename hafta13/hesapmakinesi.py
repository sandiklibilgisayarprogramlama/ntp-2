from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from multilinerightinput import MyFloatInput
from kivy.uix.button import Button

class HesapMakinesi(App):
    title="Hesap Makinesi v1"

    def build(self):
        self.anaduzen = BoxLayout(orientation="vertical")
        self.text_input = MyFloatInput()
        self.anaduzen.add_widget(self.text_input)
        self.grid_layout = GridLayout(cols = 4)

        hesap_makine=["(",")","%","AC","7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+"]

        for i in hesap_makine:
            self.buton=Button(text = "{}".format(i))
            self.buton.bind(on_press = self.press)
            self.grid_layout.add_widget(self.buton)

        self.anaduzen.add_widget(self.grid_layout)
        
        return self.anaduzen
    
    def press(self,nesne):
        if nesne.text == "AC":
            self.text_input.text=""
        elif nesne.text == "=":
            islem = self.text_input.text
            if len(islem)>0:
                try:
                    sonuc = eval(islem)
                    print(sonuc)
                    #self.text_input.text=""
                    self.text_input.insert_text("=")
                    self.text_input.insert_text(str(sonuc))

                except SyntaxError:
                    self.text_input.background_color=(163, 53, 30, 0)
        else:
            self.text_input.insert_text( nesne.text)
        
HesapMakinesi().run()