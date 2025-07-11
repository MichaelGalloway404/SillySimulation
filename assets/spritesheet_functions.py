import pygame, os
BLACK = (0, 0, 0)

class SpriteSheet(object): 
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(os.path.join(os.path.dirname(__file__),file_name)).convert()

        

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(BLACK)
        return image
