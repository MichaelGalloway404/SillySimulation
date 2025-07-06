import pygame
from .spritesheet_functions import SpriteSheet

class EVILMANFRAMES(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.sprite_sheet = SpriteSheet("clown.png")
        
        self.LEFT = []
        self.RIGHT = []
        self.BREETH = []
        self.GRABRIGHT = []
        self.GRABLEFT = []        
        self.SITRIGHT = []      
        self.SITLEFT = []        
        self.SEATEDRIGHT = []       
        self.SEATEDLEFT = []        
        self.GETUPRIGHT = []
        self.GETUPLEFT = []
        self.THROWRIGHT = []
        self.THROWLEFT = []
        self.EATRIGHT = []
        self.EATLEFT = []
        self.PICKUPRIGHT = []
        self.PICKUPLEFT = []
        self.ATKLEFT = []
        self.ATKRIGHT = []

        image = self.sprite_sheet.get_image(2, 386, 156, 124)
        self.ATKLEFT.append(image)
        
        image = self.sprite_sheet.get_image(2, 386, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.ATKRIGHT.append(image)

        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        self.PICKUPLEFT.append(image)
        image = self.sprite_sheet.get_image(802, 258, 156, 124)
        self.PICKUPLEFT.append(image)
        image = self.sprite_sheet.get_image(962, 258, 156, 124)
        self.PICKUPLEFT.append(image)
        image = self.sprite_sheet.get_image(802, 258, 156, 124)
        self.PICKUPLEFT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        self.PICKUPLEFT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        self.PICKUPLEFT.append(image)

        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.PICKUPRIGHT.append(image)
        image = self.sprite_sheet.get_image(802, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.PICKUPRIGHT.append(image)
        image = self.sprite_sheet.get_image(962, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.PICKUPRIGHT.append(image)
        image = self.sprite_sheet.get_image(802, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.PICKUPRIGHT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.PICKUPRIGHT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.PICKUPRIGHT.append(image)

        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        self.EATLEFT.append(image)
        image = self.sprite_sheet.get_image(322, 130, 156, 124)
        self.EATLEFT.append(image)
        image = self.sprite_sheet.get_image(482, 130, 156, 124)
        self.EATLEFT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        self.EATLEFT.append(image)
        image = self.sprite_sheet.get_image(802, 130, 156, 124)
        self.EATLEFT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        self.EATLEFT.append(image)
        image = self.sprite_sheet.get_image(802, 130, 156, 124)
        self.EATLEFT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        self.EATLEFT.append(image)
        image = self.sprite_sheet.get_image(802, 130, 156, 124)
        self.EATLEFT.append(image)

        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)
        image = self.sprite_sheet.get_image(322, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)
        image = self.sprite_sheet.get_image(482, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)
        image = self.sprite_sheet.get_image(802, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)
        image = self.sprite_sheet.get_image(802, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)
        image = self.sprite_sheet.get_image(642, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)
        image = self.sprite_sheet.get_image(802, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.EATRIGHT.append(image)

        image = self.sprite_sheet.get_image(322, 258, 156, 124)
        self.THROWLEFT.append(image)
        image = self.sprite_sheet.get_image(322, 258, 156, 124)
        self.THROWLEFT.append(image)
        image = self.sprite_sheet.get_image(482, 258, 156, 124)
        self.THROWLEFT.append(image)
        image = self.sprite_sheet.get_image(642, 258, 156, 124)
        self.THROWLEFT.append(image)
        image = self.sprite_sheet.get_image(642, 258, 156, 124)
        self.THROWLEFT.append(image)

        image = self.sprite_sheet.get_image(322, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.THROWRIGHT.append(image)
        image = self.sprite_sheet.get_image(322, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.THROWRIGHT.append(image)
        image = self.sprite_sheet.get_image(482, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.THROWRIGHT.append(image)
        image = self.sprite_sheet.get_image(642, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.THROWRIGHT.append(image)
        image = self.sprite_sheet.get_image(642, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.THROWRIGHT.append(image)

        image = self.sprite_sheet.get_image(2, 258, 156, 124)
        self.GETUPLEFT.append(image)
        image = self.sprite_sheet.get_image(962, 130, 156, 124)
        self.GETUPLEFT.append(image)
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        self.GETUPLEFT.append(image)

        image = self.sprite_sheet.get_image(2, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GETUPRIGHT.append(image)
        image = self.sprite_sheet.get_image(962, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GETUPRIGHT.append(image)
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GETUPRIGHT.append(image)

        image = self.sprite_sheet.get_image(2, 258, 156, 124)
        self.SEATEDLEFT.append(image)
        image = self.sprite_sheet.get_image(162, 258, 156, 124)
        self.SEATEDLEFT.append(image)

        image = self.sprite_sheet.get_image(2, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.SEATEDRIGHT.append(image)
        image = self.sprite_sheet.get_image(162, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.SEATEDRIGHT.append(image)
        
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        self.SITLEFT.append(image)
        image = self.sprite_sheet.get_image(962, 130, 156, 124)
        self.SITLEFT.append(image)
        image = self.sprite_sheet.get_image(2, 258, 156, 124)
        self.SITLEFT.append(image)

        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.SITRIGHT.append(image)
        image = self.sprite_sheet.get_image(962, 130, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.SITRIGHT.append(image)
        image = self.sprite_sheet.get_image(2, 258, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.SITRIGHT.append(image)

        image = self.sprite_sheet.get_image(962, 2, 156, 124)
        self.GRABLEFT.append(image)
        image = self.sprite_sheet.get_image(962, 2, 156, 124)
        self.GRABLEFT.append(image)
        image = self.sprite_sheet.get_image(962, 2, 156, 124)
        self.GRABLEFT.append(image)
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        self.GRABLEFT.append(image)
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        self.GRABLEFT.append(image)
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        self.GRABLEFT.append(image)

        
        image = self.sprite_sheet.get_image(962, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GRABRIGHT.append(image)
        image = self.sprite_sheet.get_image(962, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GRABRIGHT.append(image)
        image = self.sprite_sheet.get_image(962, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GRABRIGHT.append(image)
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GRABRIGHT.append(image)
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GRABRIGHT.append(image)
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.GRABRIGHT.append(image)

        
        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        self.LEFT.append(image)
        image = self.sprite_sheet.get_image(482, 2, 156, 124)
        self.LEFT.append(image)
        image = self.sprite_sheet.get_image(642, 2, 156, 124)
        self.LEFT.append(image)
        image = self.sprite_sheet.get_image(802, 2, 156, 124)
        self.LEFT.append(image)


        image = self.sprite_sheet.get_image(322, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.RIGHT.append(image)
        image = self.sprite_sheet.get_image(482, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.RIGHT.append(image)
        image = self.sprite_sheet.get_image(642, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.RIGHT.append(image)
        image = self.sprite_sheet.get_image(802, 2, 156, 124)
        image = pygame.transform.flip(image, True, False)
        self.RIGHT.append(image)


        image = self.sprite_sheet.get_image(2, 2, 156, 124)
        self.BREETH.append(image)
        image = self.sprite_sheet.get_image(162, 2, 156, 124)
        self.BREETH.append(image)


        self.image = self.RIGHT[0]
            
        self.rect = self.image.get_rect()

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
