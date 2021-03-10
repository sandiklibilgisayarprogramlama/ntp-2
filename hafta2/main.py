from flut import Flut
from gitar import Gitar
from tellienstruman import TelliEnstruman
from davul import Davul

flut1=Flut(False,100,"plastik","yanflüt")
gitar1=Gitar(True,300,"tahta",4,"90",True,3)
saz = TelliEnstruman(True,250,"tahta",5,"120",True)
davul1 = Davul(False,500,"tahta","50x50")

flut1.cal("do")
gitar1.cal()