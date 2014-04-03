# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 15:25:37 2014

Dies liest die Vorhersage Symbolde ein, damit sie genutzt werden können.
Die Dateien sind keine vollständigen SVG Dateien sondern nur kleine Schnipsel,
die direkt in eine größere Datie eingefügt werden können.
Beschreibung der Nummern: http://om.yr.no/forklaring/symbol/

@author: dario
"""
import codecs

def symboldict():
    symdic = {}
    symdic['1'] = codecs.open('./symbols/1.svg', 'r', encoding='utf-8').read()
    symdic['2'] = codecs.open('./symbols/2.svg', 'r', encoding='utf-8').read()
    symdic['3'] = codecs.open('./symbols/3.svg', 'r', encoding='utf-8').read()
    symdic['4'] = codecs.open('./symbols/4.svg', 'r', encoding='utf-8').read()
    symdic['5'] = codecs.open('./symbols/5.svg', 'r', encoding='utf-8').read()
    symdic['6'] = codecs.open('./symbols/6.svg', 'r', encoding='utf-8').read()
    symdic['7'] = codecs.open('./symbols/7.svg', 'r', encoding='utf-8').read()
    symdic['8'] = codecs.open('./symbols/8.svg', 'r', encoding='utf-8').read()
    symdic['9'] = codecs.open('./symbols/9.svg', 'r', encoding='utf-8').read()
    symdic['10'] = symdic['9']
    symdic['11'] = codecs.open('./symbols/11.svg', 'r', encoding='utf-8').read()
    symdic['12'] = codecs.open('./symbols/12.svg', 'r', encoding='utf-8').read()
    symdic['13'] = codecs.open('./symbols/13.svg', 'r', encoding='utf-8').read()
    symdic['14'] = codecs.open('./symbols/14.svg', 'r', encoding='utf-8').read()
    symdic['15'] = codecs.open('./symbols/15.svg', 'r', encoding='utf-8').read()
    symdic['20'] = codecs.open('./symbols/20.svg', 'r', encoding='utf-8').read()
    symdic['21'] = codecs.open('./symbols/21.svg', 'r', encoding='utf-8').read()
    symdic['22'] = symdic['11']
    symdic['23'] = codecs.open('./symbols/23.svg', 'r', encoding='utf-8').read()
    
    return symdic