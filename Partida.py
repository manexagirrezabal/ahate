import Jokalari;
import random;
class Partida:
    def __init__(self, jokkop, dadokop, xmlz, debug):
        self.txanda = 0
        self.jokalariKop = int(jokkop)
        self.dadoKop = dadokop
        self.jokalariak = []
        for i in range (0,self.jokalariKop):
            jok = Jokalari.Jokalari(i)
            self.jokalariak.insert(len(self.jokalariak), jok)
        self.dadoAldeKop = 6
        self.amaituta=False
        self.irabazle=-1
        self.dadoTiradaKop=0
        self.tiradaId=0
        self.debug=int(debug)
        self.xmlz=int(xmlz)

    def ausa (self, mini, maxi):
        return int(random.random()*(maxi-mini)+mini);

    def dadoakBota(self):
        ausa = self.ausa(self.dadoKop,self.dadoKop*self.dadoAldeKop+1)
        if self.debug==1: print ("%d atera da dadoetan" % (ausa))
        self.dadoTiradaKop=self.dadoTiradaKop+1
        return ausa;

    def jokatuTxanda(self):
        if self.amaituta == True:
            exit
        else:
            self.txanda=self.txanda+1
            print ("\t<tiradak zenb=\"%d\">" % (self.txanda))
            for jokalari in self.jokalariak:
                if self.amaituta==False:
                    jokalari.berriroBota=1
                    while jokalari.berriroBota > 0:
                        self.tiradaId=self.tiradaId+1
                        jokalari.berriroBota=0
                        if jokalari.zigortuta() == False:
                            zenbakia=self.dadoakBota()
                            if zenbakia == 6:
                                jokalari.berriroBota=1
                            if self.debug==1: print ("%d-n nago! %d posizio aurreratu behar ditut") % (jokalari.posizio, zenbakia)
                            jokalari.mugitu(zenbakia)
                            self.egoeraBereziakAplikatu(jokalari.zenbakia)
                            if jokalari.amaituta() == True:
                                self.amaituta=True
                                self.irabazle=jokalari.zenbakia
                                jokalari.berriroBota=0
                        else:
                            zenbakia=-1
                            if jokalari.zigorra == "laberinto":
                                if self.dadoakBota() == 5:
                                    self.zigorraKendu(jokalari.zenbakia)
                            else:
                                self.zigorraDekrementatu(jokalari.zenbakia)
                        print ("\t\t<tirada id=\"%d\" jokalari=\"%d\" dadoetanZenbat=\"%d\"/>" % (self.tiradaId, jokalari.zenbakia, zenbakia))
                else:
                    self.tiradaId=self.tiradaId+1
                    print ("\t\t<tirada id=\"%d\" jokalari=\"%d\" dadoetanZenbat=\"%d\"/>" % (self.tiradaId, jokalari.zenbakia, 0))
            print ("\t</tiradak>")
                        
    def __str__(self):
        return "Partida zoragarria, %d txandan, %d jokalarirekin eta %d dadorekin" % (self.txanda, self.jokalariKop, self.dadoKop)

    def egoeraBereziakAplikatu(self, jokz):
        pos = self.jokalariak[jokz].posizio
        if self.debug==1: print ("%d naiz, %d-n nago eta egoera berezi bat aplikatu behar dut" % (self.jokalariak[jokz].zenbakia, pos))
        if (pos % 9 == 0) and (pos < 63) and (pos > 8):
            self.jokalariak[jokz].mugitu(5)
            self.jokalariak[jokz].berriroBota=1
            if self.debug==1: print ("De oca a oca y tiro porque me toca1")
        elif (((pos - 5) % 9) == 0) and (pos < 63) and (pos > 4):
            self.jokalariak[jokz].mugitu(4)
            self.jokalariak[jokz].berriroBota=1
            if self.debug==1: print ("De oca a oca y tiro porque me toca2")
        elif (pos == 6):
            self.jokalariak[jokz].mugitu(6)
            if self.debug==1: print ("De puente a puente")
            self.jokalariak[jokz].berriroBota=1
        elif (pos == 12):
            self.jokalariak[jokz].mugitu(-6)
            self.jokalariak[jokz].berriroBota=1
            if self.debug==1: print ("De puente a puente marcha atras")
        elif (pos == 26):
            self.jokalariak[jokz].mugitu(27)
            self.jokalariak[jokz].berriroBota=1
        elif (pos == 53):
            self.jokalariak[jokz].mugitu(-27)
            self.jokalariak[jokz].berriroBota=1
        elif (pos == 19):
            self.jokalariak[jokz].zigorraZenbat=1
            self.jokalariak[jokz].zigorra="posada"
        elif (pos == 31):
            self.jokalariak[jokz].zigorraZenbat=2
            self.jokalariak[jokz].zigorra="pozo"
        elif (pos == 19):
            self.jokalariak[jokz].zigorraZenbat=3
            self.jokalariak[jokz].zigorra="carcel"
        elif (pos == 58):
            self.jokalariak[jokz].posizio=0
        elif (pos == 42):
            self.jokalariak[jokz].zigorra="laberinto"
            self.jokalariak[jokz].zigorraZenbat=self.jokalariak[jokz].zigorraZenbat+1
        else:
            if self.debug==1: print ("Ezin izan dut egoera berezirik aplikatu!")
            
    def inprimatuTxandaXmlz(self):
        print ("\t<txandaInfo zenb=\"%d\">" % (self.txanda))
        for jokalari in self.jokalariak:
            print ("\t\t<jokalari zenb=\"%d\" posizio=\"%d\"/>" % (jokalari.zenbakia, jokalari.posizio))
        print ("\t</txandaInfo>")

    def zigorraKendu(self, jokz):
        self.jokalariak[jokz].zigorra=""
        self.jokalariak[jokz].zigorraZenbat=0

    def zigorraDekrementatu(self, jokz):
        self.jokalariak[jokz].zigorraZenbat=self.jokalariak[jokz].zigorraZenbat-1
        if self.jokalariak[jokz].zigorraZenbat==0: self.jokalariak[jokz].zigorra=""

    def behekoa(self):
        print ("</partida>")

    def goiburukoa(self):
        print ("<partida>")

    def txandaBehekoa(self):
        print ("</txanda>")

    def txandaGoiburukoa(self):
        print ("<txanda zenb=\"%d\">" % (self.txanda+1))
