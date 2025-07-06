import pygame, os
from assets import levels

pygame.init()
pygame.mixer.init()

current_level = levels.level1()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
size = [1550,600]
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 44)
text = font.render('Press Q to Quit', True, BLACK)
text_controls = font.render('Keys  "x"=fullscreen,  "z"=windowed,  hold  "m"=slowtime  and  "n"=fastforward', True, BLACK)
fps=60

class MixIt(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.backgroundMusic = pygame.mixer.Sound(
            os.path.join(os.path.dirname(__file__), "BackMus1.wav")
        )
        self.mix = pygame.mixer.Channel(1)

    def update(self):
        self.sound1()

    def sound1(self):
        if not self.mix.get_busy():  # only play if not already playing
            self.mix.play(self.backgroundMusic, loops=-1)  # loop forever

mix = MixIt()
mix.sound1()  # start looping music

while True:
    events = pygame.event.get()
    for event in events:  
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:           
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == pygame.K_m:
                fps=30
            if event.key == pygame.K_n:
                fps=280
            if event.key == pygame.K_x:
                screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
            if event.key == pygame.K_z:
                screen = pygame.display.set_mode(size)

        if event.type == pygame.KEYUP:           
            if event.key == pygame.K_m:
                fps=60
            if event.key == pygame.K_n:
                fps=60
            
    current_level.update()
    current_level.draw(screen)
    screen.blit(text, [10, 10])
    screen.blit(text_controls, [10, 40])
    clock.tick(fps)
    pygame.display.update()
pygame.quit()


