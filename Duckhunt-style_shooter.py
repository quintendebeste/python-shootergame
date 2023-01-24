import pymunk
import pygame as pg
import random

pg.init()
clock = pg.time.Clock()
x,y = (1920, 1020)
window = pg.display.set_mode((x, y))
red = (255,0,0)
white = (255,255,255)

pg.mouse.set_visible(False)

active_img = 'doomgun.png'
active_img_shoot = 'doomgun_low_shoot.png'
active_img_silent = 'doomgun_low.png'
space = pymunk.Space()
space.gravity = (0, 150)


def create_ball(space):
    body = pymunk.Body(1,100,body_type = pymunk.Body.DYNAMIC)
    body.position = (random.randint(100, x), 0)
    shape = pymunk.Circle(body,80)
    space.add(body, shape)
    return shape


balls = []
balls.append(create_ball(space))

def draw_balls(balls):
    for ball in balls:      
        x_pos = int(ball.body.position.x)
        y_pos = int(ball.body.position.y)
        pg.draw.circle(window, red, (x_pos, y_pos), 50)
    if(y_pos >= y + 50):
        balls.append(create_ball(space))


font = pg.font.SysFont('Corbel',100)
pointcounter = 0

running = True
while running:

    #image handling
    img_gun = pg.image.load("C:\\Users\\quint\\Desktop\\python\\image\\"+ active_img).convert_alpha()
    img_crossair = pg.image.load("C:\\Users\\quint\\Desktop\\python\\image\\crossair.png").convert_alpha()
    m_posX,m_posY = pg.mouse.get_pos()
    img_gun_posX = m_posX - (img_gun.get_width()/2)
    img_gun_posY = y-img_gun.get_width()
    text = font.render(str(pointcounter) , True , (0,0,0))
    #end image handling

    if(m_posY < y/3):
        active_img_shoot = 'doomgun_high_shoot.png'
        active_img_silent = 'doomgun_high.png'
        active_img = active_img_silent
    else:
        active_img_shoot = 'doomgun_low_shoot.png'
        active_img_silent = 'doomgun_low.png'
        active_img = active_img_silent
        if(m_posX < x/3):
            active_img_shoot = 'doomgun_low_left_shoot.png'
            active_img_silent = 'doomgun_low_left.png'
            active_img = active_img_silent
        if(m_posX > (x/3)*2):
            active_img_shoot = 'doomgun_low_right_shoot.png'
            active_img_silent = 'doomgun_low_right.png'
            active_img = active_img_silent

    clock.tick(120)
    window.fill(white)
    pressed = pg.mouse.get_pressed()[0]
    if pressed:
        active_img = active_img_shoot

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    draw_balls(balls)
    window.blit(img_gun, (m_posX - (img_gun.get_width()/2), img_gun_posY))
    window.blit(img_crossair, (m_posX - (img_crossair.get_width()/2), m_posY - (img_crossair.get_height()/2)))
    window.blit(text , ((100) - 25,25))
    space.step(1/50)
    pg.display.flip()
pg.quit()