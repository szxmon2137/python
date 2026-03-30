from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
import os

def film():
    url = input("Podaj url:\n")
    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download()


def dzwiek():
    url = input("Podaj url:\n")
    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only()
    ys.download()

def playlista():
    url = input("Podaj url:\n")
    pl = Playlist(url)
    folder = input("Jak nazwać folder:\n")
    os.mkdir(folder)
    for video in pl.videos:
        ys = video.streams.get_audio_only()
        ys.download(folder)


print("Witaj w Pydownloderze")
print("1.Pobierz film")
print("2.Pobierz dźwięk")
print("3.Pobierz playliste(Tylko dźwięk)")
x = input("Co chcesz zrobić:\n")

match x:
    case "1":
        film()
    case "2":
        dzwiek()
    case "3":
        playlista()
    case _:
        print("Nie prawidłowa odpowiedź")
        quit()
print("Pobieranie zakończone")