# python-packages directory
import os,sys
import_dir = os.path.abspath('python-packages')
sys.path.append(import_dir)

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
    elif(d==4):

        maxLineCount = 2
        diffuculty = 4
    elif(d==5):

        maxLineCount = 1
        diffuculty = 5
    elif(d==6):
        maxLineCount = 1
        diffuculty = 6

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
    global boost_cooldown
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
    life = 0
    #gamecharacterss = gamecharacters.Player()
    #boost_cooldown = gamecharacterss.boost_cooldown


    StartTime = time.time()
    nextBeat = 0
    global isDead
        #Clean Screen window_background_color, shape_color, warning_zone, red_zone
    def get_value_from_file(search_item):
        with open('tmp.txt', 'r') as file:
            for line in file:
                if line.startswith(f'{search_item}:'):
                    value_str = line.split(': ')[1]
                    value = tuple(map(int, value_str.strip('()\n').split(', ')))
                    return value

    search_item = "window_background_color"
    sereen_value = get_value_from_file(search_item)
    search_item = "shape_color"
    shape_color = get_value_from_file(search_item)
    def interpolate_colors(color1, color2, steps):
        # Extract the RGB components of the two colors
        r1, g1, b1 = color1
        r2, g2, b2 = color2

        # Calculate the step size for each component
        step_r = (r2 - r1) / (steps + 1)
        step_g = (g2 - g1) / (steps + 1)
        step_b = (b2 - b1) / (steps + 1)

        # Initialize a list to store the interpolated colors
        interpolated_colors = []

        # Generate the interpolated colors
        for i in range(steps):
            r = int(r1 + step_r * (i + 1))
            g = int(g1 + step_g * (i + 1))
            b = int(b1 + step_b * (i + 1))
            interpolated_colors.append((r, g, b))

        return interpolated_colors

    color1 = shape_color
    color2 = (255, 0, 0)  # Red
    interpolated_colors = interpolate_colors(color1, color2, 4)


    color_var1, color_var2, color_var3, color_var4= interpolated_colors

    # Access the individual colors
    print("Color 1:", color_var1)
    print("Color 2:", color_var2)
    print("Color 3:", color_var3)
    print("Color 4:", color_var4)


    while True:

        screen.fill((sereen_value))

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

                if life == 1:
                    plr.color = color_var1
                    pygame.time.delay(100)
                if life == 2:
                    plr.color = color_var3
                    pygame.time.delay(100)
                if life == 3:
                    plr.color = color_var3
                    pygame.time.delay(100)
                if life == 4:
                    plr.color = color_var4
                    pygame.time.delay(100)
                if life == 5:
                    plr.color = color_var4
                    pygame.time.delay(100)
                if life == 6:
                    plr.color = color2
                    plr.dead = True
                    isDead = True
                    #Restart Game In 5s
                    #print("Player Has Died!")
                    life = 0

                    pygame.time.delay(3000)
                    restartGame()

                    if(Blaster.destroy):
                        del Blasters[index]

                life = life + 1

        '''
        boost_cooldown = 5
        last_boost_time = 0


        current_time = time.time()
        KEYS = {}

        if KEYS[pygame.K_SPACE]:
            if current_time - last_boost_time >= boost_cooldown:
                last_boost_time = current_time
        '''
        #Timer Text
        Text = FONT.render("Survived "+str(int(TimeElapsed))+"s",True,(0,255,255))
        screen.blit(Text,(0,0))
        Text = FONT.render("@ " + str(lineScore) + " Lines Dodged!",True,(0,255,255))
        screen.blit(Text,(0,25))
        #Text = FONT.render("! " + str(boost_cooldown) + str(current_time) + str(last_boost_time) + " boost_cooldown",True,(0,255,255))
        screen.blit(Text,(0,50))
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
        
