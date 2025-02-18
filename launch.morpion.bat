@echo off

:: Vérifier si Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installé. Installation en cours...
    :: Téléchargement de l'installateur Python
    set URL=https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe
    set INSTALLER=%TEMP%\python-installer.exe
    powershell -Command "Invoke-WebRequest -Uri %URL% -OutFile %INSTALLER%"
    :: Lancer l'installateur
    start /wait %INSTALLER% /quiet InstallAllUsers=1 PrependPath=1
    echo Python installé avec succès.
) else (
    echo Python est déjà installé.
)

:: Vérifier si pip est installé
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip n'est pas installé. Installation en cours...
    python -m ensurepip --upgrade
) else (
    echo pip est déjà installé.
)

:: Vérifier si l'environnement virtuel existe
if not exist "env" (
    echo Environnement virtuel non trouvé. Création en cours...
    python -m venv env
) else (
    echo L'environnement virtuel existe déjà.
)

:: Activer l'environnement virtuel
echo Activation de l'environnement virtuel...
call env\Scripts\activate.bat

:: Installer les dépendances à partir de requirements.txt si le fichier existe
if exist "requirements.txt" (
    echo Installation des dépendances depuis requirements.txt...
    pip install -r requirements.txt
) else (
    echo Aucun fichier requirements.txt trouvé.
)

:: Lancer le programme prg\dist\morpion.exe dans un terminal cmd
echo Lancement du programme prg\dist\morpion.exe...
start cmd /K "prg\dist\morpion.exe"

:: Fin du script
echo Installation et lancement terminés avec succès!
