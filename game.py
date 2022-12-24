import os
import threading
import time
import sys,pygame
import random
import player

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


    TotalTime = 0
    num = 0

    for t in BeatMapData:
        sleeptime = (t - TotalTime)
        TotalTime += sleeptime
        time.sleep(round(sleeptime,4))
        #os.system('cls')
        #print("-> NOTE IS HERE @ " + str(t) + "/" + str(sleeptime) + "\n")
        #Note RN
        onMusicBeat()

def playGame():
    print("\n\n\nLoading Up Game Files...\n")
    pygame.init()
    pygame.display.set_caption("HardcoreRhythmGame")
    #os.system('wmctrl -a HardcoreRhythmGame')

    global clock
    clock = pygame.time.Clock()

    #Create player
    global plr
    plr = player.Player(1280/2,720/2)

    size = width, height = 1280, 720
    global screen
    screen = pygame.display.set_mode(size)
    screen.fill((0,0,0))
    
    loadBeatMap()

    #Main Game Load Song
    song = (os.path.join(Path,"song.wav"))
    song_sound = pygame.mixer.Sound(song)
    pygame.mixer.Sound.play(song_sound)
    
    print("Loaded game files, Starting...")
    updateDisplay()

def updateDisplay():
    StartTime = time.time()
    nextBeat = 0

    while True:
        TimeElapsed = time.time() - StartTime
        BeatTime = BeatMapData[nextBeat] - TimeElapsed
        if(nextBeat < 0):
            nextBeat += 1
            onMusicBeat()

        #print("Time Elapsed: " + str(TimeElapsed) + " : Beat Timings " + str(nextBeat) +":"+ str(BeatTime))


        screen.fill((0,0,0))
        plr.update()
        plr.draw(screen)
        pygame.display.update()
        pygame.display.flip()
        clock.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

def onMusicBeat():
    screen.fill((0,0,0))
    '''
    CIRCLEPOS = (random.randint(0,1280), random.randint(0,720)) 
    CIRCLEPOS = (1280/2,720/2)
    C = pygame.draw.circle(screen,(random.randint(80,255),random.randint(80,255),random.randint(80,255)),CIRCLEPOS,250,2500)
    '''