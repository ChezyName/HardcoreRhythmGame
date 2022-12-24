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

    pygame.font.init()
    global FONT
    FONT = pygame.font.SysFont(None, 24)

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

    #countdown
    updateDisplay()

Blasters = []

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

        for index,Blaster in enumerate(Blasters):
            Blaster.draw(screen)


            if(plr.rect.colliderect(Blaster.rect) and (time.time() - plr.start) > 2.5 and Blaster.die == True and Blaster.destroy == False):
                #print("Player Has Died!")
                plr.color = (255,0,0)
                plr.dead = True

                #Restart Game In 5s


            if(Blaster.destroy):
                del Blasters[index]


        #Timer Text
        Text = FONT.render("Survived "+str(int(TimeElapsed))+"s",True,(0,255,255))
        screen.blit(Text,(0,0))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)

        #Exits when song is done
        #if(not music.get_busy()): pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


lineCount = 1

def onMusicBeat():
    global lineCount
    if(lineCount >= 3):
        newBlaster = gamecharacters.SQRBlasterAtPos(1280/2,720/2,plr.rect.x,plr.rect.y)
        Blasters.append(newBlaster)
        lineCount = 1
    else:
        newBlaster = gamecharacters.SQRBlaster(1280/2,720/2)
        Blasters.append(newBlaster)
        lineCount += 1