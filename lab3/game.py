import os # python built-in module for manipulating OS dependent functionality
#https://pygame-zero.readthedocs.io/_/downloads/en/latest/pdf/
os.environ["SDL_VIDEO_WINDOW_POS"] = "center" # opens window in the middle of the screen
from random import randint

# game window dimensions
WIDTH = 800
HEIGHT = 600

# actor initializations
mario = Actor("mario")
mario.pos = 400, 300

bird = Actor("bird-up")
bird2 = Actor("bird-down")
bird.pos = randint(800,1600), randint(10,200)
bird2.pos = randint(800,1600), randint(10,200)

house = Actor("house")
house.pos = randint(800,1600), 460

pipe = Actor("pipe")
pipe.pos = randint(800,1600), 450

coin = Actor("coin")
coin.pos = randint(800,1600), randint(10,200)

# flag variables
bird_up = True
up = False
game_over = False
# global variables
score = 0
number_of_updates = 0
# list
scores = []


def draw():
    screen.blit("background", (0, 0))
    if not game_over:
        mario.draw()
        bird.draw()
        bird2.draw()
        house.draw()
        pipe.draw()
        coin.draw()
        screen.draw.text("Score: " + str(score), color="black", top=5, right=795)
    else:
        display_high_scores()

    # instructions for reset and quit
    screen.draw.text("press 'R' to reset", color="black", fontsize=25, right=795, top=20)
    screen.draw.text("press 'esc' to quit", color="black", fontsize=25, right=795, top=45)

# event hooks
def on_mouse_down():
    global up
    up = True # turn off gravity
    mario.y -= 25 # move mario up

def on_mouse_up():
    global up
    up = False # make sure gravity gets turned back on

# reset the game
def reset_game():
    global game_over, score, mario, bird, bird2, house, pipe, coin, scores
    score = 0
    scores = []
    mario.pos = 400, 300
    bird.pos = randint(800, 1600), randint(10, 200)
    bird2.pos = randint(800, 1600), randint(10, 200)
    house.pos = randint(800, 1600), 460
    pipe.pos = randint(800, 1600), 450
    coin.pos = randint(800,1600), randint(10,200)
    game_over = False
    return

def quit_game():
    quit()

def update_high_scores():
    global score, scores
    filename = "./high-scores.txt" # set "filename" = to "[current dir path]\high-scores.txt"

    with open(filename, "r") as file: # read high scores file
        line = file.readline() # set "line" = to each file value
    high_scores = line.split() # "add each value "line" to a list "high_scores"
    high_scores.append(str(score)) # add current score to list

    for i in range(len(high_scores)): # SORT THE LIST!! from i = 0 to i = list length
        for j in range(len(high_scores)-1): # for every i in the outside loop, reorder the list from j = 0 to list length - 1
            if int(high_scores[i]) > int(high_scores[j]): # swap list index i for j if value i is larger than value j
                high_scores[j], high_scores[i] = high_scores[i], high_scores[j]

    for i in high_scores:
        scores.append(i + " ") # put ordered list into empty list for file write

    with open(filename, "w") as file: #open file specified earlier
        for high_score in scores: # for each value of scores write the score into the file
            file.write(high_score)

def display_high_scores():
    global scores
    screen.draw.text("HIGH SCORES", (350, 150), color="black")
    y = 175
    position = 1 # tracks position of each score
    for high_score in scores:
        if position <= 5: # only draw 5 scores
            screen.draw.text(str(position) + ". " + str(high_score), (350, y), color="black") # draw each score
            y += 25 # draw next score below last
            position += 1 # track score position

def flap():
    global bird_up # global flag variable that represents bird image state and update bird.image when called
    if bird_up:
        bird.image = "bird-down"
        bird2.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird2.image = "bird-up"
        bird_up = True


music.play("mariomusic") # loop music file

def update():
    global game_over, score, number_of_updates

    if keyboard.escape:
        quit_game()

    if keyboard.r and keyboard.lshift or keyboard.rshift:
        reset_game()

    if not game_over: # gravity
        if not up:
            mario.y += 1

        if bird.x > 0:
            bird.x -= 4 # move birds left if condition is met
            if number_of_updates == 9: # call flap
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1 # update counter
        else: # draw new bird (passed x = 0) and update score, reset flap state
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1
            number_of_updates = 0

        if bird2.x > 0:
            bird2.x -= 4
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird2.x = randint(800, 1600)
            bird2.y = randint(10, 200)
            score += 1
            number_of_updates = 0

        if house.right > 0: # check house in field/curtain
            house.x -= 2 # move house
        else: # redraw house in curtain and update score
            house.x = randint(800, 1600)
            score += 1

        if pipe.right > 0: # check if pipe is in field/curtain
            pipe.x -= 2 # move pipe
        else: # redraw pipe in curtain and update score
            pipe.x = randint(800, 1600)
            score += 1

        if coin.right > 0: # check if coin is in field/curtain
            coin.x -= 3 # move coin
        else: # redraw coin
            coin.pos = randint(800, 1600), randint(10, 200)

        if mario.top < 0 or mario.bottom > 560: # check if mario is within safe zone. call game over and update scores if he is not
            game_over = True
            update_high_scores()

        if (mario.collidepoint(bird.x, bird.y) or # check if mario has collided with objects, call game over and update scores if so
                mario.collidepoint(house.x, house.y) or
                mario.collidepoint(pipe.x, pipe.y)):
            game_over = True
            update_high_scores()

        if mario.colliderect(coin): # play sound, update score, and redraw coin if mario collects it
            score += 5
            sounds.coin_1.play()
            coin.pos = randint(800,1600), randint(10,200)
