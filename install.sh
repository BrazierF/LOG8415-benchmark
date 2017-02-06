#!/bin/bash
# Indique au système que l'argument qui suit est le programme utilisé pour exécuter ce fichier
# En règle générale, les "#" servent à mettre en commentaire le texte qui suit comme ici

sudo apt-get update
sudo apt-get upgrade
sudo apt-get update
sudo apt-get -y install sysbench
sudo apt-get -y install bonnie++
sudo apt-get -y install stress-ng
sudo apt-get -y install hdparm
sudo apt-get -y install speedtest-cli
exit 0
