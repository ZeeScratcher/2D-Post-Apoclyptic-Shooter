############################
# File name Lil Shooter.py #                 
# By Zee_Scratcher         #
# v 0.0.3                  #
#                          #
############################
import pygame
import random
import time
pygame.init()

#imports the module to python


background_colour = (141, 210, 242)
#sets a light blue background for the program

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

display_width = 600
display_height = 600
#sets the width and height of the window
screen = pygame.display.set_mode((display_width,display_height))
#screen.fill(background_colour)
pygame.display.set_caption('Lil shooter')
# sets up the window and title's it 'Lil shooter'
walkRight = [pygame.image.load('RR1.png'),pygame.image.load('RR2.png'), pygame.image.load('RR3.png'), pygame.image.load('RR4.png'), pygame.image.load('RR5.png'), pygame.image.load('RR6.png'), pygame.image.load('RR7.png'), pygame.image.load('RR8.png'),pygame.image.load('RR9.png'), pygame.image.load('RR10.png'),]
walkLeft = [pygame.image.load('RL1.png'), pygame.image.load('RL2.png'), pygame.image.load('RL3.png'), pygame.image.load('RL4.png'), pygame.image.load('RL5.png'), pygame.image.load('RL6.png'), pygame.image.load('RL7.png'), pygame.image.load('RL8.png'),pygame.image.load('RL9.png'), pygame.image.load('RL10.png'),]
superjumpr = pygame.image.load('JR1.png')
superjumpl = pygame.image.load('JL1.png')
PunchR = [pygame.image.load('PR1.png'), pygame.image.load('PR2.png'), pygame.image.load('PR3.png'), pygame.image.load('PR4.png'),]
PunchL = [pygame.image.load('PL1.png'), pygame.image.load('PL2.png'), pygame.image.load('PL3.png'), pygame.image.load('PL4.png'),]
IdleR = [pygame.image.load('IR1.png'), pygame.image.load('IR2.png'), pygame.image.load('IR3.png'), pygame.image.load('IR4.png'),]
IdleL = [pygame.image.load('IL1.png'), pygame.image.load('IL2.png'), pygame.image.load('IL3.png'), pygame.image.load('IL4.png'),pygame.image.load('IL3.png'),]
ShootR = [pygame.image.load('GFR1.png'),pygame.image.load('GFR2.png'),pygame.image.load('GFR3.png'),pygame.image.load('GFR4.png'),]
ShootL = [pygame.image.load('GFL1.png'),pygame.image.load('GFL2.png'),pygame.image.load('GFL3.png'),pygame.image.load('GFL4.png'),]
bg = pygame.image.load('Sunset.jpg')
#imports images from a folder located on the device

pygame.display.flip()

clock = pygame.time.Clock()
#imports the time/FPS(Frames per second) module


bulletSound = pygame.mixer.Sound('bullet.wav')
hitsound = pygame.mixer.Sound('hit.wav')
# Imports the shooting and hit sound

music = pygame.mixer.music.load('Music.wav')

#imports the music in the background



