from function.anime_choice import *
from function.construct import *
from function.convert import *
from function.downloader import *
from function.finder import *
from function.request import *
from function.title_validation import *
from function.trad import *
from function.verification import *

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_OP = os.path.join(PATH, "Opening")
ERROR_N = "download_error.txt"

def main():

    try :
        # special = 'spécial'
        valid_languages = ["en", "fr"]

        print(f"Available languages: {', '.join(valid_languages).upper()}")
        lang = input("Please select your language: ").lower()

        while lang not in valid_languages:
            print(f"\nInvalid selection. Please choose one of the following: {', '.join(valid_languages).upper()}")
            lang = input("Please select a valid language: ").lower()
        
        with open('languages.json', 'r') as lang_file:
            languages = json.load(lang_file)

        print(languages[lang]["quit_instruction"])
        print(languages[lang]["welcome_message"])
        file_name = input(languages[lang]["filename_prompt"])

        if file_name in ["q", "Q"]:
            print(languages[lang]["exit_message"])
            exit()

        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        with open(ERROR_N, "w") as error:
            error.write(languages[lang]["log_error_message"])
        
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
            try:
                op_convert = anime_name.replace(" ", "+") #remplace les espace par des + pour construire le lien plus tard dans la fonction request

                soup = request(op_convert, anime_number) #recupère l'html grace a la fonction request
                anime_jap = trad_jap(anime_name) #traduit le nom de l'animer en japonais kanji
                    
                anime_en = trad_en(anime_name) #traduit le nom de l'animer en anglais
                subprocess.run('cls', shell=True)

                selected_video_link_en, title_en = title_browse_in_en(soup, anime_en) #cherche les potentiel correspondance 
                selected_video_link_jap, title_jap = title_browse_in_jap(soup, anime_jap)

                final_link, final_title = choice(selected_video_link_jap, selected_video_link_en, title_jap, title_en)

                v_anime_name, v_anime_number = verification(final_title, title_en, title_jap, anime_number)

                if v_anime_number & v_anime_name is not True :
                    if anime_number == "1":
                        YoutubeDownloader(final_link, final_title, lang, PATH_OP, ERROR_N)

                    else:        
                        link = construct(anime_name, anime_number)
                        print(f'second link : {link}')
                        save_file(link, anime_name, anime_number, lang, PATH_OP, ERROR_N)
                        
                else:
                    YoutubeDownloader(final_link, final_title, lang, PATH_OP, ERROR_N)

            except TypeError:
                with open(ERROR_N, "a", encoding='utf8') as error:
                    error.write(languages[lang]["TypeError_None"].format(anime_name=anime_name, anime_number=anime_number))
                print((languages[lang]["TypeError_None"].format(anime_name=anime_name, anime_number=anime_number)))
                continue
        
        source_folder = PATH_OP
        convert_all_webm_in_folder(source_folder)

            # if 'spécial' in lines or 'special' in lines:                
            #     op_convert = anime_name.replace(" ", "+") #remplace les espace par des + pour construire le lien plus tard dans la fonction request
            #     link_found = special_download(op_convert, anime_name, lang)
            #     if link_found is None:
            #         with open(ERROR_N, "a", encoding='utf8') as error:
            #             error.write(languages[lang]["write_error"].format(anime_name=anime_names, url = link_found))
            #         print(languages[lang]["no_video_found"])
            #         continue
            #     else:
            #         link_found = YoutubeDownloader(link_found, anime_name, lang)
            # else:
            #     print("else")
    except KeyboardInterrupt:
        print(languages[lang]["interrupt_message"])
    
    except FileNotFoundError:
        print(languages[lang]["file_not_found"])

if __name__ == "__main__":
    main()