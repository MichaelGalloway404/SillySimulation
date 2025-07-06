import pygame,random
from .spritesheet_functions import SpriteSheet
from .MaleTshirtFrames import maletshirtframes
from . import NpcObjects

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([2, 2])
        self.image.fill((255,0,32))
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.rect.x = 0
        self.changex = 0
        self.changey = 0
        self.dir = 'right'
    def update(self):
        if self.dir == 'right':
            self.changex = 30
            self.changey = 0
        if self.dir == 'left':
            self.changex = -30
            self.changey = 0
        self.rect.x += self.changex
        self.rect.y += self.changey
        
class NPC(maletshirtframes):
    def __init__(self):
        super().__init__()
        self.change_x = 0
        self.change_y = 0
        self.direction = "RIGHT"

        self.THEobject = NpcObjects.NpcObject()
        
        self.Object_List = ["HOTDOG","HAMBUGER","FRIES","PICKLE",
                            "ICECREAM","SAUSAGE","TACO","CANDYBAR",
                            "DONUT","PIZZA","EGG","DRUMSTICK","SANDWICH",
                            "BROCCOLI","CARROT","LOLLY","FLAPJACKS","GUN"]
        
        self.Actions_list_Fullinv = ["RIGHT","LEFT","BREETH","EATLEFT","EATRIGHT","THROWLEFT","THROWRIGHT"]
        self.Actions_list_Emptyinv = ["RIGHT","LEFT","BREETH"]
        self.Aframe = ""
        self.thecounter = 0
        self.Right = 0
        self.Left = 0
        self.Breeth = 0
        self.Grabright = 0
        self.Grableft = 0   
        self.Sitright = 0
        self.Sitleft = 0
        self.Seatedright = 0
        self.Seatedleft = 0
        self.Getupright = 0
        self.Getupleft = 0
        self.Throwright = 0
        self.Throwleft = 0
        self.Eatright = 0
        self.Eatleft = 0
        self.Pickupright = 0
        self.Pickupleft = 0
        self.Atkleft = 0
        self.Atkright = 0
        self.invintory = []
        
        self.fraise_checkList = []
        
        self.GRABRVarchoice = True
        self.GrabrandVar = 0
        self.SITRVarchoice = True
        self.SitrandVar = 0
        self.PICKUPVarchoice = True
        self.PickuprandVar = 0
        
        self.BreethVarChoice = True
        self.RightVarChoice = True
        self.LeftVarChoice = True
        self.EatRightVarChoice = True
        self.EatLeftVarChoice = True
        self.SeatedRightVarChoice = True
        self.SeatedLeftVarChoice = True
        self.ChoiceVarRand = 0
        self.LeftSpeed = -2
        self.RightSpeed = 2

        self.OverLapC = True
        self.CanPickUpR = True
        self.CanPickUpL = True
        self.CanGrabL = True
        self.CanGrabR = True
        
        self.CanSitR = True
        self.CanSitL = True

        self.JumpChoy = True
        self.AtkChoy = True
        self.randAtkvar = 188
        self.randjumpvar = 88
        
        self.Name = "clown"
        self.bullet = Block()
        self.HasGun = False
        self.alive = True
        self.Mess = 1
    def update(self):
        self.rect.x += self.change_x  
        self.rect.y += self.change_y
        
        if (pygame.key.get_pressed()[pygame.K_c]):
            print('clown  ',self.invintory)
            self.alive = False

        if (pygame.key.get_pressed()[pygame.K_y]):
            print(self.SitrandVar)

        self.WalkDirection()
        self.Breething()        
        self.Grabbing()      
        self.Collision()
        self.calc_grav()
        self.frames()
        self.frameAction()
        self.Throwing()
        self.Eating()
        self.PickingUp()
        self.Sitting()
        self.Attacking()
        self.ProjectileHit()
        self.dead()

    def WalkDirection(self):
        if self.rect.left < self.boundary_left:
            self.change_x = self.RightSpeed
            self.direction = "RIGHT"
        if self.direction == "RIGHT":
            if self.RightVarChoice == True:
                self.ChoiceVarRand = random.randint(50,300)
                self.RightSpeed = random.randint(1,8)
                self.RightVarChoice = False
            self.change_x = self.RightSpeed
            if self.Right == self.ChoiceVarRand:
                self.choices()
        if self.direction != "RIGHT":  
            self.RightVarChoice = True
            
        if self.rect.left > self.boundary_right:
            self.change_x = self.LeftSpeed
            self.direction = "LEFT"
        if self.direction == "LEFT":
            if self.LeftVarChoice == True:
                self.ChoiceVarRand = random.randint(50,300)
                self.LeftSpeed = random.randint(-8,-1)
                self.LeftVarChoice = False
            self.change_x = self.LeftSpeed
            if self.Left == self.ChoiceVarRand:
                self.choices()
        if self.direction != "LEFT":  
            self.LeftVarChoice = True
        
    def Breething(self):
        if self.direction == "BREETH": #when breething this loop is continouse
            self.change_x = 0
            if self.BreethVarChoice == True: #the loop steps through this and the rest over and over
                self.ChoiceVarRand = random.randint(50,300)
                self.BreethVarChoice = False #but this omits ^^ from the loop unitil its turned back on
            if self.Breeth == self.ChoiceVarRand:
                self.Breeth = 0 # in case he decides to breeth 2x hes wont breeth forever!!
                self.choices()
        if self.direction != "BREETH":  #if the loop is exited 
            self.BreethVarChoice = True #only then is the choice TURNED BACK ON!

    def Eating(self):
        if self.direction == "EATLEFT":
            self.level.NPCs.move_to_front(self)
            self.change_x = 0
            if self.EatLeftVarChoice == True:
                self.ChoiceVarRand = random.randint(50,300)
                self.EatLeftVarChoice = False
            if self.Eatleft == self.ChoiceVarRand:
                self.Eatleft = 0
                if self.Aframe in self.invintory:
                    self.invintory.remove(self.Aframe)
                    print('clown Consummed','  ',self.Aframe)
                self.choices()
        if self.direction != "EATLEFT":
            self.EatLeftVarChoice = True
                
        if self.direction == "EATRIGHT":
            self.level.NPCs.move_to_front(self)
            self.change_x = 0
            if self.EatRightVarChoice == True:
                self.ChoiceVarRand = random.randint(50,300)
                self.EatRightVarChoice = False
            if self.Eatright == self.ChoiceVarRand:
                self.Eatright = 0
                if self.Aframe in self.invintory:
                    self.invintory.remove(self.Aframe)
                    print('clown Consummed','  ',self.Aframe)
                self.choices()
        if self.direction != "EATRIGHT":
            self.EatRightVarChoice = True
        
    def Sitting(self):
        chair_hit = pygame.sprite.spritecollide(self, self.level.BackObj, False)
        for obj in self.level.BackObj:
            if obj.ObjType == 'SEET':
                if self.rect.left+33 < obj.rect.right and self.rect.right-33 > obj.rect.left:
                    if self.SITRVarchoice == True:
                        self.SitrandVar = random.randint(1,100)
                        self.SITRVarchoice = False
                if not chair_hit:
                    self.SITRVarchoice = True
            npc_seated_hit = pygame.sprite.spritecollide(self, self.level.NPCs_seated, False)                        
            if obj.ObjType == 'SEET' and obj.ObjFace == 'RIGHT' and not npc_seated_hit:# and self.CanSitR == True:
                if self.rect.left+74 < obj.rect.right-((obj.rect.width/2)+1) and self.rect.right-74 > obj.rect.left+((obj.rect.width/2)-1) and self.SitrandVar in range(1,20):
                    self.change_x = 0
                    self.direction = "SEATEDRIGHT"
                    self.SitrandVar = 88
                                
            if obj.ObjType == 'SEET' and obj.ObjFace == 'LEFT' and not npc_seated_hit:# and self.CanSitL == True:
                if self.rect.left+74 < obj.rect.right-((obj.rect.width/2)+1) and self.rect.right-74 > obj.rect.left+((obj.rect.width/2)-1) and self.SitrandVar in range(1,20):
                    self.change_x = 0
                    self.direction = "SEATEDLEFT"
                    self.SitrandVar = 88
                    
            if self.direction == "SEATEDLEFT":
                self.level.NPCs_seated.add(self)
                self.level.NPCs.remove(self)
                if self.SeatedLeftVarChoice == True:
                    self.ChoiceVarRand = random.randint(50,300)
                    self.SeatedLeftVarChoice = False
                if self.Seatedleft == self.ChoiceVarRand:
                    self.level.NPCs_seated.remove(self)
                    self.level.NPCs.add(self)
                    self.choices()
            if self.direction != "SEATEDLEFT":
                self.SeatedLeftVarChoice = True
                    
            if self.direction == "SEATEDRIGHT":
                self.level.NPCs_seated.add(self)
                self.level.NPCs.remove(self)
                if self.SeatedRightVarChoice == True:
                    self.ChoiceVarRand = random.randint(50,300)
                    self.SeatedRightVarChoice = False
                if self.Seatedright == self.ChoiceVarRand:
                    self.level.NPCs_seated.remove(self)
                    self.level.NPCs.add(self)
                    self.choices()
            if self.direction != "SEATEDRIGHT":
                self.SeatedRightVarChoice = True
                

    def PickingUp(self):
        pickup_hit = pygame.sprite.spritecollide(self, self.level.npc_object_real, False)
        if not pickup_hit:
            self.PICKUPVarchoice = True
            self.PickuprandVar = 88
            
        for NpC_obj in self.level.npc_object_real:
            if self.direction == "LEFT" and self.rect.left+42 < NpC_obj.rect.right-((NpC_obj.rect.width/2)+1) and self.rect.right-102 > NpC_obj.rect.left+((NpC_obj.rect.width/2)-1) and self.rect.bottom -10 < NpC_obj.rect.bottom:
                if self.PICKUPVarchoice == True:
                    self.PickuprandVar = random.randint(1,100)
                    self.PICKUPVarchoice = False
                if self.PickuprandVar in range(2,10):
                    self.direction = "PICKUPLEFT"
                    self.level.NPCs.move_to_front(self)
                    self.change_x = 0
                    currentChoicePicUp = NpC_obj.direction
                    self.Aframe = NpC_obj.direction
                    self.invintory.append(currentChoicePicUp)

            if self.direction == "RIGHT" and self.rect.left+102 < NpC_obj.rect.right-((NpC_obj.rect.width/2)+1) and self.rect.right-42 > NpC_obj.rect.left+((NpC_obj.rect.width/2)-1) and self.rect.bottom -10 < NpC_obj.rect.bottom:
                if self.PICKUPVarchoice == True:
                    self.PickuprandVar = random.randint(1,100)
                    self.PICKUPVarchoice = False
                if self.PickuprandVar in range(2,10):
                    self.direction = "PICKUPRIGHT"
                    self.level.NPCs.move_to_front(self)
                    self.change_x = 0
                    currentChoicePicUp = NpC_obj.direction
                    self.Aframe = NpC_obj.direction
                    self.invintory.append(currentChoicePicUp)
                    
            if self.direction == "PICKUPLEFT" and self.image == self.PICKUPLEFT[2] and self.rect.bottom -10 < NpC_obj.rect.bottom and self.rect.left+42 < NpC_obj.rect.right-((NpC_obj.rect.width/2)+1) and self.rect.right-102 > NpC_obj.rect.left+((NpC_obj.rect.width/2)-1):
                NpC_obj.kill()
                self.level.NPCs.move_to_front(self)
            if self.direction == "PICKUPRIGHT" and self.image == self.PICKUPRIGHT[2] and self.rect.bottom -10 < NpC_obj.rect.bottom and self.rect.left+102 < NpC_obj.rect.right-((NpC_obj.rect.width/2)+1) and self.rect.right-42 > NpC_obj.rect.left+((NpC_obj.rect.width/2)-1):
                NpC_obj.kill()
                self.level.NPCs.move_to_front(self)

        if self.direction == "PICKUPRIGHT" and self.image == self.PICKUPRIGHT[5]:
            self.choices()
                
        if self.direction == "PICKUPLEFT" and self.image == self.PICKUPLEFT[5]:
            self.choices()

    def Throwing(self):
        if self.direction == "THROWLEFT":
            self.level.NPCs.move_to_front(self)
            self.change_x = 0
            if self.direction == "THROWLEFT" and self.image == self.THROWLEFT[3]:
                if self.Aframe in self.invintory:
                    self.invintory.remove(self.Aframe)
                self.choices()

        if self.direction == "THROWRIGHT":
            self.level.NPCs.move_to_front(self)
            self.change_x = 0
            if self.direction == "THROWRIGHT" and self.image == self.THROWRIGHT[3]:
                if self.Aframe in self.invintory:
                    self.invintory.remove(self.Aframe)
                    self.choices()
                
    def Grabbing(self):
        for obj in self.level.BackObj:
            if obj.direction == 'TRASHCAN':
                if self.rect.left+33 < obj.rect.left and self.rect.right-33 > obj.rect.right:
                    if self.GRABRVarchoice == True:
                        self.GrabrandVar = random.randint(1,100)
                        self.GRABRVarchoice = False
                else:
                    self.GRABRVarchoice = True
                   
                if self.direction == "LEFT" and self.rect.left+26 < obj.rect.right-(obj.rect.width/2) and self.rect.right-120 > obj.rect.left+(obj.rect.width/2) and self.GrabrandVar in range(1,25):
                    self.change_x =0
                    self.currentChoice = random.choice(self.Object_List)
                    self.invintory.append(self.currentChoice)
                    self.Aframe = self.currentChoice
                    self.direction = "GRABLEFT"
                    self.level.NPCs.move_to_front(self)
                                 
                if self.direction == "RIGHT" and self.rect.right-26 > obj.rect.left+(obj.rect.width/2) and self.rect.left+120 < obj.rect.right-(obj.rect.width/2) and self.GrabrandVar in range(1,25):
                    self.change_x =0
                    self.currentChoice = random.choice(self.Object_List)
                    self.invintory.append(self.currentChoice)
                    self.Aframe = self.currentChoice
                    self.direction = "GRABRIGHT"
                    self.level.NPCs.move_to_front(self)
                    
                if self.direction == "GRABLEFT" and self.image == self.GRABLEFT[4]:
                    self.level.NPCs.move_to_front(self)
                    self.choices()
                    self.GrabrandVar = 88
            
                if self.direction == "GRABRIGHT" and self.image == self.GRABRIGHT[4]:
                    self.level.NPCs.move_to_front(self)
                    self.choices()
                    self.GrabrandVar = 88

    def Collision(self):
        for person in self.level.NPCs:
            if person != self:
                if self.rect.left+33 < person.rect.left and self.rect.right-33 > person.rect.right:
                    if person.direction == "EATLEFT":
                        self.OverLapC = False
                    if person.direction == "EATRIGHT":
                        self.OverLapC = False
                    if person.direction == "THROWLEFT":
                        self.OverLapC = False
                    if person.direction == "THROWRIGHT":
                        self.OverLapC = False
                    if person.direction == "GRABRIGHT":
                        self.OverLapC = False
                    if person.direction == "GRABLEFT":
                        self.OverLapC = False
                    if person.direction == "PICKUPRIGHT":
                        self.OverLapC = False
                    if person.direction == "PICKUPLEFT":
                        self.OverLapC = False
                else:
                    self.OverLapC = True

    def choices(self):
        if len(self.invintory) > 0 and self.Aframe in self.invintory and self.OverLapC == True:
            self.direction = random.choice(self.Actions_list_Fullinv)
            self.Aframe = random.choice(self.invintory)
            if self.direction == "EATRIGHT" and self.Aframe == "GUN":
                self.direction = random.choice(self.Actions_list_Emptyinv)
            if self.direction == "EATLEFT" and self.Aframe == "GUN":
                self.direction = random.choice(self.Actions_list_Emptyinv)

        else:
            self.direction = random.choice(self.Actions_list_Emptyinv)

    def dead(self):
        if self.alive == False and self.Mess == 1:
            self.Mess = 0
            head = BloodyMess()
            head.rect.x = self.rect.x
            head.rect.y = self.rect.y
            head.direction = "HEADAIR"
            self.level.mess.add(head)
            
            torso = BloodyMess()
            torso.rect.x = self.rect.x
            torso.rect.y = self.rect.y
            torso.direction = "TORSOAIR"
            self.level.mess.add(torso)

            for x in range(2):
                leg = BloodyMess()
                leg.rect.x = self.rect.x
                leg.rect.y = self.rect.y
                leg.direction = "LEGAIR"
                self.level.mess.add(leg)

                arm = BloodyMess()
                arm.rect.x = self.rect.x
                arm.rect.y = self.rect.y
                arm.direction = "ARMAIR"
                self.level.mess.add(arm)
                

    def ProjectileHit(self):
        for bullets in self.level.Bullet:
            if self.rect.left < bullets.rect.left and self.rect.right > bullets.rect.right:
                self.alive = False
                self.kill()
       

            
    def Attacking(self):
        if "GUN" in self.invintory:
            self.HasGun = True
        else:
            self.HasGun = False
            
        for bullets in self.level.Bullet:
            if bullets.rect.right < 0:
                self.bullet.kill()
            if bullets.rect.right > 2000:
                self.bullet.kill()
                
        for person in self.level.NPCs:
            if person != self and self.HasGun == True:
                if self.rect.left+70 > person.rect.left-90 and self.rect.right-70 < person.rect.right+90:
                    if self.AtkChoy == True:
                        self.randAtkvar = random.randint(1,100)
                        print(self.randAtkvar)
                        self.AtkChoy = False
                else:
                    self.AtkChoy = True
                if self.randAtkvar in range(1,11) and self.direction == "RIGHT":
                    self.change_x = 0
                    self.direction = "ATKRIGHT"
                    self.level.NPCs.move_to_front(self)
                    self.bullet.rect.x = self.rect.x +180
                    self.bullet.rect.y = self.rect.y + 45
                    self.bullet.dir = 'right'
                    self.level.Bullet.add(self.bullet)
                
                    
                if self.randAtkvar in range(1,11) and self.direction == "LEFT":
                    self.change_x = 0
                    self.direction = "ATKLEFT"
                    self.level.NPCs.move_to_front(self)
                    self.bullet.rect.x = self.rect.x
                    self.bullet.rect.y = self.rect.y + 45
                    self.bullet.dir = 'left'
                    self.level.Bullet.add(self.bullet)
        if self.Atkleft == 50:
            self.choices()
            self.randAtkvar = 88
            self.Atkleft = 0
        if self.Atkright == 50:
            self.choices()
            self.randAtkvar = 88
            self.Atkright = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        if platform_hit_list:
            if self.change_y >= 0:
                self.change_y = 0
        
            
    def jump(self):
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        if len(platform_hit_list) > 0:
            self.change_y = -3
            for plat in self.level.platform_list:
                if self.rect.bottom > plat.rect.top:
                    self.rect.bottom = plat.rect.top
            
    def frames(self):
        self.Right += self.thecounter
        self.Left += self.thecounter
        self.Breeth += self.thecounter
        self.Grabright += self.thecounter
        self.Grableft += self.thecounter
        self.Seatedright += self.thecounter
        self.Seatedleft += self.thecounter    
        self.Throwright += self.thecounter
        self.Throwleft += self.thecounter
        self.Eatright += self.thecounter
        self.Eatleft += self.thecounter
        self.Pickupleft += self.thecounter
        self.Pickupright += self.thecounter
        self.Atkleft += self.thecounter
        self.Atkright += self.thecounter
        
        self.thecounter = 1
        if self.direction == "ATKLEFT":
            frame = (self.Atkleft // 33) % len(self.ATKLEFT)
            self.image = self.ATKLEFT[frame]
        if self.direction != "ATKLEFT":
            self.Atkleft = 0

        if self.direction == "ATKRIGHT":
            frame = (self.Atkright // 33) % len(self.ATKRIGHT)
            self.image = self.ATKRIGHT[frame]
        if self.direction != "ATKRIGHT":
            self.Atkright = 0
            
        if self.direction == "PICKUPRIGHT":
            frame = (self.Pickupright // 33) % len(self.PICKUPRIGHT)
            self.image = self.PICKUPRIGHT[frame]
        if self.direction != "PICKUPRIGHT":
            self.Pickupright = 0
        
        if self.direction == "PICKUPLEFT":
            frame = (self.Pickupleft // 33) % len(self.PICKUPLEFT)
            self.image = self.PICKUPLEFT[frame]
        if self.direction != "PICKUPLEFT":
            self.Pickupleft = 0

        if self.direction == "GRABRIGHT":
            frame = (self.Grabright // 15) % len(self.GRABRIGHT)
            self.image = self.GRABRIGHT[frame]
        if self.direction != "GRABRIGHT":
            self.Grabright =0

        if self.direction == "GRABLEFT":
            frame = (self.Grableft // 15) % len(self.GRABLEFT)
            self.image = self.GRABLEFT[frame]
        if self.direction != "GRABLEFT":
            self.Grableft =0

        if self.direction == "RIGHT":
            frame = (self.Right // 11) % len(self.RIGHT)
            self.image = self.RIGHT[frame]
        if self.direction != "RIGHT":
            self.Right = 0
            
        if self.direction == "LEFT":
            frame = (self.Left// 11) % len(self.LEFT)
            self.image = self.LEFT[frame]
        if self.direction != "LEFT":
            self.Left = 0

        if self.direction == "BREETH":
            frame = (self.Breeth // 15) % len(self.BREETH)
            self.image = self.BREETH[frame]
        if self.direction != "BREETH":
            self.Breeth = 0

        if self.direction == "SEATEDRIGHT":
            frame = (self.Seatedright // 33) % len(self.SEATEDRIGHT)
            self.image = self.SEATEDRIGHT[frame]
        if self.direction != "SEATEDRIGHT":
            self.Seatedright = 0

        if self.direction == "SEATEDLEFT":
            frame = (self.Seatedleft // 33) % len(self.SEATEDLEFT)
            self.image = self.SEATEDLEFT[frame]
        if self.direction != "SEATEDLEFT":
            self.Seatedleft = 0

        if self.direction == "THROWRIGHT":
            frame = (self.Throwright // 11) % len(self.THROWRIGHT)
            self.image = self.THROWRIGHT[frame]
        if self.direction != "THROWRIGHT":
            self.Throwright = 0

        if self.direction == "THROWLEFT":
            frame = (self.Throwleft // 11) % len(self.THROWLEFT)
            self.image = self.THROWLEFT[frame]
        if self.direction != "THROWLEFT":
            self.Throwleft = 0

        if self.direction == "EATRIGHT":
            frame = (self.Eatright // 22) % len(self.EATRIGHT)
            self.image = self.EATRIGHT[frame]
        if self.direction != "EATRIGHT":
            self.Eatright = 0

        if self.direction == "EATLEFT":
            frame = (self.Eatleft // 22) % len(self.EATLEFT)
            self.image = self.EATLEFT[frame]
        if self.direction != "EATLEFT":
            self.Eatleft = 0
            
    def frameAction(self):
        self.THEobject.direction = self.Aframe
        if self.direction == "ATKRIGHT":
            self.Aframe = "GUNRIGHT"
            self.THEobject.rect.x =self.rect.x +109
            self.THEobject.rect.y =self.rect.y +0
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "ATKLEFT":
            self.Aframe = "GUNLEFT"
            self.THEobject.rect.x =self.rect.x +0
            self.THEobject.rect.y =self.rect.y +0
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "PICKUPLEFT" and self.image == self.PICKUPLEFT[2]:
            self.THEobject.rect.x =self.rect.x +24
            self.THEobject.rect.y =self.rect.y +71
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "PICKUPLEFT" and self.image == self.PICKUPLEFT[3]:
            self.THEobject.rect.x =self.rect.x +29
            self.THEobject.rect.y =self.rect.y +56
        elif self.direction == "PICKUPLEFT" and self.image == self.PICKUPLEFT[4]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "PICKUPLEFT" and self.image == self.PICKUPLEFT[5]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19

        elif self.direction == "PICKUPRIGHT" and self.image == self.PICKUPRIGHT[2]:
            self.THEobject.rect.x =self.rect.x +86
            self.THEobject.rect.y =self.rect.y +71
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "PICKUPRIGHT" and self.image == self.PICKUPRIGHT[3]:
            self.THEobject.rect.x =self.rect.x +81
            self.THEobject.rect.y =self.rect.y +56
        elif self.direction == "PICKUPRIGHT" and self.image == self.PICKUPRIGHT[4]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "PICKUPRIGHT" and self.image == self.PICKUPRIGHT[5]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
        
        elif self.direction == "THROWRIGHT" and self.image == self.THROWRIGHT[0]:
            self.THEobject.rect.x =self.rect.x -1
            self.THEobject.rect.y =self.rect.y -15
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "THROWRIGHT" and self.image == self.THROWRIGHT[1]:
            self.THEobject.rect.x =self.rect.x -1
            self.THEobject.rect.y =self.rect.y -15
        elif self.direction == "THROWRIGHT" and self.image == self.THROWRIGHT[2]:
            self.THEobject.rect.x =self.rect.x +55
            self.THEobject.rect.y =self.rect.y -45
        elif self.direction == "THROWRIGHT" and self.image == self.THROWRIGHT[3]:
            OGJright = NpcObjects.NpcObject()
            OGJright.rect.x =self.rect.x +55
            OGJright.rect.y =self.rect.y -45
            OGJright.direction = self.Aframe
            OGJright.gravity = 'on'
            OGJright.change_x = random.randrange(1,10)
            self.level.npc_object_real.add(OGJright)
            self.level.NPCObj.remove(self.THEobject)
            
        elif self.direction == "THROWLEFT" and self.image == self.THROWLEFT[0]:
            self.THEobject.rect.x =self.rect.x +109
            self.THEobject.rect.y =self.rect.y -14
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "THROWLEFT" and self.image == self.THROWLEFT[1]:
            self.THEobject.rect.x =self.rect.x +109
            self.THEobject.rect.y =self.rect.y -14
        elif self.direction == "THROWLEFT" and self.image == self.THROWLEFT[2]:
            self.THEobject.rect.x =self.rect.x +52
            self.THEobject.rect.y =self.rect.y -45
        elif self.direction == "THROWLEFT" and self.image == self.THROWLEFT[3]:
            OGJleft = NpcObjects.NpcObject()
            OGJleft.rect.x =self.rect.x +52
            OGJleft.rect.y =self.rect.y -45
            OGJleft.direction = self.Aframe
            OGJleft.gravity = 'on'
            OGJleft.change_x = random.randrange(-10,-1)
            self.level.npc_object_real.add(OGJleft)
            self.level.NPCObj.remove(self.THEobject)
            
        elif self.direction == "GRABLEFT" and self.image == self.GRABLEFT[0]:            
            self.level.NPCObj.remove(self.THEobject)
        elif self.direction == "GRABLEFT" and self.image == self.GRABLEFT[2]:
            self.THEobject.rect.x =self.rect.x +3
            self.THEobject.rect.y =self.rect.y +12
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "GRABLEFT" and self.image == self.GRABLEFT[3]:
            self.THEobject.rect.x =self.rect.x +70
            self.THEobject.rect.y =self.rect.y +45
        elif self.direction == "GRABLEFT" and self.image == self.GRABLEFT[4]:
            self.THEobject.rect.x =self.rect.x +70
            self.THEobject.rect.y =self.rect.y +45

        elif self.direction == "GRABRIGHT" and self.image == self.GRABRIGHT[0]:
            self.level.NPCObj.remove(self.THEobject)
        elif self.direction == "GRABRIGHT" and self.image == self.GRABRIGHT[2]:
            self.THEobject.rect.x =self.rect.x +105
            self.THEobject.rect.y =self.rect.y +12
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "GRABRIGHT" and self.image == self.GRABRIGHT[3]:
            self.THEobject.rect.x =self.rect.x +39
            self.THEobject.rect.y =self.rect.y +45
        elif self.direction == "GRABRIGHT" and self.image == self.GRABRIGHT[4]:
            self.THEobject.rect.x =self.rect.x +39
            self.THEobject.rect.y =self.rect.y +45

        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[0]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[1]:
            self.THEobject.rect.x =self.rect.x +34
            self.THEobject.rect.y =self.rect.y -9
        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[2]:
            self.THEobject.rect.x =self.rect.x +25
            self.THEobject.rect.y =self.rect.y -7
        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[3]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[4]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[5]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[6]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[7]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATLEFT" and self.image == self.EATLEFT[8]:
            self.THEobject.rect.x =self.rect.x +41
            self.THEobject.rect.y =self.rect.y +19

        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[0]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
            self.level.NPCObj.add(self.THEobject)
        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[1]:
            self.THEobject.rect.x =self.rect.x +76
            self.THEobject.rect.y =self.rect.y -9
        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[2]:
            self.THEobject.rect.x =self.rect.x +80
            self.THEobject.rect.y =self.rect.y -7
        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[3]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[4]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[5]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[6]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[7]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
        elif self.direction == "EATRIGHT" and self.image == self.EATRIGHT[8]:
            self.THEobject.rect.x =self.rect.x +69
            self.THEobject.rect.y =self.rect.y +19
        else:
            self.level.NPCObj.remove(self.THEobject)                   
    
class BloodyMess(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.TORSOAIR = []
        self.TORSOGROUND = []
        self.LEGAIR = []
        self.LEGGROUND = []
        self.ARMAIR = []
        self.ARMGROUND = []
        self.HEADAIR = []
        self.HEADGROUND = []
        
        
        sprite_sheet = SpriteSheet("bluemanbloodymess.png")

        image = sprite_sheet.get_image(1, 131, 63, 63)
        self.HEADAIR.append(image)
        image = sprite_sheet.get_image(66, 131, 63, 63)
        self.HEADAIR.append(image)
        image = sprite_sheet.get_image(131, 131, 63, 63)
        self.HEADAIR.append(image)
        image = sprite_sheet.get_image(196, 131, 63, 63)
        self.HEADAIR.append(image)

        image = sprite_sheet.get_image(1, 196, 63, 63)
        self.HEADGROUND.append(image)
        image = sprite_sheet.get_image(66, 196, 63, 63)
        self.HEADGROUND.append(image)
        image = sprite_sheet.get_image(131, 196, 63, 63)
        self.HEADGROUND.append(image)
        image = sprite_sheet.get_image(196, 196, 63, 63)
        self.HEADGROUND.append(image)

        image = sprite_sheet.get_image(1, 1, 63, 63)
        self.ARMAIR.append(image)
        image = sprite_sheet.get_image(66, 1, 63, 63)
        self.ARMAIR.append(image)
        image = sprite_sheet.get_image(131, 1, 63, 63)
        self.ARMAIR.append(image)
        image = sprite_sheet.get_image(196, 1, 63, 63)
        self.ARMAIR.append(image)

        image = sprite_sheet.get_image(66, 66, 63, 63)
        self.ARMGROUND.append(image)
        image = sprite_sheet.get_image(196, 66, 63, 63)
        self.ARMGROUND.append(image)

        image = sprite_sheet.get_image(521, 1, 63, 63)
        self.TORSOAIR.append(image)
        image = sprite_sheet.get_image(586, 1, 63, 63)
        self.TORSOAIR.append(image)
        image = sprite_sheet.get_image(651, 1, 63, 63)
        self.TORSOAIR.append(image)
        image = sprite_sheet.get_image(716, 1, 63, 63)
        self.TORSOAIR.append(image)

        image = sprite_sheet.get_image(586, 66, 63, 63)
        self.TORSOGROUND.append(image)
        image = sprite_sheet.get_image(716, 66, 63, 63)
        self.TORSOGROUND.append(image)

        image = sprite_sheet.get_image(261, 1, 63, 63)
        self.LEGAIR.append(image)
        image = sprite_sheet.get_image(326, 1, 63, 63)
        self.LEGAIR.append(image)
        image = sprite_sheet.get_image(391, 1, 63, 63)
        self.LEGAIR.append(image)
        image = sprite_sheet.get_image(456, 1, 63, 63)
        self.LEGAIR.append(image)

        image = sprite_sheet.get_image(326, 66, 63, 63)
        self.LEGGROUND.append(image)
        image = sprite_sheet.get_image(456, 66, 63, 63)
        self.LEGGROUND.append(image)

        self.image = self.TORSOAIR[0]
        self.rect = self.image.get_rect()
        
        self.direction = "TORSOAIR"

        self.leg = 0
        self.torso = 0
        self.arm = 0
        self.head = 0
        
        self.framesGo = 0
        self.change_x = random.randrange(-10,10)
        self.change_y = random.randrange(-10,10)
    def update(self):
        self.calc_grav()
        self.rect.x += self.change_x  
        self.rect.y += self.change_y

        self.torso += self.framesGo
        self.leg += self.framesGo
        self.arm += self.framesGo
        self.head += self.framesGo
        self.framesGo = 1
        
        if self.direction == "HEADAIR":
            frame = (self.head // 10) % len(self.HEADAIR)
            self.image = self.HEADAIR[frame]
        if self.direction != "HEADAIR":
            self.head = 0
        if self.direction == "HEADGROUNDUP":
            self.image = self.HEADGROUND[0]
        if self.direction == "HEADGROUNDFACEDOWN":
            self.image = self.HEADGROUND[1]
        if self.direction == "HEADGROUNDUPSIDEDOWN":
            self.image = self.HEADGROUND[2]
        if self.direction == "HEADGROUNDFACEUP":
            self.image = self.HEADGROUND[3]
        if self.change_x == 0 and self.image == self.HEADAIR[0]:
            self.direction = "HEADGROUNDUP"
        if self.change_x == 0 and self.image == self.HEADAIR[1]:
            self.direction = "HEADGROUNDFACEDOWN"
        if self.change_x == 0 and self.image == self.HEADAIR[2]: 
            self.direction = "HEADGROUNDUPSIDEDOWN"
        if self.change_x == 0 and self.image == self.HEADAIR[3]:
            self.direction = "HEADGROUNDFACEUP"

        if self.direction == "ARMAIR":
            frame = (self.arm // 10) % len(self.ARMAIR)
            self.image = self.ARMAIR[frame]
        if self.direction != "ARMAIR":
            self.arm = 0
        if self.direction == "ARMGROUNDDOWN":
            self.image = self.ARMGROUND[0]
        if self.direction == "ARMGROUNDUP":
            self.image = self.ARMGROUND[1]
        if self.change_x == 0 and self.image == self.ARMAIR[0] or self.change_x == 0 and self.image == self.ARMAIR[1]:
            self.direction = "ARMGROUNDDOWN"
        if self.change_x == 0 and self.image == self.ARMAIR[2] or self.change_x == 0 and self.image == self.ARMAIR[3]:
            self.direction = "ARMGROUNDUP"

        if self.direction == "TORSOAIR":
            frame = (self.torso // 10) % len(self.TORSOAIR)
            self.image = self.TORSOAIR[frame]
        if self.direction != "TORSOAIR":
            self.torso = 0
        if self.direction == "TORSOGROUNDDOWN":
            self.image = self.TORSOGROUND[0]
        if self.direction == "TORSOGROUNDUP":
            self.image = self.TORSOGROUND[1]
        if self.change_x == 0 and self.image == self.TORSOAIR[0] or self.change_x == 0 and self.image == self.TORSOAIR[1]:
            self.direction = "TORSOGROUNDDOWN"
        if self.change_x == 0 and self.image == self.TORSOAIR[2] or self.change_x == 0 and self.image == self.TORSOAIR[3]:
            self.direction = "TORSOGROUNDUP"

        if self.direction == "LEGAIR":
            frame = (self.leg // 10) % len(self.LEGAIR)
            self.image = self.LEGAIR[frame]
        if self.direction != "LEGAIR":
            self.legleft = 0
        if self.direction == "LEGGROUNDDOWN":
            self.image = self.LEGGROUND[0]
        if self.direction == "LEGGROUNDUP":
            self.image = self.LEGGROUND[1]
        if self.change_x == 0 and self.image == self.LEGAIR[0] or self.change_x == 0 and self.image == self.LEGAIR[1]:
            self.direction = "LEGGROUNDDOWN"
        if self.change_x == 0 and self.image == self.LEGAIR[2] or self.change_x == 0 and self.image == self.LEGAIR[3]:
            self.direction = "LEGGROUNDUP"
            
    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

