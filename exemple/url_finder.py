from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re

# Met à jour le chemin vers le nouveau ChromeDriver téléchargé
service = Service(executable_path='chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Charger la page YouTube
url = "https://www.youtube.com/results?search_query=High+School+DxD+opening+1"
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
    pattern = rf'{re.escape(anime_name)}.*(Op|Opening)\s*\d*'
    return re.search(pattern, title, re.IGNORECASE)

# Nom de l'animé que nous cherchons
anime_name = "HighSchool DxD"

# Variables pour stocker les liens correspondants
selected_video_link = None

# Parcourir toutes les balises <a> et vérifier les attributs
for video in soup.find_all('a', href=True):
    aria_label = video.get('aria-label')
    title = video.get('title')
    href = video.get('href')

    if aria_label and title and href:
        print(f"Analyzing: aria_label={aria_label}, title={title}, href={href}")
        
        # Extraire la durée de la vidéo avec une expression régulière
        duration_str = aria_label
        duration_seconds = convert_to_seconds(duration_str)
        
        print(f"Extracted duration: {duration_seconds} seconds")

        # Vérifier si la durée est comprise entre 85 et 120 secondes (1m25s à 2m00s)
        if 85 <= duration_seconds <= 130 and is_valid_title(title, anime_name):
            selected_video_link = f"https://www.youtube.com{href}"
            break
        else:
            print(f"Duration or title does not match. Duration: {duration_seconds}, Title: {title}")

# Afficher le lien de la vidéo si trouvé
if selected_video_link:
    print(f"Le lien de la vidéo sélectionnée est : {selected_video_link}")
else:
    print("Aucune vidéo correspondant aux critères n'a été trouvée.")
