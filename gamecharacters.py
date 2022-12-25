# python-packages directory
import os,sys
import_dir = os.path.abspath('python-packages')
sys.path.append(import_dir)

import sys,pygame
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
        self.speed = 6
        #Movement Buttons
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.dead = False
        self.start = time.time()

    def draw(self,win):
        pygame.draw.rect(win,self.color,self.rect)

    def reset(self,win):
        self.start = time.time()
        pygame.draw.rect(win,self.color,self.rect)

    def update(self):
        self.velX = 0
        self.velY = 0

        #Key Pressess
        if(not self.dead):
            KEYS = pygame.key.get_pressed()
            self.up = KEYS[pygame.K_UP] or KEYS[pygame.K_w]
            self.down = KEYS[pygame.K_DOWN] or KEYS[pygame.K_s]
            self.left = KEYS[pygame.K_LEFT] or KEYS[pygame.K_a]
            self.right = KEYS[pygame.K_RIGHT] or KEYS[pygame.K_d]
        else:
            self.up = False
            self.down = False
            self.right = False
            self.left = False

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

class SQRBlaster():
    def __init__(self,centerPosX,centerPosY):
        self.Width = 0
        self.Height = 0
        X = 0
        Y = 0
        self.XorY = bool(random.getrandbits(1))

        if(self.XorY):
            #X Mode
            self.Width = 15
            self.Height = 10000
            X = random.randrange(0,centerPosX*2)
            Y = 0
        else:
            #Y Mode
            self.Width = 10000
            self.Height = 15
            X = 0
            Y = random.randrange(0,centerPosY*2)

        self.start = time.time()
        self.die = False
        self.destroy = False
        self.X = X
        self.Y = Y
        self.rect = pygame.Rect(X,Y,self.Width,self.Height)
        self.color = (0,0,0)
        self.alpha = 0
        
    
    def draw(self,win):
        timeElapsed = time.time() - self.start

        if(not(timeElapsed >= 0.95)):
            #Transparency
            self.alpha = 128*(timeElapsed/0.95)
        else:
            self.die = True

        if(timeElapsed <= 1):
            self.rect = pygame.Rect(self.X,self.Y,self.Width,self.Height)
            s = pygame.Surface((self.Width,self.Height))
            s.set_alpha(self.alpha)
            if(self.die): s.fill((255,0,0))
            else: s.fill((0,255,0))
            win.blit(s, (self.X,self.Y))
        else:
            self.destroy = True


class SQRBlasterAtPos():
    def __init__(self,centerPosX,centerPosY,PlayerPosX,PlayerPosY):
        self.Width = 0
        self.Height = 0
        X = 0
        Y = 0
        self.XorY = bool(random.getrandbits(1))

        if(self.XorY):
            #X Mode
            self.Width = 15
            self.Height = 10000
            X = PlayerPosX
            Y = 0
        else:
            #Y Mode
            self.Width = 10000
            self.Height = 15
            X = 0
            Y = PlayerPosY

        self.start = time.time()
        self.die = False
        self.destroy = False
        self.X = X
        self.Y = Y
        self.rect = pygame.Rect(self.X,self.Y,self.Width,self.Height)
        self.color = (0,0,0)
        self.alpha = 0
        
    
    def draw(self,win):
        timeElapsed = time.time() - self.start

        if(not(timeElapsed >= 0.6)):
            #Transparency
            self.alpha = 128*(timeElapsed/0.6)
        else:
            self.die = True

        if(timeElapsed <= 0.65):
            self.rect = pygame.Rect(self.X,self.Y,self.Width,self.Height)
            s = pygame.Surface((self.Width,self.Height))
            s.set_alpha(self.alpha)
            if(self.die): s.fill((255,0,0))
            else: s.fill((0,255,0))
            win.blit(s, (self.X,self.Y))
        else:
            self.destroy = True