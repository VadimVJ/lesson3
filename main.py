import pygame
import random
pygame.init()

screen_widht = 800
scren_hight = 600
screen = pygame.displey.set_mode((screen_widht,scren_hight))

pygame.displey.set_caption("ИГРА ТИР")
icon = pygame.image.load("img/archer.jpg")
icon = pygame.image.load("img/archer.jpg")
pygame.displey.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_widht=80
target_hight=80

target_x = random.randint(0, SCREEN_WIGHT - target_wight)
target_y = random.randint(0, SCREEN_HIGHT - target_hight)

color = (random.randint(0,255), random.randint( 0,255), random.randint(0,255))


running = True
while running:
    pass
    screen.fill(color)
    for event in paygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.get.pos()
            if target_x < mouse_x < target_x + target_widht and target_y < mouse_y < target_y + target_hight:
                target_x = random.randint(0, SCREEN_WIGHT - target_wight)
                target_y = random.randint(0, SCREEN_HIGHT - target_hight)

    screen.blit(target_img,(target_x,target_y))
    pygame.display.update()

pygame.quit()
