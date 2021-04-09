#!/bin/bash
if [ "$EUID$ -ne 0 ]
  then echo "Lancer le programme en tant qu'administrateur"
  exit
fi
apt-get remove python3-pyqt5
apt autoremove
