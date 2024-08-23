import re
import requests
import os
from bs4 import BeautifulSoup
import yt_dlp as youtube_dl
import subprocess
import os

PATH = os.path.dirname(os.path.abspath(__file__))
PATH_OP = os.path.join(PATH, "Opening")

def main():
    try:
        print("Pour quiter le programme tapper Q")
        opening = input("quelle est le nom de votre fichier ? : ")
        op_convert = opening.replace(" ", "+")
               
        if opening in ["q", "Q"]:
            print("Sortie du programme...")
            exit
    except KeyboardInterrupt:
        exit

if __name__ == "__main__":
    main()
