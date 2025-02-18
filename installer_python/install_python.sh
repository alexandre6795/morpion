#!/bin/bash

# Vérifier si Python est installé
if ! command -v python3 &>/dev/null; then
    echo "Python 3 n'est pas installé. Installation en cours..."
    sudo apt update -y
    sudo apt install -y python3 python3-venv python3-pip
else
    echo "Python 3 est déjà installé."
fi

# Vérifier si pip est installé
if ! command -v pip3 &>/dev/null; then
    echo "pip3 n'est pas installé. Installation en cours..."
    sudo apt install -y python3-pip
else
    echo "pip3 est déjà installé."
fi

echo "✅ Installation terminée avec succès !"
