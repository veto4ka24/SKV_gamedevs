import pygame

GREEN = (109, 234, 117)
DARKGREEN = (40, 96, 51)
RED = (221, 68, 35)
DARKRED = (132, 24, 43)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

WIDTH = 800
HEIGHT = 600

class Jeenie(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load("jeenie.png"), (280, 370))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*3 / 13, HEIGHT*4 / 13)


pygame.init()
all_sprites = pygame.sprite.Group()
akinator = Jeenie()
all_sprites.add(akinator)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Угадаю, какой регион России ты загадал!')
pygame.display.set_icon(pygame.image.load('russianflag.bmp'))
screen.fill((255, 254, 112))

pygame.draw.rect(screen, GREEN, (50, 400, 250, 150))
pygame.draw.rect(screen, DARKGREEN, (50, 400, 250, 150), 8)
pygame.draw.rect(screen, RED, (500, 400, 250, 150))
pygame.draw.rect(screen, DARKRED, (500, 400, 250, 150), 8)
pygame.display.flip()

comicsans_font1 = pygame.font.SysFont("Comic Sans", 45)
text1 = comicsans_font1.render("Да", True, WHITE)
screen.blit(text1, (135, 455))
text2 = comicsans_font1.render("Нет", True, WHITE)
screen.blit(text2, (585, 455))
comicsans_font2 = pygame.font.SysFont("Comic Sans", 25)
comicsans_font3 = pygame.font.SysFont("Comic Sans", 20)
rules_l1 = comicsans_font2.render("Правила игры", True, (130, 0, 140))
rules_l2 = comicsans_font2.render("Вы загадываете какой-то субъект России,", True, (130, 0, 140))
rules_l3 = comicsans_font2.render(" а Джинн с помощью ваших ответов его угадывает.", True, (130, 0, 140))
rules_l4 = comicsans_font2.render("Все просто, нужно лишь немного вспомнить географию!", True, (130, 0, 140))
rules_l5 = comicsans_font3.render('Для ответов на вопросы используйте клавиши "ВПРАВО" и "ВЛЕВО"', True, (140, 0, 100))
rules_l6 = comicsans_font3.render('Для всплывания окна с вопросом используйте клавишу Q', True, (150, 0, 90))

clock = pygame.time.Clock()
FPS = 60

flagRunning = True
while flagRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flagRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                pygame.draw.rect(screen, WHITE, (30, 330, 740, 260))
                screen.blit(rules_l1, (290, 360))
                screen.blit(rules_l2, (120, 400))
                screen.blit(rules_l3, (70, 430))
                screen.blit(rules_l4, (70, 460))
                screen.blit(rules_l5, (70, 510))
                screen.blit(rules_l6, (95, 545))
            elif event.key == pygame.K_q:
                pygame.draw.rect(screen, WHITE, (340, 50, 400, 200))
            elif event.key == pygame.K_LEFT:
                pygame.draw.rect(screen, (10, 110, 50), (50, 400, 250, 150))
                #pygame.draw.rect(screen, DARKGREEN, (50, 400, 250, 150), 8)
                pygame.display.flip()
            elif event.key == pygame.K_RIGHT:
                pygame.draw.rect(screen, (120, 10, 60), (500, 400, 250, 150))
                pygame.display.flip()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_h:
                screen.fill((255, 254, 112))
                pygame.draw.rect(screen, GREEN, (50, 400, 250, 150))
                pygame.draw.rect(screen, DARKGREEN, (50, 400, 250, 150), 8)
                screen.blit(text1, (135, 455))
                pygame.draw.rect(screen, RED, (500, 400, 250, 150))
                pygame.draw.rect(screen, DARKRED, (500, 400, 250, 150), 8)
                screen.blit(text2, (585, 455))
                pygame.display.flip()
            elif event.key == pygame.K_LEFT:
                pygame.draw.rect(screen, GREEN, (50, 400, 250, 150))
                pygame.draw.rect(screen, DARKGREEN, (50, 400, 250, 150), 8)
                screen.blit(text1, (135, 455))
                pygame.display.flip()
            elif event.key == pygame.K_RIGHT:
                pygame.draw.rect(screen, RED, (500, 400, 250, 150))
                pygame.draw.rect(screen, DARKRED, (500, 400, 250, 150), 8)
                screen.blit(text2, (585, 455))
                pygame.display.flip()
    clock.tick(FPS)

    #pygame.draw.rect(screen, GREY, [WIDTH / 2, HEIGHT / 2, 140, 40])
    #screen.blit(text, (WIDTH / 2 + 50, HEIGHT / 2 + 10))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()