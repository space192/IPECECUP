#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Lancer le programme en administrateur"
  exit
fi
apt-get install python3
apt-get install pyhton3-pip
apt-get install python3-pyqt5
