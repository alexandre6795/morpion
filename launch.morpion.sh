#!/bin/bash

# Vérifier si Python 3 est installé
if ! command -v python3 &>/dev/null; then
    echo "Python 3 n'est pas installé. Installation en cours..."
    sudo apt update -y
    sudo apt install python3 -y
else
    echo "Python 3 est déjà installé."
fi

# Vérifier si pip3 est installé
if ! command -v pip3 &>/dev/null; then
    echo "pip3 n'est pas installé. Installation en cours..."
    sudo apt install python3-pip -y
else
    echo "pip3 est déjà installé."
fi

# Vérifier si l'environnement virtuel existe, sinon le créer
if [ ! -d "env" ]; then
    echo "Création de l'environnement virtuel..."
    python3 -m venv env
else
    echo "L'environnement virtuel existe déjà."
fi

# Activer l'environnement virtuel
echo "Activation de l'environnement virtuel..."
source env/bin/activate

# Vérifier si le fichier requirements.txt existe et installer les dépendances
if [ -f "requirements.txt" ]; then
    echo "Installation des dépendances depuis requirements.txt..."
    pip install -r requirements.txt
else
    echo "Aucun fichier requirements.txt trouvé dans le répertoire."
fi

# Lancer le programme dans un nouveau terminal GNOME
echo "Lancement de prg/dist/morpion dans un nouveau terminal GNOME..."
gnome-terminal -- prg/dist/morpion
