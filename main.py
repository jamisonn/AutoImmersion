import os
import time
import random
import webbrowser


def ytNews():
    webbrowser.open("https://www.youtube.com/watch?v=coYw-eVU0Ks&list=PLJnmPDzgaypH1G_v7N8iEO54b9F180rRhX9")
    time.sleep(180)
    os.system("taskkill /im msedge.exe /f")


def ytKids():
    channel = random.randrange(0, 3)
    if channel == 0:
        webbrowser.open("https://youtu.be/Y3nS5Jdbzzo")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")
    if channel == 1:
        webbrowser.open("https://www.youtube.com/watch?v=SOXy9yfjGlk")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")
    if channel == 2:
        webbrowser.open("https://www.youtube.com/watch?v=tcQn9kNGFuQ")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")
def ytSoapOpera():
    channel = random.randrange(0, 3)
    if channel == 0:
        webbrowser.open("https://youtu.be/NPEoeMP3iNk")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")
    if channel == 1:
        webbrowser.open("https://youtu.be/wakKSMXwzaQ")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")
    if channel == 2:
        webbrowser.open("https://youtu.be/cnPH__cr5t0")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")


def main():
    channel =random.randrange(0, 3)
    if channel == 0:
        ytNews()
        main()
    if channel == 1:
        ytKids()
        main()
    if channel == 2:
        ytSoapOpera()
        main()


main()
