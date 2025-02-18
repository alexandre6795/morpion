# Vérifier si Python est déjà installé
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Python n'est pas installé, installation en cours..."

    # Définir l'URL et le chemin de l'installateur
    $url = "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe"
    $installer = "$env:TEMP\python-installer.exe"

    # Télécharger l'installateur Python
    Write-Host "Téléchargement de Python depuis $url..."
    Invoke-WebRequest -Uri $url -OutFile $installer

    # Lancer l'installateur avec les options silencieuses
    Write-Host "Installation de Python en cours..."
    Start-Process -FilePath $installer -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

    # Supprimer l'installateur après l'installation
    Remove-Item -Path $installer -Force

    # Vérifier à nouveau si Python est installé
    $python = Get-Command python -ErrorAction SilentlyContinue
    if (-not $python) {
        Write-Host "❌ Échec de l'installation de Python."
        exit
    }

    Write-Host "✅ Python installé avec succès."
} else {
    Write-Host "✅ Python est déjà installé."
}

# Vérifier si pip est installé
$pip = Get-Command pip -ErrorAction SilentlyContinue
if (-not $pip) {
    Write-Host "pip n'est pas installé, installation en cours..."
    python -m ensurepip --upgrade

    # Vérifier si pip est bien installé après la commande
    $pip = Get-Command pip -ErrorAction SilentlyContinue
    if ($pip) {
        Write-Host "✅ pip installé avec succès."
    } else {
        Write-Host "❌ Échec de l'installation de pip."
        exit
    }
} else {
    Write-Host "✅ pip est déjà installé."
}

Write-Host "🎉 Installation terminée avec succès!"
