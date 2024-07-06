import paygame
import random
paygame.init()

screen_widht = 800
scren_hight = 600
screen = paygame.displey.set_mode((screen_widht,scren_hight))

paygame.displey.set_caption("ИГРА ТИР")
icon = paygame.image.load("img/1642365819_1-papik-pro-p-tir-klipart-1.png")
paygame.displey.set_icon(icon)

target_img = paygame.image.load("img/target.png")
target_widht=80
target_hight=80

target_x = random.randint(0, screen_wight - target_wight)
target_y = random.randint(0, screen_hight - target_hight)

color(random.randint(0,255), random.randint( 0,255), random.randint(0,255)


running = True
while running:
    pass

paygame.quit()
