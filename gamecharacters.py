import sys,pygame
import os
import random
import time

KEY_DEBUG = False

def clamp(x,min,max):
    if(x < min): return min
    if(x > max): return max
    return x

class Player:
    def __init__(self,x,y):
        #Init
        self.rect = pygame.Rect(x,y,32,32)
        self.x = x
        self.y = y
        self.color = (255,255,255)
        self.velX = 0
        self.velY = 0
        self.speed = 0.45
        #Movement Buttons
        self.left = False
        self.right = False
        self.up = False
        self.down = False


    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0

        #Key Pressess
        KEYS = pygame.key.get_pressed()
        self.up = KEYS[pygame.K_UP] or KEYS[pygame.K_w]
        self.down = KEYS[pygame.K_DOWN] or KEYS[pygame.K_s]
        self.left = KEYS[pygame.K_LEFT] or KEYS[pygame.K_a]
        self.right = KEYS[pygame.K_RIGHT] or KEYS[pygame.K_d]

        if(KEY_DEBUG):
            os.system('cls')
            print("W: " + str(self.up))
            print("S: " + str(self.down))
            print("A: " + str(self.left))
            print("D: " + str(self.right))


        #Movement Buttons
        if self.left and not self.right:
            self.velX = -self.speed
        elif self.right and not self.left:
            self.velX = self.speed


        if self.up and not self.down:
            self.velY = -self.speed
        elif self.down and not self.up:
            self.velY = self.speed

        #Normalize Velocity
        if(abs(self.velX) + abs(self.velY) == 2):
            #Normalize
            self.velX /= 2
            self.velY /= 2

        X = self.x + self.velX
        Y = self.y + self.velY

        self.x = clamp(X,0,1280-32)
        self.y = clamp(Y,0,720-32)

        self.rect = pygame.Rect(self.x,self.y,32,32)

class Blaster():
    def __init__(self,centerPosX,centerPosY):
        StartX = random.randrange(0,centerPosX*2)
        StartY = random.randrange(centerPosY,centerPosY*2)

        EndX = random.randrange(0,centerPosX*2)
        EndY = random.randrange(-(centerPosY*2),centerPosY)

        if(StartX > centerPosX): StartX += 500
        else: StartX -= 500

        if(StartY > centerPosY): StartY += 500
        else: StartY -= 500

        if(EndX > centerPosX): EndX += 500
        else: EndX -= 500

        if(EndY > centerPosY): EndY += 500
        else: EndY -= 500

        if(StartX > centerPosX and EndX > centerPosX): EndX = -EndX
        if(StartY > centerPosY and EndY > centerPosY): EndY = -EndY


        self.startPos = pygame.Vector2(StartX,StartY)
        self.endPos = pygame.Vector2(EndX,EndY)
        self.thickness = 1
        self.start = time.time()

        ''' DEBUG MODE
        print("Start:")
        print(str(self.startPos))
        print("End:")
        print(str(self.endPos))
        '''
        
    
    def draw(self,win):
        timeElapsed = time.time() - self.start

        if(not(timeElapsed >= 0.45)):
            self.thickness = int(80*(timeElapsed/1.2))

        if(timeElapsed <= 0.5):
            pygame.draw.line(win,(255,80,80),self.startPos,self.endPos,self.thickness)