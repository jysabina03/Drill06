import random
from pico2d import *


TUK_WIDTH,TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')
hand_arrow = load_image('hand_arrow.png')

def make_hand(x,y):
    global speed,hand
    new_handX = x
    new_handY = y

    if len(hand) == 0:
        global handX, handY
        handX, handY = new_handX,new_handY
        speed = 0

    hand.append((new_handX,new_handY))


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
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x,y = event.x, TUK_HEIGHT - 1 - event.y
            make_hand(x,y)


def delete_hand():
    global hand,speed
    if len(hand) > 0:
        del hand[0]

        if len(hand)>0:
            global handX, handY
            handX,handY=hand[0]
            speed=0





running = True
charX,charY = TUK_WIDTH // 2,TUK_HEIGHT//2
handX,handY = charX,charY
nowX,nowY=charX,charY
dir_see = 1
frame = 0
speed = 0
hand=[(charX,charY)]


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)

    if len(hand)>0:

        if abs(handX-nowX)<2 and abs(handY-nowY)<2:
            delete_hand()
        make_load((nowX,nowY),(handX,handY))
        speed+=5
        for i in range(0,len(hand)):
            hand_arrow.clip_draw(0, 0, 50, 52, hand[i][0], hand[i][1])

        if handX> nowX:
            dir_see = 1
        else:
            dir_see = -1

        if dir_see == 1:
            character.clip_composite_draw(frame * 100, 0, 100, 100, 0,'h',nowX, nowY,100,100)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, nowX, nowY)
    else:
        if dir_see == 1:
            character.clip_composite_draw(0, 200, 100, 100, 0, 'h', nowX, nowY, 100, 100)
        else:
            character.clip_draw(0, 200, 100, 100, nowX, nowY)


    frame = (frame + 1) % 8
    update_canvas()
    handle_events()
    delay(0.1)


close_canvas()
