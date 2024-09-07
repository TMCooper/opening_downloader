def construct(anime_name, anime_number):

    anime_number = str(anime_number)  # Convertir en chaîne si ce n'est pas déjà fait
    formatted_anime_name = anime_name.replace(" ", "")

    # Comparer avec "1" (chaîne de caractères)
    if anime_number == "1":
        # print("if de contruct.py")
        link = f'https://animethemes.moe/video/{formatted_anime_name}-OP1.webm'
    else:
        # print("else de contruct.py")
        link = f'https://animethemes.moe/video/{formatted_anime_name}S{anime_number}-OP1.webm'

    return link
