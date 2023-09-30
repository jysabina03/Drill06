import random
from pico2d import *


TUK_WIDTH,TUK_HEICHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEICHT)
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')

def make_hand():
    global handX,handY,speed
    handX = random.randint(0,TUK_WIDTH)
    handY = random.randint(0,TUK_HEICHT)
    speed=0
    global nowX, dir_see

    if nowX < handX:
        dir_see = 1
    else:
        dir_see = -1

def make_load(p1,p2):
    x1,y1=p1[0],p1[1]
    x2,y2=p2[0],p2[1]

    global speed
    t=speed/100

    global nowX, nowY
    x = (1-t) * x1 + t*x2
    y = (1-t) * y1 + t*y2

    nowX, nowY =x,y


running = True
charX,charY = TUK_WIDTH // 2,TUK_HEICHT//2
handX,handY = charX,charY
nowX,nowY=charX,charY
dir_see = 1
frame = 0
speed = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEICHT//2)

    if int(handX) == int(nowX) and int(handY) == int(nowY):
        make_hand()
    make_load((nowX,nowY),(handX,handY))
    speed+=5

    hand.clip_draw(0, 0, 50, 52, handX, handY)

    if dir_see == 1:
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0,'h',nowX, nowY,100,100)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, nowX, nowY)

    frame = (frame + 1) % 8
    update_canvas()
    delay(0.1)


close_canvas()
