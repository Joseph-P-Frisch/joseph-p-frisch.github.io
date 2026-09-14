#https://www.pygame.org/docs/
#https://pygame-zero.readthedocs.io/en/stable/
import os
# Force Pygame engine to limit framing overhead before loading modules
os.environ['SDL_HINT_RENDER_VSYNC'] = '1'
import pgzrun
from random import randint
FPS = 60
# Set the window size
WIDTH = 400
HEIGHT = 400

#global variables
score = 0
current_time = 20
game_over = False

#actor object initialization
kirby = Actor("kirby")
kirby.pos = WIDTH/2, HEIGHT/2
coin = Actor("coin")
coin.pos = 100, 100

def time_up():
    global game_over
    game_over = True

def draw():
    screen.fill("green")
    kirby.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score) + " press 'y' to reset", color="black", topleft=(10, 10))
    screen.draw.text("Time: " + str(current_time) + "s", color="black", topleft=(10, 30))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score) + "\ncontinue? y-yes    esc-quit", topleft=(10, 10), fontsize=35)
        return

def update_time():
    global current_time
    if not game_over:
        current_time -= 1

def place_coin():
    coin.pos = (randint(20, (WIDTH-20)), randint(20, (HEIGHT-20)))

def update(dt):
    global score
    global game_over
    global current_time

    if keyboard.left and kirby.left > 0:
        kirby.x -= (dt*60 + score/50)
    if keyboard.right and kirby.right < WIDTH:
        kirby.x += (dt*60 + score/50)
    if keyboard.up and kirby.top > 0:
        kirby.y -= (dt*60 + score/50)
    if keyboard.down and kirby.bottom < HEIGHT:
        kirby.y += (dt*60 + score/50)

    coin_collected = kirby.colliderect(coin)

    if coin_collected and game_over is not True:
        score += 10
        place_coin()
        sounds.coin_1.play()

    if keyboard.y:
        game_over = False
        score = 0
        current_time = 20
        kirby.pos = WIDTH/2, HEIGHT/2
        place_coin()
        clock.unschedule(update_time)
        clock.unschedule(time_up, 20.0)
        clock.schedule_interval(update_time, 1)
        clock.schedule(time_up, 20.0)
        return
    if keyboard.escape:
        quit()

    if game_over:
        if keyboard.escape:
            quit()
        return

clock.schedule_interval(update_time, 1)
clock.schedule(time_up, 20.0)
place_coin()
pgzrun.go()
