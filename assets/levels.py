import pygame,random
from . import MaleTshirt, EvilMan
from . import BackGroundMISC, chairs


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (111, 111, 111)##(221, 242, 247)
size = [850,600]
screen = pygame.display.set_mode(size)

# floor 
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill((122,66,66))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
class Level():
    def __init__(self):
        self.level_limit = -1000
        self.music = pygame.sprite.LayeredUpdates()
        self.npc_object_real = pygame.sprite.LayeredUpdates()
        self.NPCs_seated = pygame.sprite.LayeredUpdates()
        self.NPCs = pygame.sprite.LayeredUpdates()
        self.platform_list = pygame.sprite.LayeredUpdates()
        self.BackObj = pygame.sprite.LayeredUpdates()
        self.NPCObj = pygame.sprite.LayeredUpdates()
        self.Bullet = pygame.sprite.LayeredUpdates()
        self.mess = pygame.sprite.LayeredUpdates()
        
    def update(self):
        self.NPCs_seated.update()
        self.NPCObj.update()
        self.NPCs.update()
        self.BackObj.update()
        self.platform_list.update()
        self.npc_object_real.update()
        self.Bullet.update()
        self.music.update()
        self.mess.update()

        for floor in self.platform_list:
            for obj in self.npc_object_real:
                if obj.rect.bottom > floor.rect.top:
                    obj.rect.bottom = floor.rect.top 
                    obj.change_x = 0
                    obj.change_y = 0
                    obj.gravity = 'off'
            for mess in self.mess:
                    if mess.rect.bottom >= floor.rect.top:
                        mess.change_x = 0
                        mess.change_y = 0
                        mess.rect.bottom = floor.rect.top
            for npc in self.NPCs:
                if npc.rect.bottom >= floor.rect.top:
                    npc.rect.bottom = floor.rect.top 
                    npc.change_y = 0
        
    def draw(self, screen):
        screen.fill(BLUE)
        self.platform_list.draw(screen)
        self.BackObj.draw(screen)
        self.NPCs_seated.draw(screen)
        self.NPCs.draw(screen)
        self.NPCObj.draw(screen)
        self.npc_object_real.draw(screen)
        self.Bullet.draw(screen)
        self.mess.draw(screen)
 
class level1(Level): 
    def __init__(self):
        Level.__init__(self)
        self.level_limit = -1256
        floor = Block(0,510,1650,1600,)
        self.platform_list.add(floor)

        for obj in self.platform_list:
            Trashcan = BackGroundMISC.backgroundOBJECT()
            Trashcan.rect.x = 400
            Trashcan.rect.bottom = obj.rect.top
            Trashcan.direction = "TRASHCAN"
            Trashcan.level = self
            self.BackObj.add(Trashcan)

            toxicBarrel = BackGroundMISC.backgroundOBJECT()
            toxicBarrel.rect.x = 100
            toxicBarrel.rect.bottom = obj.rect.top
            toxicBarrel.direction = "TOXICBUBBLE"
            toxicBarrel.level = self
            self.BackObj.add(toxicBarrel)

            benchL = chairs.SEET()
            benchL.rect.x = 700
            benchL.rect.bottom = obj.rect.top
            benchL.ObjType = 'SEET'
            benchL.ObjFace = 'RIGHT'
            benchL.direction = "BENCH"
            self.BackObj.add(benchL)

            benchR = chairs.SEET()
            benchR.rect.x = 1200
            benchR.rect.bottom = obj.rect.top
            benchR.ObjType = 'SEET'
            benchR.ObjFace = 'LEFT'
            benchR.direction = "BENCH"
            self.BackObj.add(benchR)

        for i in range(3):
            man = MaleTshirt.NPC()
            man.direction = 'LEFT'
            man.rect.x = 400
            man.level = self
            man.boundary_right = 1460
            man.boundary_left = 0
            self.NPCs.add(man)

            evilman = EvilMan.NPC()
            evilman.direction = 'LEFT'
            evilman.rect.x = random.randrange(500,600)
            evilman.level = self
            evilman.boundary_right = 1460
            evilman.boundary_left = 0
            self.NPCs.add(evilman)

