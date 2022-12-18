import pygame
import random
from Button_class import Button
from question import *
from blit_text import blit_text
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
        self.rect.center = (WIDTH*3 / 17, HEIGHT*4 / 13)


pygame.init()
pygame.mixer.music.load("Gimny_-_Gosudarstvennyjj_gimn_Rossijjskojj_ederacii_48240966.mp3")
pygame.mixer.music.play(loops = -1, fade_ms = 60)
all_sprites = pygame.sprite.Group()
akinator = Jeenie()
all_sprites.add(akinator)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Угадаю, какой регион России ты загадал!')
pygame.display.set_icon(pygame.image.load('russianflag.bmp'))
screen.fill((255, 254, 112))
comicsans_font2 = pygame.font.SysFont("Comic Sans", 25)
comicsans_font3 = pygame.font.SysFont("Comic Sans", 20)
rules_l1 = comicsans_font2.render("Правила игры", True, (130, 0, 140))
rules_l2 = comicsans_font2.render("Вы загадываете какой-то субъект России,", True, (130, 0, 140))
rules_l3 = comicsans_font2.render(" а Джинн с помощью ваших ответов его угадывает.", True, (130, 0, 140))
rules_l4 = comicsans_font2.render("Все просто, нужно лишь немного вспомнить географию!", True, (130, 0, 140))
rules_l5 = comicsans_font3.render('Для ответов на вопроcы используйте кнопки на экране', True, (140, 0, 100))
rules_l6 = comicsans_font3.render('Для всплывания окна с вопросом используйте клавишу Q', True, (150, 0, 90))

first=Question('Правила игры \n Вы загадываете какой-то субъект России, \nа Джинн с помощью ваших ответов его угадывает. \n Все просто, нужно лишь немного вспомнить географию! \n Для ответов на вопроcы используйте кнопки на экране \n Ну что, начнём?',yes=oblast,no=None)
first.no=first
title=first
def myFunction():
    global title
    if type(title)!=Replica:
        title=title.next_yes()
        if type(title)==Replica:
           title.replica='Была загадана '+title.replica+' ?'
    if type(title)==Replica:
        phrases=["Изи катка","Загадывай лучше"," Это в очередной раз доказывает, что искуственный сильнее обычного"]
        r=random.randint(0,2)
        title=Question(phrases[r]+'\n Сыграем ещё?',oblast,'quit')





def myFunction1():
    global title
    if type(title)!=Replica:
        title=title.next_no()
        if type(title)==Replica:
           title.replica='Была загадана '+title.replica+' ?'
    if type(title)==Replica:
        phrases=["Звездишь!!!","Ты бы хоть ответы на предыдущие вопросы запоминал!!!"," Ну я так не играю!!"]
        r=random.randint(0,2)
        title=Question(phrases[r]+'\n Сыграем ещё?',oblast,'quit')



bt=Button(buttonText= 'Да', screen=screen,font=pygame.font.SysFont("Comic Sans", 45),onclickFunction=myFunction,x=50, y=400, width= 250, height=150,color1=GREEN,color2=DARKGREEN,color3=WHITE)
bt2=Button(buttonText= 'Нет', screen=screen,font=pygame.font.SysFont("Comic Sans", 45),onclickFunction=myFunction1,x=500, y=400, width= 250,height=150,color1=RED,color2=DARKRED,color3=WHITE)
clock = pygame.time.Clock()
FPS = 60

flagRunning = True
while flagRunning:
    screen.fill((255, 254, 112))
    bt.process()
    bt2.process()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flagRunning = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                myFunction()
                pygame.display.flip()
            if event.key == pygame.K_RIGHT:
                myFunction1()
                pygame.display.flip()

    clock.tick(FPS)



    #pygame.draw.rect(screen, GREY, [WIDTH / 2, HEIGHT / 2, 140, 40])
    #screen.blit(text, (WIDTH / 2 + 50, HEIGHT / 2 + 10))
    all_sprites.draw(screen)
    pygame.draw.rect(screen, WHITE, (290, 50, 500, 250))
    #screen.blit(comicsans_font2.render(title.replica, True, (130, 0, 140)), (360, 60))
    blit_text(text=title.replica,pos=[300,60],xs=800,ys=600,surface=screen,color=(130, 0, 140),font=comicsans_font3)

    pygame.display.flip()




pygame.quit()