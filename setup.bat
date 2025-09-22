@echo off
REM Met un titre a la fenetre de la console
title Lanceur d'application Python

REM --- VERIFICATIONS ---
REM Vérifie si le dossier de l'environnement virtuel existe
IF NOT EXIST ".\op_dl\Scripts\activate.bat" (
    echo [INFO] Environnement virtuel 'op_dl' introuvable. Tentative de création...

    REM Teste si 'python' est dispo
    where python >nul 2>nul
    IF %ERRORLEVEL%==0 (
        echo [INFO] Utilisation de 'python' pour créer le venv.
        python -m venv op_dl
    ) ELSE (
        REM Teste si 'py' est dispo
        where py >nul 2>nul
        IF %ERRORLEVEL%==0 (
            echo [INFO] Utilisation de 'py -3.11' pour créer le venv.
            py -3.11 -m venv op_dl
        ) ELSE (
            echo [ERREUR] Ni 'python' ni 'py' n'ont été trouvés. Veuillez installer Python.
            exit /b 1
        )
    )
)

REM Verifie si le fichier requirements.txt existe
IF NOT EXIST "requirements.txt" (
    echo [ERREUR] Le fichier 'requirements.txt' est introuvable.
    goto End
)

REM Verifie si le fichier main.py existe
IF NOT EXIST "opening_downloader.py" (
    echo [ERREUR] Le script principal 'opening_downloader.py' est introuvable.
    goto End
)

REM --- EXECUTION ---
echo [1/3] Activation de l'environnement virtuel...
REM L'appel a CALL permet d'executer le script d'activation dans la console actuelle
CALL .\op_dl\Scripts\activate.bat

echo.
echo [2/3] Installation des dependances depuis requirements.txt...
pip install -r requirements.txt
playright install

REM Verifie si l'installation a reussi
IF %ERRORLEVEL% NEQ 0 (
    echo [ERREUR] L'installation des dependances a echoue.
    goto End
)

echo.
echo --------------------------------------------------
echo.

:End
echo Le script est termine. Appuyez sur une touche pour quitter.
REM pause permet de garder la fenetre ouverte pour voir le resultat ou les erreurs
pause >nul