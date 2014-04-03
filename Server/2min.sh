#!/bin/sh
#alle 2 min ausfuehren: holen der Fahrplandaten

cd ~/scripts/

wget -q "http://fpl.jenah.de/bontip-ifgi/php/proxy.php?vsz=60&azbid=6103" -O lobeda.xml
wget -q "http://fpl.jenah.de/bontip-ifgi/php/proxy.php?vsz=60&azbid=6104" -O zwaetzen.xml
wget -q "http://fpl.jenah.de/bontip-ifgi/php/proxy.php?vsz=60&azbid=6501" -O westbhf.xml
wget -q "http://fpl.jenah.de/bontip-ifgi/php/proxy.php?vsz=60&azbid=6502" -O rautal.xml

python parsejenah2.py

#svg2png erst png erzeugen, dann Bittiefe aendern
rsvg-convert --dpi-x=166.66 --dpi-y=166.66 --output=screen0.png --background-color=white screen.svg
pngcrush -bit_depth 4 -c 0 screen0.png screen.png

cp screen.png /var/www/screen.png