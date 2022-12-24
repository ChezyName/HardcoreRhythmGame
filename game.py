import os
import threading
import time
import sys,pygame
import random
import gamecharacters

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
    

def playGame():
    print("\n\n\nLoading Up Game Files...\n")
    pygame.init()
    pygame.display.set_caption("HardcoreRhythmGame")
    os.system('wmctrl -a HardcoreRhythmGame')

    global clock
    clock = pygame.time.Clock()

    #Create player
    global plr
    plr = gamecharacters.Player(1280/2,720/2)

    size = width, height = 1280, 720
    global screen
    screen = pygame.display.set_mode(size)
    screen.fill((0,0,0))
    
    loadBeatMap()

    #Main Game Load Song
    global music
    song = (os.path.join(Path,"song.wav"))
    song_sound = pygame.mixer.Sound(song)
    music = pygame.mixer.Sound.play(song_sound)
    
    print("Loaded game files, Starting...")
    updateDisplay()

Entities = []

def updateDisplay():
    StartTime = time.time()
    nextBeat = 0

    while True:
        #Clean Screen
        screen.fill((0,0,0))

        TimeElapsed = time.time() - StartTime

        if(nextBeat < len(BeatMapData) and BeatMapData[nextBeat] < TimeElapsed):
            nextBeat += 1
            onMusicBeat()

        #print("Time Elapsed: " + str(BeatMapData[nextBeat])+"----------"+str(TimeElapsed))

        plr.update()
        plr.draw(screen)

        pygame.display.update()
        pygame.display.flip()
        clock.tick()

        #Exits when song is done
        #if(not music.get_busy()): pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

def onMusicBeat():
    print("BEAT NOW!")