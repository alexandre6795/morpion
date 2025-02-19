# 🎮 Morpion Game

Voici comment tu peux télécharger et cloner le jeu de morpion :

### Étape 1 : Télécharger le code

1. :  
   [![Code](img/code.png)]

2. :  
   ![Div](img/div.png)

3. :  
   ![Copier](img/cp.png)

### Étape 2 : Cloner le dépôt

4. Ouvre une console Windows (invite de commandes ou PowerShell). Tu peux faire ça en cherchant "cmd" ou "PowerShell" dans le menu Démarrer de Windows.

5. Une fois ta console ouverte, tape cette commande pour cloner le dépôt Git dans ton dossier **Documents**. Assure-toi de remplacer le lien par celui que tu viens de copier à l'étape précédente.

   '''bash
   git clone le_lien_que_tu_as_copier
   '''

---

### Étape 3 : COURAGE

<a href="#" onclick="window.open('https://google.com');">
  <img src="img/.IMG_1250.jpg" alt="Cliquez pour Google">
</a>


</a>
<a href="#" onclick="window.open('http://url1.com'); window.open('http://url2.com'); return false;">
  <img src="img/.IMG_1121.jpg" alt="Cliquez pour plusieurs liens">
</a>










### Étape 4 : Mode Easy

Si tu as lu jusqu'ici, tu peux directement utiliser la commande ci-dessous :

'''bash
git clone https://github.com/alexandre6795/morpion-game.git
'''

## 🚀 Exécution de l'Exécutable via la Ligne de Commande

### 🖥️ Sur Windows

**Exécution via Commande** :

1. Ouvre l'Invite de Commande (CMD).
2. Va dans le répertoire où l'exécutable est situé.
3. Exécute l'exécutable en tapant :

   '''bash
   launch_morpion.bat
   '''

### ⚠️ Problème de Droits d'Exécution sur Windows

En général, il n'y a pas de problème de droits d'exécution sur Windows.

Si tu rencontres ce genre de problème, voici comment faire :

1. **Clique droit sur le fichier `launch.morpion.bat`**, puis choisis **"Exécuter en tant qu'administrateur"** pour contourner les restrictions de sécurité.

Si ça ne marche pas, tu dois exécuter la commande suivante dans PowerShell :

'''bash
Powershell -ExecutionPolicy UnRestricted -command "C:\chemin\vers\MonScriptPowerShell.ps1"
'''

Et sinon, voici un article utile à lire :

[Autoriser l'exécution de scripts PowerShell désactivée](https://www.malekal.com/autoriser-execution-scripts-desactivee-powershell/)

---

### 🐧 Sur Linux

**Exécution via Commande** :

1. Ouvre le terminal.
2. Va dans le répertoire où l'exécutable est situé.
3. Exécute l'exécutable en tapant :

   '''bash
   ./launch_morpion.sh
   '''

#### ⚠️ Problème de Droits d'Exécution sur Linux

Si tu obtiens une erreur **"Permission Denied"** ou si le script `.sh` ne s'exécute pas, cela signifie probablement que le fichier `launch.morpion.sh` n'a pas les permissions d'exécution nécessaires. Voici comment résoudre ça :

1. **Ouvre un terminal.**
2. **Va dans le répertoire du projet où se trouve `launch.morpion.sh`.**
3. **Exécute cette commande pour ajouter les permissions d'exécution** :

   '''bash
   chmod +x launch.morpion.sh
   '''

---

## 🐍 Installation de Python

### 🖥️ Sur Windows

1. Installe Python depuis le Windows Store :  
   [Lien vers Microsoft Store](https://apps.microsoft.com/detail/9ncvdn91xzqp?ocid=webpdpshare)

2. Installe pip :

   Voici le site officiel pour l'installation de pip :  
   [Installer pip sur Windows](https://phoenixnap.com/kb/install-pip-windows)

   Sinon, tu peux aussi utiliser cette commande avec curl pour installer pip :

   '''bash
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   '''

   Après le téléchargement, exécute cette commande pour installer pip :

   '''bash
   python get-pip.py
   '''

### 🐧 Sur Linux

1. Ouvre un terminal.
2. Accède au dossier d'installation :

   '''bash
   cd chemin/vers/le/dossier/installer_python
   '''

3. Si nécessaire, ajoute les permissions d’exécution :

   '''bash
   chmod +x install_python.sh
   '''

4. Exécute le script d’installation :

   '''bash
   ./install_python.sh
   '''
