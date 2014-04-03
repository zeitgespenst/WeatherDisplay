# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 13:08:12 2014

Hiermit werden die Wetterdaten in das SVG-Template geschrieben.

@author: dario
"""
import codecs
import datetime
import locale

def svgmpi(wetter):
    tmplt = codecs.open('template-yr.svg', 'r', encoding='utf-8').read() #lesen
    #alle Werte runden und wieder in str umwandeln
    temperature = int(round(float(wetter['T (degC)'])))
    relhum = int(round(float(wetter['rh (%)'])))
    wind = int(round(float(wetter['wv (m/s)'])))
    
    #Platzhalter ersetzen
    tmplt = tmplt.replace('TEMP0', str(temperature))
    tmplt = tmplt.replace('RH', str(relhum))
    tmplt = tmplt.replace('WS', str(wind))
    
    #Lokaliserung auf deutsch setzen für Datum und Datum erstzen
    locale.setlocale(locale.LC_ALL, 'deu_deu')  #windows
    #locale.setlocale(locale.LC_ALL, 'de_DE')   #unix
    now = datetime.date.today()
    today = now.strftime('%A, %d. %B %Y')
    tmplt = tmplt.replace('DATE', today)
    
    #neue SVG-Datei schreiben
    codecs.open('template-wetter.svg', 'w', encoding='utf-8').write(tmplt)
    return 0