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


def afficher_contenu_fichier(fichier, offset_x, offset_y):
    # Lire le contenu du fichier
    with open(fichier, 'r', encoding='utf-8') as file:
        contenu = file.read()

    # Échapper correctement le texte pour éviter les erreurs de syntaxe
    contenu_safe = contenu.replace("'", "\\'").replace("\n", "\\n")

    # Détecter l'OS
    systeme = os.name  # "posix" pour Linux/Mac, "nt" pour Windows

    if systeme == "posix":  # Pour Linux/Mac
        pos_x = random.randint(0, 1920) + offset_x  # Ajuster selon l'offset
        pos_y = random.randint(0, 1080) + offset_y  # Ajuster selon l'offset

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


def afficher_image(image_path):
    systeme = os.name  # "posix" pour Linux/Mac, "nt" pour Windows

    if systeme == "posix":  # Pour Linux
        # Utiliser `eog` (Eye of Gnome) pour afficher l'image
        subprocess.Popen(["eog", image_path])

    elif systeme == "nt":  # Pour Windows
        subprocess.Popen(["start", image_path], shell=True)  # Ouvrir avec le programme par défaut


# Chercher les fichiers .text1.txt, .text2.txt, et l'image .jpeg partout dans les sous-répertoires
file_paths = [find_file('.text1.txt'), find_file('.text2.txt'), find_file('.chimique.jpeg')]

# Vérifier si tous les fichiers ont été trouvés
if None not in file_paths:
    offset_x = 0  # Décalage initial
    offset_y = 0  # Décalage initial
    
    # Première boucle pour .text1.txt
    for i in range(34):  # Modifier ce chiffre si besoin
        afficher_contenu_fichier(file_paths[0], offset_x, offset_y)
        time.sleep(0.01)  # Pause de 0.01 seconde entre chaque ouverture

        # Afficher l'image après chaque itération de la boucle
        afficher_image(file_paths[2])

        # Tous les 5 lancements, augmenter le décalage aléatoire de 200
        if (i + 1) % 5 == 0:
            offset_x += 200
            offset_y += 200

    # Pause entre les deux boucles
    time.sleep(5)

    # Deuxième boucle pour .text2.txt
    offset_x = 0  # Réinitialiser le décalage
    offset_y = 0  # Réinitialiser le décalage
    for i in range(34):  # Modifier ce chiffre si besoin
        afficher_contenu_fichier(file_paths[1], offset_x, offset_y)
        time.sleep(0.01)  # Pause de 0.01 seconde entre chaque ouverture

        # Afficher l'image après chaque itération de la boucle
        afficher_image(file_paths[2])

        # Tous les 5 lancements, augmenter le décalage aléatoire de 200
        if (i + 1) % 5 == 0:
            offset_x += 200
            offset_y += 200

else:
    print("Un ou plusieurs fichiers '.text1.txt', '.text2.txt' ou 'image.jpeg' n'ont pas été trouvés.")
