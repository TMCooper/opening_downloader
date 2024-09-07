def verification(final_title, title_en, title_jap, anime_number):

    if title_jap is not None:

        v_anime_name = str(title_jap) in final_title
        if v_anime_name is None:
             v_anime_name = title_jap
        v_anime_number = str(anime_number) in final_title
        if v_anime_number is None:
             v_anime_number = anime_number
    else:
        
        v_anime_name = title_en
        v_anime_name = str(title_en) in final_title
        if v_anime_name is None:
             v_anime_name = title_en
        v_anime_number = str(anime_number) in final_title

    return v_anime_name, v_anime_number