#!/usr/bin/python
import sys
import Partida
p1=Partida.Partida(10, 1, 1, 0)

if p1.xmlz==1: p1.goiburukoa()
while p1.amaituta == False:
    if p1.xmlz==1: p1.txandaGoiburukoa();
    p1.jokatuTxanda()
    if p1.xmlz==1: p1.inprimatuTxandaXmlz()
    if p1.xmlz==1: p1.txandaBehekoa();
if p1.xmlz==1: p1.behekoa()
print "%d. jokalariak irabazi du partida! %d tirada egin dituzte." % (p1.irabazle, p1.dadoTiradaKop)

#for jokalari in p1.jokalariak:
    #print "%d jokalariaren posizioa: %d" % (jokalari.zenbakia, jokalari.posizio)
