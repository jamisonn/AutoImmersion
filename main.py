import os
import time
import random
import webbrowser
import tkinter as tk

# TodoSection

window = tk.Tk()


def ytNews():
    webbrowser.open("https://www.youtube.com/watch?v=SRS3oAwBivc&pp=ygUY5pel5pys6Kqe44Gu44OL44Ol44O844K5")
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
        webbrowser.open("https://www.youtube.com/watch?v=qlol2rW0pSk")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")
    if channel == 1:
        webbrowser.open("https://www.youtube.com/watch?v=66vWPj9S7Fc&pp=ygUV5pel5pys6Kqe44Gu44OJ44Op44Oe")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")
    if channel == 2:
        webbrowser.open("https://www.youtube.com/watch?v=lYuc8RDaOdQ&pp=ygUV5pel5pys6Kqe44Gu44OJ44Op44Oe")
        time.sleep(180)
        os.system("taskkill /im msedge.exe /f")


def begin_immersion():
    channel = random.randrange(0, 3)
    if channel == 0:
        ytNews()
        begin_immersion()
    if channel == 1:
        ytKids()
        begin_immersion()
    if channel == 2:
        ytSoapOpera()
        begin_immersion()


button = tk.Button(window, text="Begin Random Immersion", command=begin_immersion)
button2 = tk.Button(window, text="Youtube Soap Opera", command=ytSoapOpera)
button3 = tk.Button(window, text="Youtube Kids", command=ytKids)
button4 = tk.Button(window, text="Youtube News ", command=ytNews)


button.pack()
button2.pack()
button3.pack()
button4.pack()
window.mainloop()
