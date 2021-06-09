import string
from kivy.uix.textinput import TextInput

class MyFloatInput(TextInput):

    def __init__(self, **kwargs):
        super(MyFloatInput, self).__init__(**kwargs)
        self.multiline = False
        self.izin = ["(",")","%","AC","7","8","9","/","4","5","6","*","1","2","3","-","0",".","=","+"]


    def insert_text(self, theText, from_undo=False):
        if theText not in self.izin:
            return
        if '.' in self.text and theText == '.':
            return

        maxWidth = self.width - self.padding[0] - self.padding[2]
        cc, cr = self.cursor
        curText = self._lines[cr]
        new_text = curText[:cc] + theText + curText[cc:]
        textWidth = self._get_text_width(new_text, self.tab_width, self._label_cached)
        while textWidth < maxWidth:
            new_text = ' ' + new_text
            textWidth = self._get_text_width(new_text, self.tab_width, self._label_cached)
        while textWidth >= maxWidth:
            if new_text[0] != ' ':
                break
            else:
                new_text = new_text[1:]
                textWidth = self._get_text_width(new_text, self.tab_width, self._label_cached)
        self._lines[cr] = ''
        self.cursor = (0,cr)
        super(MyFloatInput, self).insert_text(new_text, from_undo=from_undo)