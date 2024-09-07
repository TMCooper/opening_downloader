from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from bs4 import BeautifulSoup


def request(op_convert, anime_number):
    url = f'https://www.youtube.com/results?search_query={op_convert}+opening+{anime_number}'

    service = Service(executable_path='chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Attendre que la page soit complètement chargée
    driver.implicitly_wait(5)  # Attendre jusqu'à 5 secondes pour le chargement complet

    # Extraire le HTML rendu
    html_content = driver.page_source

    # Fermer le navigateur
    driver.quit()

    # Analyser le HTML avec BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    return soup