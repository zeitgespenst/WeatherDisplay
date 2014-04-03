# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 20:30:56 2014
Hiermit werden die Fahrplandaten in das SVG-Template geschrieben.

@author: dario
"""
import datetime
import codecs

def subst(sort_ab): #ersetzen der Platzhalter durch die sortierten Daten
    tmplt = codecs.open('template-wetter.svg', 'r', encoding='utf-8').read()    #SVG lesen
    length = len(sort_ab)
    if length == 0:
        tmplt = tmplt.replace('ZIEL3', 'Keine Abfahrten!')  #mögliches leeres Array abfangen
    for i in range(length):
        nr = str(i)
        tmplt = tmplt.replace('ZIEL'+nr, sort_ab[i][0])
        tmplt = tmplt.replace('LINE'+nr, sort_ab[i][1])
        tmplt = tmplt.replace('TIME'+nr, sort_ab[i][2].strftime('%H:%M'))
    for i in range(length,8):   #wenn weniger als 8 Abfahrten dann leere Felder einfügen
        nr = str(i)
        tmplt = tmplt.replace('ZIEL'+nr, '')
        tmplt = tmplt.replace('LINE'+nr, '')
        tmplt = tmplt.replace('TIME'+nr, '') 

    return tmplt

def iter_ab(dic):#macht aus verzweigtem Dictionary eine Liste (rekursiv)
    for val in dic.itervalues():
        if type(val) == dict:
            iter_ab(val)
        else:
                ablist.append(val)
    return ablist

def svgtram(abfahrten): #eigentliche Funktion
    global ablist   #als gloabal da eine feste Liste von iter_ab verwendet werden muss
    ablist = []
    abfliste = []
    abfliste = iter_ab(abfahrten) #Dict2List
    
    newablist = [''] * int((len(abfliste)/3))   #Liste entsprechend der Anzahl der Einträge
    
    for i in range(0, len(abfliste), 3):    #Abfahrten in Liste schreiben
        j=i/3
        newablist[j] = [abfliste[i], abfliste[i+1], abfliste[i+2]]
        newablist[j][2] = datetime.datetime.strptime( newablist[j][2], '%Y-%m-%dT%H:%M:%S' )
    #Sortieren der Liste
    sort_ab = sorted(newablist, key=lambda abfahrt: abfahrt[2])
    
    #In SVG-Datei ersetzen
    final = subst(sort_ab)
    #neues SVG schreiben
    codecs.open('screen.svg', 'w', encoding='utf-8').write(final)