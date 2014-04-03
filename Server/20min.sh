#!/bin/bash
#alle 20 minuten: holen neuer Wetterdaten
cd ~/scripts

wget -q http://www.bgc-jena.mpg.de/wetter/mpi_saale.zip -O mpi_saale.zip
unzip -oq mpi_saale.zip

python parseyr.py
python parsecsv.py
