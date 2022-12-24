import os
from playsound import playsound
import threading
import time
import subprocess
import random
import tkinter as tk
from tkinter.ttk import *

window_width = 80
window_height = 80

#Consts
Path = os.path.join(os.getcwd(),"Music")
BeatMapData = []

def loadBeatMap():
    global BeatMapData
    file = open(os.path.join(Path,"song.cheesemap"))
    text = file.read()
    BeatMapData = [float(string) for string in text.split('\n') if string != '']
    

def realGame():
    #Load beatmap FIRST
    loadBeatMap()
    print("Ready To Play??")

    #Main Game Load Song
    song = (os.path.join(Path,"song.wav"))
    threading.Thread(target=playsound, args=(song,), daemon=True).start()

    global num
    global TotalTime
    num = 0

    t = BeatMapData[num]
    num += 1
    TotalTime = 0
    sleeptime = t - TotalTime
    TotalTime += sleeptime
    time.sleep(sleeptime)
    mainW.newWindow()

    '''
    print(len(BeatMapData))
    for t in BeatMapData:
        sleeptime = t - TotalTime
        TotalTime += sleeptime
        time.sleep(sleeptime)
        os.system('cls')
        print("-> NOTE IS HERE @ " + str(t) + "/" + str(sleeptime) + "\n")
        #Note RN
        threading.Thread(target=mainW.newWindow(), args=(), daemon=True).start()
    '''

def playGame():
    root = tk.Tk()
    global mainW
    mainW = Example(root)
    mainW.pack(side="top", fill="both", expand=True)

    root.after(0,realGame)
    root.mainloop()

def createNewWindowIn():
    global num
    global TotalTime
    t = BeatMapData[num]
    num += 1
    sleeptime = t - TotalTime
    TotalTime += sleeptime
    time.sleep(sleeptime)
    mainW.newWindow()

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.count = 0

    def newWindow(self):
        self.count += 1
        window = tk.Toplevel(self)
        #Center Windowd
        global screen_height, screen_width, x_cordinate, y_cordinate
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        #random positioning
        x_cordinate = random.randrange(0,(screen_width) - (window_width))
        y_cordinate = random.randrange(0,(screen_height) - (window_height))

        print("\n>Creating New Window")

        window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        btn = tk.Button(window, text = 'HERE', bd = '5', command = window.destroy,width=1000,height=1000)
        btn.pack(side = 'top') 

        #Finish Init Window
        window.resizable(False, False)
        window.after(0,createNewWindowIn)