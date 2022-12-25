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
    

def playGame(d):
    global diffuculty
    global maxLineCount
    
    if(d == 1):
        #Easy
        diffuculty = 1
        maxLineCount = 6
    elif(d==2):
        #Med
        diffuculty = 2
        maxLineCount = 4
    elif(d==3):
        #Hard
        maxLineCount = 3
        diffuculty = 3

    lineScore = 0

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

def restartGame():
    global StartTime
    global isDead
    global music
    global nextBeat
    global lineScore
    global TimeElapsed

    print("\n")
    print("======================================")
    print("Game Ended, Your Score:")
    print(str(lineScore) + " Lasers Dodged!")
    print("Survived " + str(TimeElapsed) + " Seconds!")
    print("======================================")

    lineScore = 0

    for index,Blaster in enumerate(Blasters):
        del Blasters[index]

    plr.velX = 1280/2
    plr.velY = 720/2
    plr.reset(screen)

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

    music.stop()
    StartTime = time.time()
    plr.color = (255,255,255)
    plr.dead = False
    isDead = False
    nextBeat = 0

    song = (os.path.join(Path,"song.wav"))
    song_sound = pygame.mixer.Sound(song)
    music = pygame.mixer.Sound.play(song_sound)

Blasters = []
isDead = False
lineScore = 0

def updateDisplay():
    global StartTime
    global nextBeat
    global lineScore
    global TimeElapsed
    StartTime = time.time()
    nextBeat = 0
    global isDead

    while True:
        #Clean Screen
        screen.fill((0,0,0))

        if(not isDead):
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
                isDead = True
                #Restart Game In 5s
                restartGame()

            if(Blaster.destroy):
                del Blasters[index]


        #Timer Text
        Text = FONT.render("Survived "+str(int(TimeElapsed))+"s",True,(0,255,255))
        screen.blit(Text,(0,0))
        Text = FONT.render("@ " + str(lineScore) + " Lines Dodged!",True,(0,255,255))
        screen.blit(Text,(0,25))

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
    global diffuculty
    global maxLineCount
    global lineScore

    if(isDead): return
    global lineCount
    if(lineCount >= maxLineCount):
        newBlaster = gamecharacters.SQRBlasterAtPos(1280/2,720/2,plr.rect.x,plr.rect.y)
        Blasters.append(newBlaster)
        lineCount = 1
        lineScore += 1
    else:
        for i in range(diffuculty):
            newBlaster = gamecharacters.SQRBlaster(1280/2,720/2)
            Blasters.append(newBlaster)
            lineScore += 1
        lineCount += 1
        