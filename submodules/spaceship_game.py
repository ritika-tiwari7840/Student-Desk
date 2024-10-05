import pygame
import random
import math
from pygame import mixer
import os
#initializing pygame

pygame.init()

#screen setup

screen = pygame.display.set_mode((800,600))

#title
pygame.display.set_caption("space warriors")

#background
background=pygame.image.load(f"{os.getcwd()}/images/spaceship/background.jpg")
#background music
mixer.music.load(f'{os.getcwd()}/images/spaceship/background.wav')
mixer.music.play(-1)

#icon
icon= pygame.image.load(f"{os.getcwd()}/images/spaceship/spaceship.png")
pygame.display.set_icon(icon)
#player
playerimg = pygame.image.load(f"{os.getcwd()}/images/spaceship/spaceship.png")
playerX=350
playerY=500
playerX_change = 0


#bullet
bulletimg = pygame.image.load(f"{os.getcwd()}/images/spaceship/bullet.png")
bulletX=0
bulletY=500
bulletX_change = 0
bulletY_change = 1
#ready in the state will allow the image not to appear on the screen
#fire will allow the bullet to move
bullet_state = "ready"

#font
score = 0
font = pygame.font.Font("freesansbold.ttf",32)

textX=10
textY=10

#game over text
over_font = pygame.font.Font("freesansbold.ttf",64)


 

#enemy
enemyimg =[]
enemyX=[]
enemyY=[]
enemyX_change =[]
enemyY_change =[]
num_enemies = 6
for i in range(num_enemies):
    enemyimg.append(pygame.image.load(f"{os.getcwd()}/images/spaceship/enemy.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)







#function
def game_over_text():
    over_text=over_font.render("GAME OVER !!!",True, (255,255,255))
    screen.blit(over_text, (400, 300)) 
    



def show_score(x,y):
    scorevalue=font.render("score :" + str(score),True, (255,255,255))
    screen.blit(scorevalue, (x, y))     

    
def player(x,y):
    screen.blit(playerimg, (x, y))

    
def enemy( i, x,y):
    screen.blit(enemyimg[i], (x, y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance= math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2))) 
    if distance < 27:
        return True
    else:
        return False


    
#game loop quit
#running= True
#while running:
 #   for event in pygame.event.get():
  #      if event.type== pygame.QUIT:
   #         running= False
while True:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))


    #playerX += 0.1
    #\playerY -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                playerX_change=-0.3
            if event.key ==pygame.K_RIGHT:
                playerX_change= 0.3
            

            if event.key ==pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound(f'{os.getcwd()}/images/spaceship/laser.wav')
                    bullet_Sound.play() 

                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                   
        if event.type ==pygame.KEYUP:
            if event.key ==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                playerX_change= 0
    

    playerX += playerX_change


    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_enemies):
        #game over

        if enemyY[i] > 400:
            for j in range(num_enemies):
                enemyY[j] = 2000
            game_over_text()
            break





        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        collision= isCollision(enemyX[i],enemyY[i],bulletX,bulletY)    
        if collision:
            collision_Sound = mixer.Sound(f'{os.getcwd()}/images/spaceship/explosion.wav')
            collision_Sound.play() 
            bulletY= 480
            bullet_state = "ready"
            score +=1
            print(score)
            enemyX[i]=random.randint(0,736)
            enemyY[i]=random.randint(0,150)

        enemy(i,enemyX[i],enemyY[i])




    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    
    player(playerX,playerY)
    
    show_score(textX,textY)
    pygame.display.update()
