REM --- EXECUTION ---
echo [1] Activation de l'environnement virtuel...
REM L'appel a CALL permet d'exécuter le script d'activation dans la console actuelle
CALL .\op_dl\Scripts\activate.bat

REM Vérifie si le fichier principal existe
IF NOT EXIST "opening_downloader.py" (
    echo [ERREUR] Le script principal 'opening_downloader.py' est introuvable.
    goto End
)

REM Vérifie si 'python' est disponible
where python >nul 2>nul
IF %ERRORLEVEL%==0 (
    echo [INFO] Exécution avec 'python'
    CALL python opening_downloader.py
) ELSE (
    REM Vérifie si 'py' est disponible
    where py >nul 2>nul
    IF %ERRORLEVEL%==0 (
        echo [INFO] Exécution avec 'py'
        CALL py opening_downloader.py
    ) ELSE (
        echo [ERREUR] Ni 'python' ni 'py' n'ont été trouvés. Impossible d'exécuter le script.
        goto End
    )
)
