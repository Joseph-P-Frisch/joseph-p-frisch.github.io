from SimpleGraphics import *
import random
from random import randint
M = 55
MakeWindow(M, False, bgcolor=[.04,.02,.4])

for i in range(M):
    if i % 5 == 0:
        DrawStar(random.uniform(-M+2, M-2), random.uniform((-M+2), (M-2)), r = random.uniform(1,2), theta = randint(45, 99), FillColor=[random.uniform(.9, 1), random.uniform(.9, 1), random.uniform(.7, .8)])
    else:
        DrawStar(random.uniform(-M+2, M-2), random.uniform((-M+2), (M-2)), r = random.uniform(1,2), theta = 0, FillColor=[random.uniform(.6, .8), random.uniform(.6, .8), random.uniform(.5, .6)])

DrawDisk(M-M/4,M-M/4, M/2, FillColor=[.65, .65, .65], EdgeColor=None, EdgeWidth=0)

ShowWindow(duration=10)
CloseWindow()