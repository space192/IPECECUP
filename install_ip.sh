#!/bin/bash
if [ "$EUID$ -ne 0 ]
  then echo "Lancer le programme en tant qu'administrateur"
  exit
fi
apt-get update
apt-get upgrade -y
apt-get install python3
apt-get install pyhton3-pip
apt-get install python3-pyqt5
