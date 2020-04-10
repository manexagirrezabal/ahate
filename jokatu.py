#!/usr/bin/python
import sys
import Partida
import screen

from matplotlib import pyplot as plt


p1=Partida.Partida(4, 1, 1, 0)

if p1.xmlz==1: p1.goiburukoa()
while p1.amaituta == False:
    if p1.xmlz==1: p1.txandaGoiburukoa();
    p1.jokatuTxanda()
    if p1.xmlz==1: p1.inprimatuTxandaXmlz()
    if p1.xmlz==1: p1.txandaBehekoa();
    positions = [jokalari.posizio for jokalari in p1.jokalariak]

    print (positions)
    plotted_ones = screen.show_situation(positions)

    plt.waitforbuttonpress()
    
    screen.clean_plotted(plotted_ones)
if p1.xmlz==1: p1.behekoa()
print ("%d. jokalariak irabazi du partida! %d tirada egin dituzte." % (p1.irabazle, p1.dadoTiradaKop))

#for jokalari in p1.jokalariak:
    #print "%d jokalariaren posizioa: %d" % (jokalari.zenbakia, jokalari.posizio)
