#!/bin/sh

cd /mnt/us/weather

rm screen.png
eips -c

wget -O screen.png "http://.../screen.png"
eips -g screen.png
