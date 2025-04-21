import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('background.png')

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6


for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("Alien.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH -69))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
Bl=pygame.load.image("Bl.png")
BlX=0
BlY=PLAYER_START_Y
BlX_change=0
BlY_change=BULLET_SPEED_Y
Bl_state="ready"
score=0
over_font=pygame.font.Font('freesanbold.ttf',64)
def show_score(x,y):
    score= font.render("Score:"+str(score_value),True,(255,255,255))
    screen.blit(score(x,y))
def game_over_text(x,y):
    over_text=over_font.render('GET OUT',True(255,255,255))
    screen.blit(over_text(200,250))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(Bl.png,(x+16,y+16))
    
def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              playerX_change = -5
          if event.key == pygame.K_RIGHT:
              playerX_change = 5
          if event.key == pygame.K_SPACE and bullet_state == "ready":
              bulletX = playerX
              fire_bullet(bulletX,bulletY)
      if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
          playerX_change = 0
    playerX+=playerX_change
    playerX=max(0,min(playerX,SCREEN_WIDTH -64))
    for i in range(num_of_enemies):
        if enemyY[i]>340:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
        enemyX[i]=enemyX_change[i]
        if enemyX[i]<0 or enemyX[i]>=SCREEN_WIDTH -64:
            enemyX_change[i]*=-1
            enemyY[i]+=enemyY_change[i]
            if isCollision(enemyX[i],enemyY[i],bulletX,bulletY):
                bulletY= PLAYER_START_Y
                bullet_state="ready"
                score_value+=1
                enemyX[i]=random.randint(0,SCREEN_WIDTH-64)
                enemyX[i]=random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX)
            enemy(enemyY[i],enemyX[i],i)
            if bulletY<0:
                bulletY=PLAYER_START_Y
                bullet_state="ready"
            elif bullet_state=="fire":
                fire_bullet(bulletX,bulletY)
                bulletY_=bulletY_change
            player(playerX,playerY)
            show_score(textX,textY)
            pygame.display.update()