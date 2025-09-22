import os
import json
import subprocess
import asyncio 
from function.__init__ import *

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_OP = os.path.join(PATH, "Opening")
ERROR_N = "download_error.txt"

async def main():

    try:
        valid_languages = ["en", "fr"]

        print(f"Available languages: {', '.join(valid_languages).upper()}")
        lang = input("Please select your language: ").lower()

        while lang not in valid_languages:
            print(f"\nInvalid selection. Please choose one of the following: {', '.join(valid_languages).upper()}")
            lang = input("Please select a valid language: ").lower()
        
        with open('languages.json', 'r', encoding='utf-8') as lang_file:
            languages = json.load(lang_file)

        print(languages[lang]["quit_instruction"])
        print(languages[lang]["welcome_message"])
        file_name = input(languages[lang]["filename_prompt"])

        if file_name.lower() == "q":
            print(languages[lang]["exit_message"])
            exit()

        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        with open(ERROR_N, "w", encoding='utf-8') as error:
            error.write(languages[lang]["log_error_message"])
        
        anime_names = []
        anime_numbers = []

        for line in lines:
            line = line.strip()
            if not line: continue # Ignorer les lignes vides
            
            if '--' in line:
                name, number = line.split('--')
                name = name.strip('- ').strip()
                number = number.strip()
            else:
                name = line.strip('- ').strip()
                number = '1'

            anime_names.append(name)
            anime_numbers.append(number)

        for anime_name, anime_number in zip(anime_names, anime_numbers):
            try:
                op_convert = anime_name.replace(" ", "+")
                
                print(f"Searching for: {anime_name} OP {anime_number}")
                
                # Appel asynchrone correct
                soup = await request(op_convert, anime_number)
                
                anime_jap = trad_jap(anime_name)
                anime_en = trad_en(anime_name)

                subprocess.run('cls', shell=True)

                selected_video_link_en, title_en = title_browse_in_en(soup, anime_en)
                selected_video_link_jap, title_jap = title_browse_in_jap(soup, anime_jap)

                final_link, final_title = choice(selected_video_link_jap, selected_video_link_en, title_jap, title_en)

                # Si une recherche YouTube a abouti
                if final_link:
                    print(f"Found YouTube video: {final_title}")
                    YoutubeDownloader(final_link, final_title, lang, PATH_OP, ERROR_N)
                
                # Sinon, on tente de télécharger depuis AnimeThemes
                else:
                    print("No suitable video found on YouTube, trying AnimeThemes.moe...")
                    link = construct(anime_name, anime_number)
                    save_file(link, anime_name, anime_number, lang, PATH_OP, ERROR_N)

            except Exception as e:
                print(f"An error occurred for {anime_name}: {e}")
                print("Trying fallback download from AnimeThemes.moe...")
                try:
                    Detect = False
                    link = construct(anime_name, anime_number)
                    Detect = las_try_save_file(link, anime_name, anime_number, lang, PATH_OP, ERROR_N, Detect)
                    
                    if Detect: # Si las_try_save_file a échoué
                        with open(ERROR_N, "a", encoding='utf-8') as error_file:
                            error_file.write(f"Failed to download for {anime_name} S{anime_number} from all sources.\n")

                except Exception as fallback_e:
                    print(f"Fallback download also failed for {anime_name}: {fallback_e}")
                    with open(ERROR_N, "a", encoding='utf-8') as error_file:
                        error_file.write(f"Fallback failed for {anime_name} S{anime_number}: {fallback_e}\n")
                
                continue
        
        source_folder = PATH_OP
        if os.path.exists(source_folder):
            convert_all_webm_in_folder(lang, source_folder)

    except KeyboardInterrupt:
        subprocess.run('cls', shell=True)
        print("\nProcess interrupted by user.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())