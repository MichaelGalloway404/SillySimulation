import pygame
from .spritesheet_functions import SpriteSheet

floor = 600
class NpcObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        sprite_sheet = SpriteSheet("ball.png")

        self.OBJECTS = []

        image = sprite_sheet.get_image(0, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(50, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(100, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(150, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(200, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(250, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(300, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(350, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(400, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(450, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(500, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(550, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(600, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(650, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(700, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(750, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(800, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(850, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(900, 0, 50, 50)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(900, 0, 50, 50)
        image = pygame.transform.flip(image, True, False)
        self.OBJECTS.append(image)
        image = sprite_sheet.get_image(950, 0, 50, 50)
        self.OBJECTS.append(image)

        self.image = self.OBJECTS[19]
            
        self.rect = self.image.get_rect()

        self.direction = "NOTHING"
        self.change_x = 0
        self.change_y = 0
        self.gravity = 'off'
    def update(self):
        if self.gravity == 'on':
            self.calc_grav()
        self.rect.x += self.change_x  
        self.rect.y += self.change_y
        
        if self.direction == "NOTHING":
            self.image = self.OBJECTS[19]
        elif self.direction == "HOTDOG":
            self.image = self.OBJECTS[0]
        elif self.direction == "HAMBUGER":
            self.image = self.OBJECTS[1]
        elif self.direction == "FRIES":
            self.image = self.OBJECTS[2]
        elif self.direction == "PICKLE":
            self.image = self.OBJECTS[3]
        elif self.direction == "ICECREAM":
            self.image = self.OBJECTS[4]
        elif self.direction == "SAUSAGE":
            self.image = self.OBJECTS[5]
        elif self.direction == "TACO":
            self.image = self.OBJECTS[6]
        elif self.direction == "CANDYBAR":
            self.image = self.OBJECTS[7]
        elif self.direction == "DONUT":
            self.image = self.OBJECTS[8]
        elif self.direction == "PIZZA":
            self.image = self.OBJECTS[9]
        elif self.direction == "EGG":
            self.image = self.OBJECTS[10]
        elif self.direction == "DRUMSTICK":
            self.image = self.OBJECTS[11]
        elif self.direction == "SANDWICH":
            self.image = self.OBJECTS[12]
        elif self.direction == "BROCCOLI":
            self.image = self.OBJECTS[13]
        elif self.direction == "CARROT":
            self.image = self.OBJECTS[14]
        elif self.direction == "LOLLY":
            self.image = self.OBJECTS[15]
        elif self.direction == "FLAPJACKS":
            self.image = self.OBJECTS[16]
        elif self.direction == "GUNLEFT":
            self.image = self.OBJECTS[17]
        elif self.direction == "GUNRIGHT":
            self.image = self.OBJECTS[18]
        elif self.direction == "GUN":
            self.image = self.OBJECTS[17]

            
        if self.rect.bottom > floor:
            self.change_x = 0
            self.change_y = 0
            self.gravity = 'off'

            
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        if self.rect.bottom >= floor:
           if self.change_y >= 0:
               self.change_y = 0



