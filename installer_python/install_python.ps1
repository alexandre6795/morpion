# Vérifier si Python est déjà installé
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Python n'est pas installé, installation en cours..."

    # Téléchargement de l'installateur Python
    $url = "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe"
    $installer = "$env:TEMP\python-installer.exe"
    Invoke-WebRequest -Uri $url -OutFile $installer

    # Lancer l'installateur avec les options pour ajouter Python au PATH
    Start-Process -FilePath $installer -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

    # Vérifier si Python a été correctement installé
    $python = Get-Command python -ErrorAction SilentlyContinue
    if ($python) {
        Write-Host "Python installé avec succès."
    } else {
        Write-Host "Échec de l'installation de Python."
        exit
    }
}

# Vérifier si pip est installé
$pip = Get-Command pip -ErrorAction SilentlyContinue
if (-not $pip) {
    Write-Host "pip n'est pas installé, installation en cours..."

    # Installer pip
    python -m ensurepip --upgrade
}

# Vérifier si requirements.txt existe
if (Test-Path "requirements.txt") {
    Write-Host "Installation des dépendances depuis requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "Aucun fichier requirements.txt trouvé dans le répertoire."
}

Write-Host "Installation terminée avec succès!"
