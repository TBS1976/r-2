import pygame
import self


class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super(Bg,self).__init__()
        bg_beijing = pygame.image.load('bj1.png').convert_alpha()
        background_color = bg_beijing.subsurface((0,0,512,320))
        self.surf = pygame.transform.scale(background_color,(1080,640))
        self.rect = self.surf.get_rect(left=0,top=0)
class Cat(pygame.sprite.Sprite):
    def __init__(self):
        super(Cat,self).__init__()
        self.surf = pygame.image.load('rw1.png').convert_alpha()
        self.rect = self.surf.get_rect(center = (207,160))

    def update(self,keys):
        if keys[pygame.K_UP]:
            self.rect.move_ip((0,-1))
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip((0,1))
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip((-1,0))
        elif keys[pygame.K_RIGHT]:
            self.rect.move_ip((1,0))

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 1080:
            self.rect.right = 1080
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 640:
            self.rect.bottom = 640

class Marmot(pygame.sprite.Sprite):
    def __init__(self):
        super(Marmot,self).__init__()
        self.surf = pygame.image.load('rw2.png').convert_alpha()
        self.rect = self.surf.get_rect(center = (500,370))
        
def main():
    pygame.init()
    pygame.display.set_caption('土拨鼠制作')
    win = pygame.display.set_mode((1080,640))

    bg = Bg()
    cat = Cat()
    marmot = Marmot()
    all_sprites = [bg,cat,marmot]

    pygame.mixer.music.load("yy1.flac")
    pygame.mixer.music.play(-1)
    done = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        cat.update(keys)
        for sprite in all_sprites:
            win.blit(sprite.surf, sprite.rect)
        pygame.display.flip()

main()
