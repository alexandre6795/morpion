import subprocess
import time
import random
import os
import shutil

r = 34  # Nombre d'itérations des boucles


def find_file(file_name):
    """Cherche le fichier dans tous les sous-répertoires du répertoire courant."""
    for root, dirs, files in os.walk(os.getcwd()):
        if file_name in files:
            return os.path.join(root, file_name)
    return None  # Retourne None si le fichier n'est pas trouvé


def convertir_fichier_windows(original, converti):
    """Convertit un fichier texte au format Windows (CRLF)."""
    with open(original, 'r', encoding='utf-8') as f:
        contenu = f.read()

    with open(converti, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(contenu)


def afficher_contenu_fichier(fichier, offset_x, offset_y):
    """Affiche le contenu du fichier dans un terminal."""
    with open(fichier, 'r', encoding='utf-8') as file:
        contenu = file.read()

    # Échapper correctement le texte pour éviter les erreurs de syntaxe
    contenu_safe = contenu.replace("'", "\\'").replace("\n", "\\n")

    systeme = os.name  # "posix" pour Linux/Mac, "nt" pour Windows

    if systeme == "posix":  # Linux/Mac
        pos_x = random.randint(0, 1920) + offset_x
        pos_y = random.randint(0, 1080) + offset_y

        subprocess.Popen(["gnome-terminal", f"--geometry=80x24+{pos_x}+{pos_y}", "--", "bash", "-c",
                          f"echo -e '{contenu_safe}\n{contenu_safe}'; read -p ''"])

    elif systeme == "nt":  # Windows
        subprocess.Popen(["cmd", "/c", "start", "cmd", "/K",
                          f"mode con: cols=120 lines=40 && echo {contenu_safe} & pause"])
    else:
        print("Système d'exploitation non pris en charge.")


def afficher_image(image_path):
    """Affiche l'image avec le programme par défaut."""
    systeme = os.name

    if systeme == "posix":  # Linux
        subprocess.Popen(["eog", image_path])

    elif systeme == "nt":  # Windows
        subprocess.Popen(["start", image_path], shell=True)


# Trouver les fichiers originaux
file_text1 = find_file('.text1.txt')
file_text2 = find_file('.text2.txt')
file_image = find_file('.chimique.jpeg')

systeme = os.name

if systeme == "posix":  # Si on est sous Linux
    if all([file_text1, file_text2, file_image]):  # Vérifier que tous les fichiers existent
        offset_x = 0
        offset_y = 0

        # Première boucle (text1)
        for i in range(r):
            afficher_contenu_fichier(file_text1, offset_x, offset_y)
            time.sleep(0.01)
            afficher_image(file_image)

            if (i + 1) % 5 == 0:
                offset_x += 200
                offset_y += 200

        time.sleep(2)  # Pause entre les deux boucles

        # Deuxième boucle (text2)
        offset_x = 0
        offset_y = 0
        for i in range(r):
            afficher_contenu_fichier(file_text2, offset_x, offset_y)
            time.sleep(0.01)
            afficher_image(file_image)

            if (i + 1) % 5 == 0:
                offset_x += 200
                offset_y += 200
    else:
        print("Un ou plusieurs fichiers '.text1.txt', '.text2.txt' ou 'image.jpeg' n'ont pas été trouvés.")

elif systeme == "nt":  # Si on est sous Windows
    if all([file_text1, file_text2, file_image]):
        # Renommer et convertir les fichiers en format Windows
        file_text1_win = file_text1.replace(".txt", "_windows.txt")
        file_text2_win = file_text2.replace(".txt", "_windows.txt")

        # Vérification si les fichiers avec les nouveaux noms existent déjà
        if not os.path.exists(file_text1_win):
            convertir_fichier_windows(file_text1, file_text1_win)
        else:
            pass

        if not os.path.exists(file_text2_win):
            convertir_fichier_windows(file_text2, file_text2_win)
        else:
            pass
        offset_x = 0
        offset_y = 0

        # Première boucle (text1_windows)
        for i in range(r):
            afficher_contenu_fichier(file_text1_win, offset_x, offset_y)
            time.sleep(0.01)
            afficher_image(file_image)

            if (i + 1) % 5 == 0:
                offset_x += 200
                offset_y += 200

        time.sleep(2)

        # Deuxième boucle (text2_windows)
        offset_x = 0
        offset_y = 0
        for i in range(r):
            afficher_contenu_fichier(file_text2_win, offset_x, offset_y)
            time.sleep(0.01)
            afficher_image(file_image)

            if (i + 1) % 5 == 0:
                offset_x += 200
                offset_y += 200

    else:
        print("Un ou plusieurs fichiers '.text1.txt', '.text2.txt' ou 'image.jpeg' n'ont pas été trouvés.")
