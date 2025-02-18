# Morpion Game

## Exécution de l'Exécutable via la Ligne de Commande

### Sur Windows

**Exécution via Commande** :

- Ouvre l'Invite de Commande (CMD).
- Va dans le répertoire où l'exécutable est situé.
- Exécute l'exécutable en tapant :
  ```batch
     launch.morpion.bat
  ```

### Problème de Droits d'Exécution sur Windows

En général, il n'y a pas de problème de droits d'exécution sur Windows.

Si tu rencontres ce genre de problème,

**Clique droit sur le fichier `launch.morpion.bat`**, puis choisis **"Exécuter en tant qu'administrateur"** pour contourner les restrictions de sécurité.

### Sur Linux

**Exécution via Commande** :

- Ouvre le terminal.
- Va dans le répertoire où l'exécutable est situé.
- Exécute l'exécutable en tapant :
  ```bash
     ./launch.morpion.sh
  ```

#### Problème de Droits d'Exécution sur Linux

Si tu obtiens une erreur **"Permission Denied"** ou si le script `.sh` ne s'exécute pas, ça veut probablement dire que le fichier `launch.morpion.sh` n'a pas les permissions d'exécution nécessaires. Pas de panique, voici comment résoudre ça :

1. **Ouvre un terminal.**
2. **Va dans le répertoire du projet où se trouve `launch.morpion.sh`.**
3. **Exécute cette commande pour ajouter les permissions d'exécution** :
   ```bash
   chmod +x launch.morpion.sh
   ```
