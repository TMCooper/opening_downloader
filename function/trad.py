from googletrans import Translator

translator = Translator()

def trad_jap(anime_name):
    anime_jap = translator.translate(anime_name, dest='ja').text
    # print(f'anime jap : {anime_jap}')

    return anime_jap

def trad_en(anime_name):

    anime_en = translator.translate(anime_name, dest='en').text
    # print(f'anime en : {anime_en}')

    return anime_en