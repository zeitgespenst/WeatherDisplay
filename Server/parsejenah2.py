# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:04:43 2014

Hier werden die Fahrplandaten des IST-Fahrplans verarbeitet. Die Daten müssen
vorher per Shell-Script geladen werden.

@author: dario
"""

import xml.etree.ElementTree as ET
from svgjenah import svgtram    #setzt Daten in SVG-Datei ein

#eine Funktion die aus den immer gleich aufgebauten Dateien die Daten sammelt
def ab(richtung):

    tree  = ET.parse(richtung+'.xml')   #XML importieren
    xml = tree.getroot()

    abfahrt = {}    #leeres dictionary erstellen
    length = len(xml[1].getchildren())  #Länge auslesen

    if length > 2:  #Länge auf zwei beschränken
        length = 2

    for i in range(length): #über Länge iterieren (0 bis länge-1) passt genau
        abfahrt['a'+str(i)] = {}  #Dictionary anlegen
        abfahrt['a'+str(i)]['linie'] = xml[1][i][4].text  #Linientext
        abfahrt['a'+str(i)]['richtung'] = xml[1][i][6].text   #Richtungstext
        abfahrt['a'+str(i)]['abfahrt'] = xml[1][i][12].text   #IST-Abfahrt
    return abfahrt  #Dict mit zwei Dicts mit Abfahrtzeiten etc. zurückgeben

#Start eigentliches Programm:
#erstelle ein dictionary mit einem Dict für jeden Haltepunkt

abfahrten = {}

abfahrten['zwaetzen'] = ab('zwaetzen')

abfahrten['lobeda'] = ab('lobeda')

abfahrten['westbhf'] = ab('westbhf')

abfahrten['rautal'] = ab('rautal')

#einfügen der Daten in SVG
svgtram(abfahrten)