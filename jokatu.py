#!/usr/bin/python
import sys
import Partida
import screen
from matplotlib import pyplot as plt

plt.show()



p1=Partida.Partida(4, 1, 1, 1)

plt.subplot(1,2,2,aspect="equal")

p1.jokalariak[0].izena="Imanol"
p1.jokalariak[1].izena="Oier"
p1.jokalariak[2].izena="Gorka"
p1.jokalariak[3].izena="Manex"


plt.subplot(1,2,2,aspect="equal")

plt.cla()

screen.plot_number(0, ax=plt)
screen.show_players(p1,p1.jokalariak[0])

plt.subplot(1,2,1)
positions = [jokalari.posizio if jokalari.posizio != 0 else 1 for jokalari in p1.jokalariak]
plotted_ones = screen.show_situation(positions)
ev = plt.waitforbuttonpress()
if ev == "q":
    exit()

screen.clean_plotted(plotted_ones)


if p1.xmlz==1: p1.goiburukoa()
while p1.amaituta == False:
    if p1.xmlz==1: p1.txandaGoiburukoa();
    p1.jokatuTxanda()
    if p1.xmlz==1: p1.inprimatuTxandaXmlz()
    if p1.xmlz==1: p1.txandaBehekoa();


#    positions = [jokalari.posizio if jokalari.posizio != 0 else 1 for jokalari in p1.jokalariak]
#    plotted_ones = screen.show_situation(positions)
#    plt.waitforbuttonpress()
#    screen.clean_plotted(plotted_ones)


if p1.xmlz==1: p1.behekoa()
print ("%d. jokalariak irabazi du partida! %d tirada egin dituzte." % (p1.irabazle, p1.dadoTiradaKop))

#for jokalari in p1.jokalariak:
    #print "%d jokalariaren posizioa: %d" % (jokalari.zenbakia, jokalari.posizio)
