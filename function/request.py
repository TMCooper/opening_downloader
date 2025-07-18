from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def request(op_convert, anime_number):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.198 Safari/537.36"
        )
        page = await context.new_page()

        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', { get: () => undefined });")

        url = f'https://www.youtube.com/results?search_query={op_convert}+opening+{anime_number}'
        await page.goto(url)

        try:
            # On donne un délai court (5s) car la fenêtre apparaît très vite ou pas du tout.
            await page.locator("button[aria-label*='Accept all']").click(timeout=5000)
            print("Cookie consent accepted.")
        except Exception:
            # Si le bouton n'est pas trouvé après 5 secondes, on continue.
            print("Cookie consent dialog not found, proceeding...")

        # 2. Attendre que les résultats de la recherche soient réellement chargés.
        # 'ytd-video-renderer' est l'élément qui contient chaque vidéo dans les résultats.
        # C'est un bien meilleur indicateur que 'body'.
        try:
            await page.wait_for_selector('ytd-video-renderer', timeout=15000)
            print("Video results are loaded.")
        except Exception:
            print("Could not find video results on the page. The page might be empty or structured differently.")
            await browser.close()
            # Retourne une soupe vide si aucun résultat n'est trouvé
            return BeautifulSoup("", 'html.parser')

        # --- FIN DES MODIFICATIONS ---

        page_source = await page.content()
        await browser.close()

        soup = BeautifulSoup(page_source, 'html.parser')
        return soup

# def request_sp(op_convert, anime_number):

#     anime_number = " "
#     url = f'https://www.youtube.com/results?search_query={op_convert}+opening+{anime_number}special'
#     service = Service(executable_path='chromedriver-win64/chromedriver.exe')
#     driver = webdriver.Chrome(service=service)
#     driver.get(url)

#     # Attendre que la page soit complètement chargée
#     driver.implicitly_wait(5)  # Attendre jusqu'à 5 secondes pour le chargement complet

#     # Extraire le HTML rendu
#     html_content = driver.page_source

#     # Fermer le navigateur
#     driver.quit()

#     # Analyser le HTML avec BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')
    
#     return soup