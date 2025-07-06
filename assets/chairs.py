import pygame
from .spritesheet_functions import SpriteSheet
        
class SEET(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()

        self.CHAIR = []
        
        sprite_sheet = SpriteSheet("bench.png")
        image = sprite_sheet.get_image(2, 2, 148, 62)
        self.CHAIR.append(image)
        image = sprite_sheet.get_image(2, 68, 148, 62)
        self.CHAIR.append(image)
        
        self.image = self.CHAIR[0]
        self.rect = self.image.get_rect()

        self.ObjType = 'SEET'
        self.ObjFace = 'LEFT'
        self.direction = "BENCH"

    def update(self):
        if self.ObjType == 'SEET':
            if self.ObjFace == 'LEFT':
                if self.direction == "BENCH":
                    self.image = self.CHAIR[0]
                    
        if self.ObjType == 'SEET':     
            if self.ObjFace == 'RIGHT':
                if self.direction == "BENCH":
                    self.image = self.CHAIR[1]
