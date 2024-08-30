import re
import os
from bs4 import BeautifulSoup
import yt_dlp as youtube_dl
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
from g4f.client import Client

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_OP = os.path.join(PATH, "Opening")
ERROR_N = "download_error.txt"

client = Client()

def main():

    try:
        special = 'spécial'
        valid_languages = ["en", "fr"]

        with open('languages.json', 'r') as lang_file:
            languages = json.load(lang_file)
        
        print(f"Available languages: {', '.join(valid_languages).upper()}")
        lang = input("Please select your language: ").lower()

        while lang not in valid_languages:
            print(f"\nInvalid selection. Please choose one of the following: {', '.join(valid_languages).upper()}")
            lang = input("Please select a valid language: ").lower()
        
        with open(ERROR_N, "w") as error:
            error.write(languages[lang]["log_error_message"])

        print(languages[lang]["welcom_message"])

        print(languages[lang]["quit_instruction"])
        opening = input(languages[lang]["filename_prompt"])

        if opening in ["q", "Q"]:
                print(languages[lang]["exit_message"])
                exit()

        with open(opening, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # On crée deux listes pour stocker les noms d'animes et les chiffres
        anime_names = []
        anime_numbers = []

        # On parcourt chaque ligne du fichier
        for line in lines:
            line = line.strip()
            
            if '--' in line:
                name, number = line.split('--')
                
                name = name.strip('- ').strip()
                number = number.strip()
            else:

                name = line.strip('- ').strip()
                number = '1'

            anime_names.append(name)
            anime_numbers.append(number)

        for i in range(len(anime_names)):

            anime_name = anime_names[i]  # Définir la variable anime_name
            anime_number = anime_numbers[i]  # Définir la variable anime_number            
            
            # Met à jour le chemin vers le nouveau ChromeDriver téléchargé
            service = Service(executable_path='chromedriver-win64/chromedriver.exe')
            driver = webdriver.Chrome(service=service)
            
            op_convert = anime_name.replace(" ", "+")

            # Charger la page YouTube
            if re.search(r'\b{}\b'.format(re.escape(special)), anime_name):
                anime_number = ""
                url = f'https://www.youtube.com/results?search_query={op_convert}+opening+{anime_number}'
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": f'traduit moi cela en japonais kanji : {anime_name} \n puis affiche moi uniquement le nom de celui ci'}]
                )
                anime_name = response.choices[0].message.content.split("「")[1].split("」")[0]

            else:
                url = f'https://www.youtube.com/results?search_query={op_convert}+opening+{anime_number}'
            
            driver.get(url)

            # Attendre que la page soit complètement chargée
            driver.implicitly_wait(5)  # Attendre jusqu'à 5 secondes pour le chargement complet

            # Extraire le HTML rendu
            html_content = driver.page_source

            # Fermer le navigateur
            driver.quit()

            # Analyser le HTML avec BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Fonction pour convertir le temps en secondes
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

            # Fonction pour vérifier si le titre correspond à l'animé et à un Op/Opening
            def is_valid_title(title, anime_name):
                
                if re.search(r'cover|instrumental|カバー|インストルメンタル', title, re.IGNORECASE):
                    return False
                
                pattern = rf'{re.escape(anime_name)}.*(Op|Opening|スペシャル)\s*\d*'
                return re.search(pattern, title, re.IGNORECASE)
            
            # Nom de l'animé que nous cherchons
            anime_name = anime_name

            # Variables pour stocker les liens correspondants
            selected_video_link = None

            # Parcourir toutes les balises <a> et vérifier les attributs
            for video in soup.find_all('a', href=True):
                aria_label = video.get('aria-label')
                title = video.get('title')
                href = video.get('href')

                if aria_label and title and href:                   
                    # Extraire la durée de la vidéo avec une expression régulière
                    duration_str = aria_label
                    duration_seconds = convert_to_seconds(duration_str)

                    # Vérifier si la durée est comprise entre 85 et 120 secondes (1m25s à 2m00s)
                    if 85 <= duration_seconds <= 150 and is_valid_title(title, anime_name):
                        selected_video_link = f"https://www.youtube.com{href}"
                        subprocess.run('cls', shell=True)
                        break
                    else:
                        subprocess.run('cls', shell=True)
                        continue

            # Afficher le lien de la vidéo si trouvé
            if selected_video_link:
                if not os.path.exists(PATH_OP):
                    os.mkdir(PATH_OP)

                Link = selected_video_link
                ID_V = Link.split("watch?v=")[1].split("&")[0]
                video = (f'https://www.youtube.com/watch?v={ID_V}')

                yt = youtube_dl.YoutubeDL({'outtmpl': os.path.join(PATH_OP, '%(title)s.%(ext)s'),
                                        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
                            })
                ytv = yt.extract_info(video, download=True)
                print(languages[lang]["success_download"].format(title=title, path=PATH_OP))
                subprocess.run("cls", shell=True)
            else:
                with open(ERROR_N, "a") as error:
                    error.write(languages[lang]["write_error"].format(anime_names=anime_names[i], url = url))
                print(languages[lang]["no_video_found"])
                subprocess.run('cls', shell=True)

    except KeyboardInterrupt :
        driver.quit()
        print(languages[lang]["interrupt_message"])

if __name__ == "__main__":
    main()