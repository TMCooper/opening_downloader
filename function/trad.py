from googletranslate import translate

def trad_jap(anime_name):
    anime_jap = translate(f'{anime_name}', 'ja')
    # print(f'anime jap : {anime_jap}')

    return anime_jap

def trad_en(anime_name):

    anime_en  = translate(f'{anime_name}', 'en') 
    # print(f'anime en : {anime_en}')

    return anime_en