class Player(object):
    #filles all the code for the player

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velo = 8
        self.left = False
        self.right = False
        self.walkcount = 0
        self.Idlecount = 0
        self.guncount = 0
        self.gunisfired = False
        self.isIdle = False
        self.standing = True
        self.punchislaunched = False
        self.punchcount = 0
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 10
        #sets the varibles

    def draw(self, screen):
        #draws all the chracter animations to the screen
        if self.walkcount + 1 >= 27:  #<------------ this tells the project to set the players walking image to the first one
            self.walkcount = 0
        elif self.Idlecount + 1 >= 27: #<------------ same thing exept its for the idle animation
            self.Idlecount = 0
        if not(self.standing):#<---------- this signifies whether the character is walking or standing
            if self.left:
                screen.blit(walkLeft[self.walkcount//3], (self.x,self.y))# <--------- tels it that when it moves left it plays a walking animation
                self.walkcount += 1
                #if self.gunisfired == True:
                #   if self.guncount//5 >= len(ShootR):
                #       self.guncount = 0
                #       self.gunisfired == False
                #   screen.blit(ShootR[self.guncount//5], (self.x,self.y))
                #   self.guncount += 1

            if self.right:
                screen.blit(walkRight[self.walkcount//3], (self.x,self.y)) # < ------- same thing here exept its for right
                self.walkcount += 1
                #if self.gunisfired == True:
                #   if self.guncount//5 >= len(ShootR):
                #       self.guncount = 0
                #       self.gunisfired == False
                #   screen.blit(ShootR[self.guncount//5], (self.x,self.y))
                #   self.guncount += 1
        else: # this else controls what happens if you are not standing
            if self.left:# this means that if you were last looking left you will be able to do some certain actions whilst facing left
                if self.isIdle == True:# this means if you last walked left the idle animation will face left
                    if self.Idlecount//3 >= len(IdleL):
                        self.Idlecount = 0
                        self.isIdle == False
                    screen.blit(IdleL[self.Idlecount//3], (self.x,self.y))
                    self.Idlecount += 1
                if self.gunisfired == True:# same thing here exept its for the gun shot animation
                    if self.guncount//7 >= len(ShootL):
                        self.guncount = 0
                        self.gunisfired == False
                    screen.blit(ShootL[self.guncount//7], (self.x,self.y))
                    self.guncount += 1
                if self.punchislaunched == True:# it applies here as well but it is for the punch animation
                    if self.punchcount//5 >= len(PunchL):
                        self.punchcount = 0
                        self.punchislaunched == False
                    screen.blit(PunchL[self.punchcount//5], (self.x,self.y))
                    self.punchcount += 1
            else:# this else is to signify that everything that happend in the if statments
                if self.isIdle == True:
                    if self.Idlecount//3 >= len(IdleR):
                        self.Idlecount = 0
                        self.isIdle == False
                    screen.blit(IdleR[self.Idlecount//3], (self.x,self.y))
                    self.Idlecount += 1
                if self.gunisfired == True:
                    if self.guncount//7 >= len(ShootR):
                        self.guncount = 0
                        self.gunisfired == False
                    screen.blit(ShootR[self.guncount//7], (self.x,self.y))
                    self.guncount += 1
                if self.punchislaunched == True:
                    if self.punchcount//5 >= len(PunchR):
                        self.punchcount = 0
                        self.punchislaunched == False
                    screen.blit(PunchR[self.punchcount//5], (self.x,self.y))
                    self.punchcount += 1
        self.hitbox = (self.x, self.y, 51, 74)# this create an invisible hitbox
        pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))#this makes the health bar
        pygame.draw.rect(screen, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))#this code is to tell the program that when it losses health it clears a segment of green and replaces it with red
        #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)

        pygame.display.update()#this tels the program to remember to put all the images onto the screen

    def hit(self):#this organises the code for the hitboxes colliding
        if self.health > 0:
            self.health -= 1

    

class Projectile(object):#this organises the code for the bullet
    
    def __init__(self,x,y,radius,colour,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.velo = 8 * self.facing
        # stores the varibles for the bullet

    def draw(self,screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)
        #this drwas the bullet to the screen

class Enemy(object):

    ZwalkRight = [pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'), pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'),pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'), pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'),pygame.image.load('ZR2.png'),pygame.image.load('ZR2.png'),pygame.image.load('ZR2.png'),]
    ZwalkLeft = [pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),pygame.image.load('ZL1.png'),pygame.image.load('ZL1.png'),pygame.image.load('ZL1.png'),]
    #this imports the images of the zombie
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.velo = 3 
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 10
        self.visible = True
        
        #sets all the varibles for the zombie



    def draw(self,win):
        self.move()#this tells it to do everthin in the move function when it is drawn
        if self.visible:#this tells the program to dellete itself if it is 'dead'.
            if self.walkcount + 1 >= 33:
                self.walkcount = 0

            if self.velo > 0:
                screen.blit(self.ZwalkRight[self.walkcount//3], (self.x, self.y))#this sets the walking animation for when it moves right
                self.walkcount += 1
            else:
                screen.blit(self.ZwalkLeft[self.walkcount //3], (self.x, self.y))#same thing  here exept its for when it moves left
                self.walkcount += 1
            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))# this is the health segment for the zombie
            pygame.draw.rect(screen, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))
            self.hitbox = (self.x, self.y, 44, 74)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)
    
    def move(self):
        if timeForLevel == 2000:
            self.velotimeser = 0.00002
            self.velo *= self.velotimeser
        if self.velo > 0:#this has all the function for its moving paterns
            if self.x +  self.velo < self.path[1]:
                self.x += self.velo
            else:
                self.velo = self.velo * -1
                self.walkcount = 0
        else:
            if self.x - self.velo > self.path[0]:
                self.x += self.velo
            else:
                self.velo = self.velo * -1
                self.walkcount = 0

    def hit(self):# this stores the functions for when it is hit

        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False

        #print('hit')# to test it was hit i put a print function

class Enemy1(object):

    ZwalkRight = [pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'), pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'),pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'), pygame.image.load('ZR1.png'), pygame.image.load('ZR2.png'),pygame.image.load('ZR2.png'),pygame.image.load('ZR2.png'),pygame.image.load('ZR2.png'),]
    ZwalkLeft = [pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),pygame.image.load('ZL1.png'), pygame.image.load('ZL2.png'),pygame.image.load('ZL1.png'),pygame.image.load('ZL1.png'),pygame.image.load('ZL1.png'),]
    #this imports the images of the zombie
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.velo = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 10
        self.visible = True
        #sets all the varibles for the zombie



    def draw(self,win):
        self.move()#this tells it to do everthin in the move function when it is drawn
        if self.visible:#this tells the program to dellete itself if it is 'dead'.
            if self.walkcount + 1 >= 33:
                self.walkcount = 0

            if self.velo > 0:
                screen.blit(self.ZwalkRight[self.walkcount//3], (self.x, self.y))#this sets the walking animation for when it moves right
                self.walkcount += 1
            else:
                screen.blit(self.ZwalkLeft[self.walkcount //3], (self.x, self.y))#same thing  here exept its for when it moves left
                self.walkcount += 1
            pygame.draw.rect(screen, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))# this is the health segment for the zombie
            pygame.draw.rect(screen, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10) * (10 - self.health)), 10))
            self.hitbox = (self.x, self.y, 44, 74)
            #pygame.draw.rect(screen, (255,0,0), self.hitbox,2)
    
    def move(self):
        if self.velo > 0:#this has all the function for its moving paterns
            if self.x +  self.velo < self.path[1]:
                self.x += self.velo
            else:
                self.velo = self.velo * -1
                self.walkcount = 0
        else:
            if self.x - self.velo > self.path[0]:
                self.x += self.velo
            else:
                self.velo = self.velo * -1
                self.walkcount = 0

    def hit(self):# this stores the functions for when it is hit

        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False

        #print('hit')# to test it was hit i put a print function

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)



def quitgame():
    pygame.quit()
    quit()
intro = False
run = False

def stop_intro():
    global intro
    global run
    intro = False
    run = True

def respawn():
    global run
    run = False



def dead():
    ####################################


    ####################################
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Died", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    screen.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Quit", 250, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Lilshooter", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        screen.blit(TextSurf, TextRect)

        button("LETS PLAY!", 20, 450, 115, 50, green, bright_green, stop_intro)
        button("Quit", 490, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)




def redrawGameWindow():
    #this draws the characters the background and the text onto the screen
    
    screen.blit(bg, (0,-100))
    text = font.render('Points:' + str(points), 1, (255,251,0))
    screen.blit(text, (390, 10))
    man.draw(screen)
    zombie.draw(screen)
    zombie1.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.update()

    
    pygame.display.update()
#the code bellow sets any important varibles that coudnt be put in anany of the classes

velotimeser = 1
timeForLevel = 0
font = pygame.font.SysFont('comicsans', 30, True)
man = Player(300, 508, 64, 64)
zombie = Enemy(100, 508, 64, 64, 450)
zombie1 = Enemy1(100, 508, 64, 64, 450)
randomside = 0
gunCapacity = 1
points = 0
bullets = []
intro = True
game_intro()
pygame.mixer.music.play(-1)

 # in seconds



while run:

    clock.tick(27)
    #this is the hitbox for when the zombie collides with the player and the player hasnt shot a bullet or has launched a punch that it should deduct a peice of health and 5 points and move the player back depending on where the zombie is facing


    timeForLevel += 0.05
    
    
    


    if man.hitbox[1] < zombie.hitbox[1] + zombie.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie.hitbox[0] and man.hitbox[0] < zombie.hitbox[0] + zombie.hitbox[2] and man.punchislaunched == False and zombie.visible == True and zombie.velo > 0 and man.x > zombie.x:
            man.x += 15
            pygame.time.delay(10)
            points -= 5
            man.hit()

    if man.hitbox[1] < zombie.hitbox[1] + zombie.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie.hitbox[0] and man.hitbox[0] < zombie.hitbox[0] + zombie.hitbox[2] and man.punchislaunched == False and zombie.visible == True and zombie.velo > 0 and man.x < zombie.x:
            man.x -= 15
            pygame.time.delay(10)
            points -= 5
            man.hit()

    if man.hitbox[1] < zombie.hitbox[1] + zombie.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie.hitbox[0] and man.hitbox[0] < zombie.hitbox[0] + zombie.hitbox[2] and man.punchislaunched == False and zombie.visible == True and zombie.velo < 0 and man.x <= zombie.x:
            man.x -= 15
            pygame.time.delay(10)
            points -= 5
            man.hit()

    if man.hitbox[1] < zombie.hitbox[1] + zombie.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie.hitbox[0] and man.hitbox[0] < zombie.hitbox[0] + zombie.hitbox[2] and man.punchislaunched == False and zombie.visible == True and zombie.velo < 0 and man.x > zombie.x:
            man.x += 15
            pygame.time.delay(10)
            points -= 5
            man.hit()

    

    #this hitbox detects if the player is touching the zombie whilst punching it
    if man.hitbox[1] < zombie.hitbox[1] + zombie.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie.hitbox[0] and man.hitbox[0] < zombie.hitbox[0] + zombie.hitbox[2] and man.punchislaunched == True and zombie.visible == True:
            if zombie.velo < 0 and zombie.x < man.x:
                zombie.x = zombie.x - 15
                zombie.hit()
                points += 5
            if zombie.velo < 0 and zombie.x > man.x:
                zombie.x = zombie.x + 15
                zombie.hit()
                points += 5
            if zombie.velo > 0 and zombie.x > man.x:
                zombie.x = zombie.x + 15
                zombie.hit()
                points += 5
            if zombie.velo > 0 and zombie.x < man.x:
                zombie.x = zombie.x - 15
                zombie.hit()
                points += 5

    #this is the hitbox for when the zombie collides with the player and the player hasnt shot a bullet or has launched a punch that it should deduct a peice of health and 5 points and move the player back depending on where the zombie is facing
    if man.hitbox[1] < zombie1.hitbox[1] + zombie1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie1.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie1.hitbox[0] and man.hitbox[0] < zombie1.hitbox[0] + zombie1.hitbox[2] and man.punchislaunched == False and zombie1.visible == True and zombie.velo > 0 and man.x > zombie1.x:
            man.x += 15
            pygame.time.delay(10)
            points -= 5
            man.hit()

    if man.hitbox[1] < zombie1.hitbox[1] + zombie1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie1.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie1.hitbox[0] and man.hitbox[0] < zombie1.hitbox[0] + zombie1.hitbox[2] and man.punchislaunched == False and zombie1.visible == True and zombie.velo > 0 and man.x < zombie1.x:
            man.x += 15
            pygame.time.delay(10)
            points -= 5
            man.hit()
            
    #same thing here expet its for when the zombie is facing left       
    if man.hitbox[1] < zombie1.hitbox[1] + zombie1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie1.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie1.hitbox[0] and man.hitbox[0] < zombie1.hitbox[0] + zombie1.hitbox[2] and man.punchislaunched == False and zombie1.visible == True and zombie1.velo < 0 and man.x < zombie1.x:
            man.x -= 15
            pygame.time.delay(10)
            points -= 5
            man.hit()

    if man.hitbox[1] < zombie1.hitbox[1] + zombie1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie1.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie1.hitbox[0] and man.hitbox[0] < zombie1.hitbox[0] + zombie1.hitbox[2] and man.punchislaunched == False and zombie1.visible == True and zombie1.velo < 0 and man.x > zombie1.x:
            man.x -= 15
            pygame.time.delay(10)
            points -= 5
            man.hit()

    #this hitbox detects if the player is touching the zombie whilst punching it
    if man.hitbox[1] < zombie1.hitbox[1] + zombie1.hitbox[3] and man.hitbox[1] + man.hitbox[3] > zombie1.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > zombie1.hitbox[0] and man.hitbox[0] < zombie1.hitbox[0] + zombie1.hitbox[2] and man.punchislaunched == True and zombie1.visible == True:
                if zombie1.velo < 0 and zombie1.x < man.x:
                    zombie1.x = zombie1.x - 15
                    zombie1.hit()
                    points += 1
                if zombie1.velo < 0 and zombie1.x > man.x:
                    zombie1.x = zombie1.x + 15
                    zombie1.hit()
                    points += 1
                if zombie1.velo > 0 and zombie1.x > man.x:
                    zombie1.x = zombie1.x + 15
                    zombie1.hit()
                    points += 1
                if zombie1.velo > 0 and zombie1.x < man.x:
                    zombie1.x = zombie1.x - 15
                    zombie1.hit()
                    points += 1
                    

    #this tels it to shoot one bullet at a time instead of sending a group of bullets to the zombie
    if gunCapacity > 0:
        gunCapacity += 1
    if gunCapacity> 10:
        gunCapacity = 0

    #this tels it to close the programe if you press the big red cross at the top right
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            run = False
       
    #this sets the collision for when the zombie  touches the bullet
    for bullet in bullets:
        if bullet.y - bullet.radius < zombie.hitbox[1] + zombie.hitbox[3] and bullet.y + bullet.radius > zombie.hitbox[1]:
            if bullet.x + bullet.radius > zombie.hitbox[0] and bullet.x - bullet.radius < zombie.hitbox[0] + zombie.hitbox[2] and zombie.visible == True:
                if zombie.velo < 0 and zombie.x < man.x:
                    zombie.x = zombie.x - 15
                    zombie.hit()
                    points += 1
                    bullets.pop(bullets.index(bullet))
                if zombie.velo < 0 and zombie.x > man.x:
                    zombie.x = zombie.x + 15
                    zombie.hit()
                    points += 1
                    bullets.pop(bullets.index(bullet))
                if zombie.velo > 0 and zombie.x > man.x:
                    zombie.x = zombie.x + 15
                    zombie.hit()
                    points += 1
                    bullets.pop(bullets.index(bullet))
                if zombie.velo > 0 and zombie.x < man.x:
                    zombie.x = zombie.x - 15
                    zombie.hit()
                    points += 1
                    bullets.pop(bullets.index(bullet))

                
                
                    

        #this tells the bullet to delete itself if it touches the the end of the screen
        if bullet.x < 600 and bullet.x > 0:
            bullet.x += bullet.velo
        else:
            bullets.pop(bullets.index(bullet))

    
    #this sets the collision for when the zombie  touches the bullet
    for bullet in bullets:
        if bullet.y - bullet.radius < zombie1.hitbox[1] + zombie1.hitbox[3] and bullet.y + bullet.radius > zombie1.hitbox[1]:
            if bullet.x + bullet.radius > zombie1.hitbox[0] and bullet.x - bullet.radius < zombie1.hitbox[0] + zombie1.hitbox[2] and zombie1.visible == True:
                if zombie1.velo < 0 and zombie1.x < man.x:
                    zombie1.x = zombie1.x - 15
                    zombie1.hit()
                    points += 1
                    bullets.pop(bullets.index(bullet))
                if zombie1.velo < 0 and zombie1.x > man.x:
                    zombie1.x = zombie1.x + 15
                    zombie1.hit()
                    points += 1
                    bullets.pop(bullets.index(bullet))
                if zombie1.velo > 0 and zombie1.x > man.x:
                    zombie1.x = zombie1.x + 15
                    zombie1.hit()
                    points += 1
                    bullets.pop(bullets.index(bullet))
                if zombie1.velo > 0 and zombie1.x < man.x:
                    zombie1.x = zombie1.x - 15
                    zombie1.hit()
                    points += 1
                    bullets.pop(bullets.index(bullet))
        #this tells the bullet to delete itself if it touches the the end of the screen
        if bullet.x < 600 and bullet.x > 0:
            bullet.x += bullet.velo
        else:
            bullets.pop(bullets.index(bullet))

    
    if timeForLevel > 20:
        velotimeser = 1.0002
        zombie.velo = zombie.velo * velotimeser
        zombie1.velo = zombie1.velo * velotimeser


    

    keys = pygame.key.get_pressed()

    #these are the keaboard bings for all the functions
    if keys[pygame.K_LEFT] and man.x > man.velo:
        man.x -= man.velo
        man.right = False
        man.left = True
        man.Idlecount = 0
        man.guncount = 0
        man.gunisfired = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 600 - man.width - man.velo:
        man.x += man.velo
        man.right = True
        man.left = False
        man.Idlecount = 0
        man.guncount = 0
        man.gunisfired = False
        man.standing = False
    elif keys[pygame.K_SPACE]:
        man.gunisfired = True
        man.isIdle = False
        man.standing = True
        man.Idlecount = 0
        man.punchislaunched = False
        man.walkcount = 0
    
    elif keys[pygame.K_x]:
        man.gunisfired = False
        man.isIdle = False
        man.standing = True
        man.Idlecount = 0
        man.guncount = 0
        man.punchislaunched = True
    else:
        man.walkcount = 0
        man.isIdle = True
        man.guncount = 0
        man.gunisfired = False
        man.standing = True
        man.punchislaunched = False
        man.punchcount = 0
    if keys[pygame.K_SPACE] and gunCapacity == 0:
        
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))
            bulletSound.play()
        gunCapacity = 1

    #this tells the zombie to respawn when it is dead
    if zombie.visible == False:
        randomside = random.randint(1,4)
        if randomside == 1:
            zombie.x = 20
        if randomside ==2:
            zombie.x = 580
        if randomside ==3:
            zombie.x = 580
            zombie1.x = 520
            zombie1.visible = True
            zombie1.health = 10
            zombie1.draw(screen)
        if randomside == 4:
            zombie.x = 20
            zombie1.x = 80
            zombie1.visible = True
            zombie1.health = 10
            zombie1.draw(screen)

        zombie.visible = True
        zombie.health = 10
        zombie.draw(screen)
    print(randomside)

    if man.health == 0:
        dead()    

    
    
       
    redrawGameWindow()
    Timetext = font.render('Time elapsed:' + str(round(timeForLevel,1)), 1, (255,251,0))
    screen.blit(Timetext, (20, 10))
    pygame.display.update()

pygame.quit()
