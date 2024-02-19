import pygame
from paddle import Paddle 
from ball import Ball
from brick import Brick

pygame.init()

#Constants for colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Initializes scores and lives
score = 0
lives = 3

#Create a window
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Super Brick Breaker")

#Initializes sprites
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#Initialize groups
all_sprites = pygame.sprite.Group()

all_sprites.add(paddle)
all_sprites.add(ball)

all_bricks = pygame.sprite.Group()
for i in range(7):
  brick = Brick(WHITE, 80, 30)
  brick.rect.x = 60 + i * 100
  brick.rect.y = 60
  all_sprites.add(brick)
  all_bricks.add(brick)

for i in range(7):
  brick = Brick(WHITE, 80, 30)
  brick.rect.x = 60 + i * 100
  brick.rect.y = 100
  all_sprites.add(brick)
  all_bricks.add(brick)

for i in range(7):
  brick = Brick(WHITE, 80, 30)
  brick.rect.x = 60 + i * 100
  brick.rect.y = 140
  all_sprites.add(brick)
  all_bricks.add(brick)

#Running variable
running = True

#Frames per second object
clock = pygame.time.Clock()

#------- Main Game Loop
while running:
  #--- Main Event loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  #Move paddle left and right
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    paddle.move_left(5)

  if keys[pygame.K_RIGHT]:
    paddle.move_right(-5)

  # --- Game Logic | Physics
  all_sprites.update()
  #------ ball bouncing algorithm
  if ball.rect.x >= 790:
    ball.velocity[0] = -ball.velocity[0]

  if ball.rect.x <= 0:
    ball.velocity[0] = -ball.velocity[0]
  
  if ball.rect.y > 590:
    ball.velocity[1] = -ball.velocity[1]
    lives -= 1

    if lives == 0:
      #Display game over
      font = pygame.font.Font(None, 74)
      text = font.render("GAME OVER!", 1, WHITE)
      screen.blit(text, (250, 300))
      pygame.display.flip()
      pygame.time.wait(3000) #Wait 3 seconds

      running = False

  if ball.rect.y < 40:
    ball.velocity[1] = -ball.velocity[1]
  
  #------ Detect collision between ball and paddle
  if pygame.sprite.collide_mask(ball, paddle):
    ball.rect.x -= ball.velocity[0]
    ball.rect.y -= ball.velocity[1]
    ball.bounce()
  
  #------- Detect collision between ball and bricks
  brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)

  for brick in brick_collision_list:
    ball.bounce()
    score += 1
    brick.kill()

    if len(all_bricks) == 0:
      font = pygame.font.Font(None, 74)
      text = font.render("Level Complete!", 1, WHITE)
      screen.blit(text, (250, 300))
      pygame.display.flip()
      pygame.time.wait(3000) #Wait 3 seconds

      running = False

  #--- Drawing Code
  #Black background
  screen.fill(BLACK)
  pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

  #Display score and lives
  font = pygame.font.Font(None, 34)
  small_font = pygame.font.Font(None, 18)

  text = font.render("Score: " + str(score), 1, WHITE)
  screen.blit(text, (20, 10))

  text = font.render("Lives: " + str(lives), 1, WHITE)
  screen.blit(text, (650, 10))

  text = small_font.render("Made by MJ", 1, WHITE)
  screen.blit(text, (10, 580))

  #Draw our sprites
  all_sprites.draw(screen)
  # --- Updates screen with drawings
  pygame.display.flip()

  #--- Limit to 60 frames per second
  clock.tick(60)

#Exits the program
pygame.quit()