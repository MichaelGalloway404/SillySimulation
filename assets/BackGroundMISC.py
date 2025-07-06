import pygame
from .spritesheet_functions import SpriteSheet

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill((255,0,32))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
class backgroundOBJECT(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()

        self.TRASHCAN = []
        self.FLAG = []
        self.CHIMES = []
        self.WINDCHICKEN = []
        self.TOXICBUBBLE = []
        self.TOXICCLEEN = []
        self.TOXICDIRTY = []
        self.TOXICGRAFFITI = []
        
        sprite_sheet = SpriteSheet('BackMisc.png')

        image = sprite_sheet.get_image(38, 832, 86, 115)
        self.TRASHCAN.append(image)
        image = sprite_sheet.get_image(214, 832, 86, 115)
        self.TRASHCAN.append(image)
        image = sprite_sheet.get_image(382, 832, 86, 115)
        self.TRASHCAN.append(image)
        
        image = sprite_sheet.get_image(2, 2, 114, 118)
        self.FLAG.append(image)
        image = sprite_sheet.get_image(130, 2, 114, 118)
        self.FLAG.append(image)
        image = sprite_sheet.get_image(258, 2, 114, 118)
        self.FLAG.append(image)
        image = sprite_sheet.get_image(386, 2, 114, 118)
        self.FLAG.append(image)
        image = sprite_sheet.get_image(514, 2, 114, 118)
        self.FLAG.append(image)

        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(130, 137, 114, 118)
        image = pygame.transform.flip(image, True, False)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(130, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(258, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(130, 137, 114, 118)
        image = pygame.transform.flip(image, True, False)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(130, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)
        image = sprite_sheet.get_image(2, 137, 114, 118)
        self.CHIMES.append(image)

        image = sprite_sheet.get_image(2, 268, 114, 118)
        image = pygame.transform.scale(image, (70, 70))
        self.WINDCHICKEN.append(image)
        image = sprite_sheet.get_image(130, 268, 114, 118)
        image = pygame.transform.scale(image, (70, 70))
        self.WINDCHICKEN.append(image)
        image = sprite_sheet.get_image(258, 268, 114, 118)
        image = pygame.transform.scale(image, (70, 70))
        self.WINDCHICKEN.append(image)
        image = sprite_sheet.get_image(2, 268, 114, 118)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (70, 70))
        self.WINDCHICKEN.append(image)
        image = sprite_sheet.get_image(130, 268, 114, 118)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale(image, (70, 70))
        self.WINDCHICKEN.append(image)

        sprite_sheet = SpriteSheet("ToxicBarrel.png")
        image = sprite_sheet.get_image(1, 1, 127, 116)
        self.TOXICBUBBLE.append(image)
        image = sprite_sheet.get_image(130, 1, 127, 116)
        self.TOXICBUBBLE.append(image)
        image = sprite_sheet.get_image(259, 1, 127, 116)
        self.TOXICBUBBLE.append(image)
        image = sprite_sheet.get_image(388, 1, 127, 116)
        self.TOXICBUBBLE.append(image)
        image = sprite_sheet.get_image(517, 1, 127, 116)
        self.TOXICBUBBLE.append(image)
        image = sprite_sheet.get_image(646, 1, 127, 116)
        self.TOXICBUBBLE.append(image)

        image = sprite_sheet.get_image(775, 1, 127, 116)
        self.TOXICDIRTY.append(image)

        image = sprite_sheet.get_image(904, 1, 127, 116)
        self.TOXICCLEEN.append(image)

        image = sprite_sheet.get_image(1033, 1, 127, 116)
        self.TOXICGRAFFITI.append(image)
        
        self.image = self.TRASHCAN[0]
        self.rect = self.image.get_rect()

        self.theflag = 0
        self.flagGo = 0

        self.Tcan = 0
        self.TcanGo = 0

        self.theChicken = 0
        self.theChickenGo = 0

        self.thechime = 0
        self.chimeGo = 0

        self.ToxicBubbling = 0
        self.ToxicBubblingGo = 0

        self.Sludge = 0
        self.SludgeGo = 0

        self.SludgeBack = 0
        self.SludgeBackGo = 0
        
        self.direction = "TRASHCAN"
        self.ObjType = ''
        self.ObjFace = ''
    def update(self):
        
        self.theflag += self.flagGo
        self.thechime += self.chimeGo
        self.theChicken += self.theChickenGo
        self.Tcan += self.TcanGo
        self.ToxicBubbling += self.ToxicBubblingGo
        self.Sludge += self.SludgeGo
        self.SludgeBack += self.SludgeBackGo

        if self.direction == "TOXICBUBBLE":
            self.ToxicBubblingGo = 1
            frame = (self.ToxicBubbling // 25) % len(self.TOXICBUBBLE)
            self.image = self.TOXICBUBBLE[frame]
        if self.direction != "TOXICBUBBLE":
            self.ToxicBubbling = 0

        if self.direction == "TOXICGRAFFITI":
            self.image = self.TOXICGRAFFITI[0]

        if self.direction == "TOXICCLEEN":
            self.image = self.TOXICCLEEN[0]

        if self.direction == "TOXICCLEEN":
            self.image = self.TOXICCLEEN[0]

        if self.direction == "TRASHCAN":
            self.TcanGo = 1
            frame = (self.Tcan // 25) % len(self.TRASHCAN)
            self.image = self.TRASHCAN[frame]
        if self.direction != "TRASHCAN":
            self.Tcan = 0
            
        if self.direction == "FLAG":
            self.flagGo = 1
            frame = (self.theflag // 25) % len(self.FLAG)
            self.image = self.FLAG[frame]
        if self.direction != "FLAG":
            self.theflag = 0

        if self.direction == "CHIMES":
            self.chimeGo = 1
            frame = (self.thechime // 20) % len(self.CHIMES)
            self.image = self.CHIMES[frame]
        if self.direction != "CHIMES":
            self.thechime = 0

        if self.direction == "CHICKEN":
            self.theChickenGo = 1
            frame = (self.theChicken // 10) % len(self.WINDCHICKEN)
            self.image = self.WINDCHICKEN[frame]
        if self.direction != "CHICKEN":
            self.theChicken = 0
