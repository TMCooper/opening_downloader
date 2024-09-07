from function.convert import *
from function.title_validation import *

def title_browse_in_en(soup, anime_en):
    
    selected_video_link_en = None
    title_en = None


    for video in soup.find_all('a', href=True):
            aria_label = video.get('aria-label')
            title = video.get('title')
            href = video.get('href')

            if aria_label and title and href:                   
                # Extraire la durée de la vidéo avec une expression régulière
                duration_str = aria_label
                duration_seconds = convert_to_seconds(duration_str)

                # Vérifier si la durée est comprise entre 85 et 120 secondes (1m25s à 2m00s)
                if 85 <= duration_seconds <= 150 and is_valid_title_en(title, anime_en):
                    title_en = title
                    selected_video_link_en = f"https://www.youtube.com{href}"
                    break
                else:
                    continue
    
    return selected_video_link_en, title_en

def title_browse_in_jap(soup, anime_jap):

    selected_video_link_jap = None
    title_jap = None

    for video in soup.find_all('a', href=True):
            aria_label = video.get('aria-label')
            title = video.get('title')
            href = video.get('href')

            if aria_label and title and href:                   
                # Extraire la durée de la vidéo avec une expression régulière
                duration_str = aria_label
                duration_seconds = convert_to_seconds(duration_str)

                # Vérifier si la durée est comprise entre 85 et 120 secondes (1m25s à 2m00s)
                if 85 <= duration_seconds <= 150 and is_valid_title_en(title, anime_jap):
                    title_jap = title
                    selected_video_link_jap = f"https://www.youtube.com{href}"
                    break
                else:
                    continue
                
    return selected_video_link_jap, title_jap