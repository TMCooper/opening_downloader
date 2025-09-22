REM --- EXECUTION ---
echo [1] Activation de l'environnement virtuel...
REM L'appel a CALL permet d'executer le script d'activation dans la console actuelle
CALL .\op_dl\Scripts\activate.bat

REM Verifie si le fichier main.py existe
IF NOT EXIST "opening_downloader.py" (
    echo [ERREUR] Le script principal 'opening_downloader.py' est introuvable.
    goto End
)

CALL python opening_downloader.py