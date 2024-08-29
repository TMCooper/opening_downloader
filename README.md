# Opening Downloader
## if you want to use the programe

- on windows execute install.bat
- next create an .txt file with the name of you want
- execute the programme (here .opening_downloader.py)
- then precise your file.txt (if the file is on the same folder of the programme if not precise the absolute path like c:\name\of\your_file.txt) 
- then let the programme continue

## Use the good syntaxe
if you don't use an good syntaxe the programme can't find correctly your anime so be sure the
spelling of your anime is good and on your txt do that :

`- {anime_of_your_choice} --{select_the_opening_you_want_by_default_is_1}`

## Potential problem

If the code don't execute correcly and you have install Python (3.10.6 minimum) and execute install.bat juste after
the software can maybe return an error bind with ffmpeg to patch that does this :

#### install Chocolatey 

- execute powershell in administrator
- copy and pasth this line on your powershell : `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`
- after the download finish
- tap on the same powershell (or you can reopen an new but in administrator too) `choco install ffmpeg` and if the program asks you for a yes or an a then type one or the other (the result is the same)
- then you can re execute the opening_downloader.py

## Warning 

- don't use the programme to download too much opening in one time it's a big source of error and the programme is not perfect currently the programme have a 70% of success rate... the opening of oav  if they are in Kanji, Katagana or Hiragana dosen't work's currently

- about the file download_error.txt be careful between each new search the file is emptied of old links and information

## Currently up to date

to make more simple the gestion of anime to manage errors and animate not download addition of a file download_error.txt which aims to group all animate not download with the link of the request in order to see if this one exists for you on your side