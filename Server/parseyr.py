# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:14:08 2014

Hier wird die Vorhersagen von yr.no ausgewertet, der Download erfolgt in diesem
Script. 

@author: dario
"""

import lxml.etree as ET
import requests
import datetime
from svgyr import svgyr #an SVG geben

def get_weather(i):#Funktion, die die Daten ausliest
    wetter = {}
    wetter['time'] = root[5][0][i].attrib #welches Tageszeit
    wetter['sky'] = root[5][0][i][1].attrib   #Bewökung/Niederschlagsart
    wetter['temp'] = root[5][0][i][6].attrib  #Temperatur
    wetter['prec'] = root[5][0][i][2].attrib  #Niederschlagsmenge
    return wetter

#einlesen der vorhandenen Datei
varsel  = ET.parse('varsel.xml')
root = varsel.getroot()

#wenn daten zu alt sind, dann hole neue daten
nextupdate = root[3][1].text #datum für nächstes Update lesen und umwandeln
next_time = datetime.datetime.strptime( nextupdate, "%Y-%m-%dT%H:%M:%S" )

#Ende der Gültigkeit des ersten Wertes auslesen und umwandeln
valid = datetime.datetime.strptime(root[5][0][0].attrib['to'], "%Y-%m-%dT%H:%M:%S" )

#nur neu verarbeiten, wenn neue Daten da, oder neues Viertel begonnen hat
if datetime.datetime.now() > next_time or datetime.datetime.now() > valid:
    varsel  = ET.parse('http://www.yr.no/sted/Tyskland/Th%C3%BCringen/Jena/varsel.xml')
    root = varsel.getroot()
    weather = {}
    weather['sun'] = root[4].attrib	#Sonnenauf (rise)- und untergang (set)    
    
    weather['std0'] = get_weather(0)    #jetzige Vorhersage
    weather['std6'] = get_weather(1)     #nächste Tageshälfte
    weather['std12'] = get_weather(2)    #...
    weather['std18'] = get_weather(3)
    
    #an SVG übergeben
    svgyr(weather)
    #neu geladenen Daten speichern
    varsel.write('varsel.xml', encoding="UTF-8",  xml_declaration=True)