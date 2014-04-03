# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 11:46:25 2014

Dies schreibt die Wettervorhersage in die SVG-Datei

@author: dario
"""
import datetime
import codecs
from symboldict import symboldict #hier werden die ganzen Vorhersagesymbole eingelesen

def svgyr(wetteryr):
    #Ersetzen von Sonnenauf- und untergang
    sunrise = datetime.datetime.strptime( wetteryr['sun']['rise'], '%Y-%m-%dT%H:%M:%S' )    
    sunset = datetime.datetime.strptime( wetteryr['sun']['set'], '%Y-%m-%dT%H:%M:%S' )
    tmplt = codecs.open('template-subst.svg', 'r', encoding='utf-8').read()
    tmplt = tmplt.replace('SUNSET', sunset.strftime('%H:%M'))
    tmplt = tmplt.replace('SUNRISE', sunrise.strftime('%H:%M'))
    
    #Ersetzen von Vorhersage
    #Day = {'0': str('0:00 bis 6:00'), '1': str('6:00 bis 12:00'),'2': str('12:00 bis 18:00'),'3': str('18:00 bis 0:00')}
    Day = {'0': str(u'2. Nachthälfte'), '1':'Vormittag', '2':'Nachmittag', '3':str(u'1. Nachthälfte')}
    Symbols = symboldict()
    i=1
    liste = ['std0', 'std6', 'std12']
    for key in liste:
        nr=str(i)
        tmplt = tmplt.replace('TEMP'+nr, wetteryr[key]['temp']['value'])
        tmplt = tmplt.replace('PREC'+nr, wetteryr[key]['prec']['value'])
        tmplt = tmplt.replace('DAYTIME'+nr, Day[wetteryr[key]['time']['period']])
        tmplt = tmplt.replace('SYMBOL'+nr, Symbols[wetteryr[key]['sky']['number']])
        i+=1
    
    #neues SVG schreiben
    codecs.open('template-yr.svg', 'w', encoding='utf-8').write(tmplt)
    return 0
