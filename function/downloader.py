import os
import json
import yt_dlp as youtube_dl
import subprocess
import requests
from moviepy.editor import VideoFileClip
from function.convert import *

def YoutubeDownloader(final_link, final_title, lang, PATH_OP, ERROR_N):

    with open('languages.json', 'r') as lang_file:
            languages = json.load(lang_file)

    if final_link:
        if not os.path.exists(PATH_OP):
            os.mkdir(PATH_OP)

        ID_V = final_link.split("watch?v=")[1].split("&")[0]
        video = (f'https://www.youtube.com/watch?v={ID_V}')

        yt = youtube_dl.YoutubeDL({'outtmpl': os.path.join(PATH_OP, '%(title)s.%(ext)s'),
                                   'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
                                   })
        ytv = yt.extract_info(video, download=True)
        print(languages[lang]["success_download"].format(title=final_title, path=PATH_OP))
        subprocess.run("cls", shell=True)
    else:
        with open(ERROR_N, "a", encoding='utf-8') as error:
            error.write(languages[lang]["write_error"].format(final_title=final_title, url=final_link))
        print(languages[lang]["no_video_found"])
        subprocess.run('cls', shell=True)
    

def convert_webm_to_mp4(lang, webm_file, output_folder=None):

    with open('languages.json', 'r') as lang_file:
            languages = json.load(lang_file)

    # Définir le nom du fichier de sortie avec extension mp4
    mp4_file = os.path.splitext(webm_file)[0] + ".mp4"
    
    # Si un dossier de sortie est spécifié, l'utiliser
    if output_folder:
        mp4_file = os.path.join(output_folder, os.path.basename(mp4_file))
    
    try:
        # Charger le fichier webm
        video_clip = VideoFileClip(webm_file)
        
        # Écrire le fichier de sortie en mp4
        video_clip.write_videofile(mp4_file, codec="libx264")
        
        # print(f"Conversion réussie : {mp4_file}")
        print(languages[lang]["success_convert"].format(mp4_file=mp4_file))
        
        # Supprimer le fichier .webm après une conversion réussie
        os.remove(webm_file)
        print(languages[lang]["remove_file"].format(webm_file=webm_file))
    
    except Exception as e:
        # print(f"Erreur lors de la conversion de {webm_file} : {str(e)}")
        e = str(e)
        print(languages[lang]["error_convert"].format(webm_file=webm_file, e=e))

def save_file(link, anime_name, anime_number, lang, PATH_OP, ERROR_N):
    
    with open('languages.json', 'r') as lang_file:
            languages = json.load(lang_file)    

    if not os.path.exists(PATH_OP):
            os.mkdir(PATH_OP)

    name_file = (f'/{anime_name}_S{anime_number}_OP.webm')
    path = PATH_OP+name_file
    
    try:
        # Faire une requête GET pour obtenir le contenu du fichier
        response = requests.get(link, stream=True)
        response.raise_for_status()  # Vérifie si la requête a réussi (code 200)
        
        # Ouvrir un fichier local en mode écriture binaire
        with open(path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(languages[lang]["success_download"].format(title=name_file, path = path))

    except requests.exceptions.RequestException:
        with open(ERROR_N, "a", encoding='utf-8') as error:
                    error.write(languages[lang]["write_error"].format(final_title=anime_name, url=link))
        print(languages[lang]["no_video_found"])

def las_try_save_file(link, anime_name, anime_number, lang, PATH_OP, ERROR_N, Detect):
    
    with open('languages.json', 'r') as lang_file:
            languages = json.load(lang_file)    

    if not os.path.exists(PATH_OP):
            os.mkdir(PATH_OP)

    name_file = (f'/{anime_name}_S{anime_number}_OP.webm')
    path = PATH_OP+name_file
    
    try:
        # Faire une requête GET pour obtenir le contenu du fichier
        response = requests.get(link, stream=True)
        response.raise_for_status()  # Vérifie si la requête a réussi (code 200)
        
        # Ouvrir un fichier local en mode écriture binaire
        with open(path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(languages[lang]["success_download"].format(title=name_file, path = path))

    except requests.exceptions.RequestException:
        Detect = True  # Si une erreur est détectée, on considère que le fichier n'est pas disponible

    return Detect