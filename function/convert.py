import re
import os
import subprocess
from function.downloader import *

def convert_to_seconds(time_str):
    # Extraire minutes et secondes, et convertir en secondes
    minutes = 0
    seconds = 0
                
    # Chercher les minutes et les secondes dans la chaîne
    min_match = re.search(r'(\d+)\s*minute(?:s)?', time_str)
    sec_match = re.search(r'(\d+)\s*seconde(?:s)?', time_str)
    
    if min_match:
        minutes = int(min_match.group(1))
    if sec_match:
        seconds = int(sec_match.group(1))
    
    return minutes * 60 + seconds

def convert_all_webm_in_folder(lang, source_folder, output_folder=None):

    # Créer le dossier de sortie s'il n'existe pas
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Parcourir tous les fichiers dans le dossier source
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".webm"):
                webm_file = os.path.join(root, file)
                print(f"Conversion de : {webm_file}")
                convert_webm_to_mp4(lang, webm_file, output_folder)

    print("Conversion de tous les fichiers terminée.")
    # subprocess.run('cls', shell=True)