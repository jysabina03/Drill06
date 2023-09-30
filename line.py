import random
from pico2d import *


TUK_WIDTH,TUK_HEICHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEICHT)
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')
hand_arrow = load_image('hand_arrow.png')

def make_hand(x,y):
    global speed,hand,handnum
    new_handX = x
    new_handY = y
    hand.append((new_handX,new_handY))
    handnum+=1

def make_load(p1,p2):
    x1,y1=p1[0],p1[1]
    x2,y2=p2[0],p2[1]

    global speed
    t=speed/100

    global nowX, nowY
    x = (1-t) * x1 + t*x2
    y = (1-t) * y1 + t*y2

    nowX, nowY =x,y


def handle_events():
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x,y = event.x, TUK_HEIGHT - 1 - event.y
            make_hand(x,y)


def delete_hand():
    pass


running = True
charX,charY = TUK_WIDTH // 2,TUK_HEICHT//2
handX,handY = charX,charY
nowX,nowY=charX,charY
dir_see = 1
frame = 0
speed = 0
handnum=0
hand=[(charX,charY)]


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEICHT//2)

    if int(handX) == int(nowX) and int(handY) == int(nowY):
        delete_hand()
    make_load((nowX,nowY),(handX,handY))
    speed+=5

    hand_arrow.clip_draw(0, 0, 50, 52, handX, handY)

    #
    # if  hand[0][0]< handX:
    #     dir_see = 1
    # else:
    #     dir_see = -1
    #
    if dir_see == 1:
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0,'h',nowX, nowY,100,100)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, nowX, nowY)

    frame = (frame + 1) % 8
    update_canvas()
    delay(0.1)


close_canvas()
