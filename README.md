# 🎮 Morpion Game

Voici comment tu peux télécharger et cloner le jeu de morpion :

### Étape 1 : Télécharger le code
1. Clique sur l'image ci-dessous pour accéder au dépôt Git du projet :  
   [![Code](img/code.png)](https://www.google.fr)


### Étape 2 : Accéder au fichier source
2. Après ça, clique sur l'image suivante pour aller à la section du code ou fichier à télécharger :  
   ![Div](img/div.png)

### Étape 3 : Copier le lien du projet
3. Ensuite, clique sur l'image qui suit pour copier le lien du dépôt Git :  
   ![Copier](img/cp.png)

### Étape 4 : Cloner le dépôt
4. Ouvre une console Windows (invite de commandes ou PowerShell). Tu peux faire ça en cherchant "cmd" ou "PowerShell" dans le menu Démarrer de Windows.

5. Une fois ta console ouverte, tape cette commande pour cloner le dépôt Git dans ton dossier **Documents**. Assure-toi de remplacer le lien par celui que tu viens de copier à l'étape précédente.

   ```bash
   git clone https://github.com/alexandre6795/morpion-game.git


## 🚀 Exécution de l'Exécutable via la Ligne de Commande

### 🖥️ Sur Windows

**Exécution via Commande** :

1. Ouvre l'Invite de Commande (CMD).
2. Va dans le répertoire où l'exécutable est situé.
3. Exécute l'exécutable en tapant :
    ```batch
    launch.morpion.bat
    ```

### ⚠️ Problème de Droits d'Exécution sur Windows

En général, il n'y a pas de problème de droits d'exécution sur Windows.

Si tu rencontres ce genre de problème, voici comment faire :

1. **Clique droit sur le fichier `launch.morpion.bat`**, puis choisis **"Exécuter en tant qu'administrateur"** pour contourner les restrictions de sécurité.

---

### 🐧 Sur Linux

**Exécution via Commande** :

1. Ouvre le terminal.
2. Va dans le répertoire où l'exécutable est situé.
3. Exécute l'exécutable en tapant :
    ```bash
    ./launch.morpion.sh
    ```

#### ⚠️ Problème de Droits d'Exécution sur Linux

Si tu obtiens une erreur **"Permission Denied"** ou si le script `.sh` ne s'exécute pas, cela signifie probablement que le fichier `launch.morpion.sh` n'a pas les permissions d'exécution nécessaires. Voici comment résoudre ça :

1. **Ouvre un terminal.**
2. **Va dans le répertoire du projet où se trouve `launch.morpion.sh`.**
3. **Exécute cette commande pour ajouter les permissions d'exécution** :
    ```bash
    chmod +x launch.morpion.sh
    ```

---

## 🐍 Installation de Python

### 🖥️ Sur Windows

1. Ouvre PowerShell en mode administrateur (clic droit → "Exécuter en tant qu'administrateur").
2. Accède au dossier d'installation :
    ```bash
    cd chemin\vers\le\dossier\installer_python
    ```
3. Exécute le script d’installation :
    ```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force
    .\install_python.ps1
    ```

---

### 🐧 Sur Linux

1. Ouvre un terminal.
2. Accède au dossier d'installation :
    ```bash
    cd chemin/vers/le/dossier/installer_python
    ```
3. Si nécessaire, ajoute les permissions d’exécution :
    ```bash
    chmod +x install_python.sh
    ```
4. Exécute le script d’installation :
    ```bash
    ./install_python.sh
    ```
