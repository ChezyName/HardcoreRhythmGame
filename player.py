import sys,pygame
import os

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
        self.speed = 0.65
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
