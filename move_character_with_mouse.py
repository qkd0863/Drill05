from pico2d import *
import  random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')



points=[(random.randint(300,900),random.randint(300,900))for i in range(2)]

def move_to_line():
    global mx, my, frame
    for i in range(0,100+1,10):
        frame = (frame + 1) % 8
        t = i/100
        mx = (1-t) * mx + t * hx
        my = (1-t) * my + t * hy
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(hx, hy)
        if (mx >= hx):
            character.clip_draw(frame * 100, 100 * 0, 100, 100, mx, my)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, mx, my)
        update_canvas()
        delay(0.1)



def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
mx, my = TUK_WIDTH // 2, TUK_HEIGHT // 2
hx = random.randint(300,900)
hy = random.randint(300,900)
frame = 0
hide_cursor()

while running:
    move_to_line()
    hx = random.randint(300, 900)
    hy = random.randint(300, 900)
    handle_events()

close_canvas()



