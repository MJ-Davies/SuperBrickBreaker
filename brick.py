import pygame

BLACK = (0, 0, 0)

class Brick(pygame.sprite.Sprite):
  def __init__(self, color, width, height):
    super().__init__()

    #Pass in parameters
    self.image = pygame.Surface([width, height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)

    #Draw rect
    pygame.draw.rect(self.image, color, [0, 0, width, height])

    #Fetch the rectangle
    self.rect = self.image.get_rect()