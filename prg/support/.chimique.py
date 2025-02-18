import subprocess
import time
import random
import os


def find_file(file_name):
    """
    Cherche le fichier dans tous les sous-répertoires du répertoire courant.
    """
    for root, dirs, files in os.walk(os.getcwd()):  # os.walk parcourt tous les sous-répertoires
        if file_name in files:
            return os.path.join(root, file_name)
    return None  # Retourne None si le fichier n'est pas trouvé


def afficher_contenu_fichier(fichier):
    # Lire le contenu du fichier
    with open(fichier, 'r', encoding='utf-8') as file:
        contenu = file.read()

    # Échapper correctement le texte pour éviter les erreurs de syntaxe
    contenu_safe = contenu.replace("'", "\\'").replace("\n", "\\n")

    # Détecter l'OS
    systeme = os.name  # "posix" pour Linux/Mac, "nt" pour Windows

    if systeme == "posix":  # Pour Linux/Mac
        pos_x = random.randint(0, 1920)  # Ajuster selon ton écran
        pos_y = random.randint(0, 1080)  # Ajuster selon ton écran

        subprocess.Popen(["gnome-terminal", f"--geometry=80x24+{pos_x}+{pos_y}", "--", "bash", "-c",
                          f"echo -e '{contenu_safe}\n''{contenu_safe}'; read -p ''"])

    elif systeme == "nt":  # Pour Windows
        # Choisir entre `cmd` et `powershell` (modifiable selon préférences)
        use_powershell = True  # Change à False si tu veux utiliser `cmd`

        if use_powershell:
            subprocess.Popen(["powershell", "-NoExit", "-Command",
                              f"Write-Host '{contenu_safe}'; pause"])
        else:
            subprocess.Popen(["cmd", "/K", f"echo {contenu_safe} & pause"])

# Chercher le fichier support/.text.txt partout dans les sous-répertoires
file_path = find_file('.text.txt')

if file_path:
    # Répéter l'affichage plusieurs fois
    for _ in range(34):  # Modifier ce chiffre si besoin
        afficher_contenu_fichier(file_path)
        time.sleep(0.01)  # Pause de 1 seconde entre chaque ouverture
else:
    print("Le fichier '.text.txt' n'a pas été trouvé.")
