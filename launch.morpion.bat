@echo off
cd /d "%~dp0"

:: Vérifier si Python est installé
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python 3 n'est pas installé. Installation requise !
    exit /b
) else (
    echo Python 3 est déjà installé.
)

:: Vérifier si pip est installé
python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo pip n'est pas installé. Installation en cours...
    python -m ensurepip
) else (
    echo pip est déjà installé.
)

:: Vérifier si tkinter est disponible
python -c "import tkinter" >nul 2>nul
if %errorlevel% neq 0 (
    echo tkinter n'est pas installé. Veuillez l'installer manuellement.
    exit /b
) else (
    echo tkinter est déjà installé.
)

:: Vérifier si l'environnement virtuel existe, sinon le créer
if not exist env (
    echo Création de l'environnement virtuel...
    python -m venv env
) else (
    echo L'environnement virtuel existe déjà.
)

:: Activer l'environnement virtuel
call env\Scripts\activate

:: Vérifier si requirements.txt existe et installer les dépendances
if exist requirements.txt (
    echo Installation des dépendances depuis requirements.txt...
    pip install -r requirements.txt
) else (
    echo ⚠️ Aucun fichier requirements.txt trouvé dans %cd% !
)

:: Lancer le programme dans un nouveau terminal
echo Lancement de prg\morpion.py dans un nouveau terminal...
start cmd /k python prg\morpion.py
