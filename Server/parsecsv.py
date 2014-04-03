# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:01:34 2014

Hier werden die Wetterdaten des MPI-BGC verarbeitet. Die Daten müssen sperat
heruntergeladen und entpackt werden.

@author: dario
"""
from svgmpi import svgmpi #Script zum einfügen in SVG-Datei 

#Lese erste und letzte Zeile der csv Datei ein und mache ein dict draus.

with open('mpi_saale.csv', "rb") as w:
    first = w.readline()     # Read the first line.
    w.seek(-2, 2)            # Jump to the second last byte.
    while w.read(1) != "\n": # Until EOL is found...
        w.seek(-2, 1)        # ...jump back the read byte plus one more.
    last = w.readline()      # Read last line.
    
first = first.translate(None, '"') #Anführungszeichen (") löschen

datalist = last.split(",")  #an Kommas auftrennen und Liste draus machen
headerlist = first.split(",")

zipdata = zip(headerlist, datalist) #paarweise zusammenfügen
wetterdata = dict(zipdata)  #in dictionary umwandeln

svgmpi(wetterdata) #an SVG übergeben