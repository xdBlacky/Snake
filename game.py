import pygame
import random
pygame.init()

ScreenWidth = 500
ScreenHeight = 500

win = pygame.display.set_mode((ScreenWidth, ScreenHeight))

pygame.display.set_caption("Game")



def Snake():
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()


def Food():
    pygame.draw.rect(win, (0, 255, 0), (xFruit * 2, yFruit * 2, widthFruit, heightFruit))
    pygame.display.update()



xFruit = random.randrange(0, 250)
yFruit = random.randrange(0, 250)
widthFruit = 20
heightFruit = 20


x = 50
y = 50
width = 40
height = 40
vel = 10


run = True
while run:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= vel

    if keys[pygame.K_d]:
        x += vel

    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel

    if keys[pygame.K_f]:
        print(x)
        print(y)

    if keys[pygame.K_c]:
        print(xFruit)
        print(yFruit)

    if x > ScreenWidth - width:
        x = 0
    if x < 0:
        x = ScreenWidth - width

    if y > ScreenHeight - height:
        y = 0
    if y < 0:
        y = ScreenHeight - height



    win.fill((0, 0, 0))

    Food()

    Snake()

pygame.quit()
