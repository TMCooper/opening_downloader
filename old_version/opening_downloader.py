import requests
import os
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_OP = os.path.join(PATH, "Opening")
ERROR_N = "download_error.txt"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def main():
    try:
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

            op_convert = anime_name.replace(" ", "%20")

            # Charger la page YouTube
            url = f'https://themes.moe/list/search/{op_convert}%20{anime_number}'
            driver.get(url)

            # Attendre que la page soit complètement chargée
            driver.implicitly_wait(5)  # Attendre jusqu'à 5 secondes pour le chargement complet
            links = driver.find_elements('xpath', '//tbody/tr[1]/td[2]/a')

            for link in links:
                print(link.get_attribute('href'))
                save_file(requests.get(link.get_attribute('href'), headers=headers).content, link.get_attribute('href'))


            # Fermer le navigateur
            driver.quit()

    except KeyboardInterrupt:
        driver.quit()
        print(languages[lang]["interrupt_message"])

def save_file(file_content, url):
    filename = url.split('/')[-1].split('?')[0]
    filepath = os.path.join('videos', filename)
    if not os.path.exists("videos"):
        os.makedirs('videos')
        os.remove(filepath)
    try:
        with open(filepath, 'wb') as f:
            f.write(file_content)
        return f"Fichier enregistré sous {PATH_OP+filename}"
    except Exception as e:
        return f"Erreur lors de la sauvegarde du fichier {filename}: {e}"


if __name__ == "__main__":
    main()