class Jokalari:
    def __init__ (self, zenb,izena=None):
        self.zenbakia=zenb;
        self.posizio=0;
        self.zigorra="";
        self.zigorraZenbat=0;
        self.berriroBota=0;
        if izena is None:
            self.izena = "jokalari"+str(zenb)
        else:
            self.izena = izena

    def zigortuta (self):
        if self.zigorraZenbat > 0:
            return True
        else:
            return False

    def mugitu (self, kop):
        self.posizio=self.posizio+kop;
        if self.posizio > 63:
            self.posizio = 63 - (self.posizio - 63)

    def amaituta (self):
        if self.posizio == 63:
            return True
        else:
            return False
