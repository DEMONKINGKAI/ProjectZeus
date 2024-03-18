import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Git\\usr\\bin\\notepad",
    'discord': "C:\\Users\\666de\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'spotify': "C:\\Users\\666de\\AppData\\Local\\Microsoft\\WindowsApps" \
               "\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe"
}

def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_spotify():
    os.startfile(paths['spotify'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])