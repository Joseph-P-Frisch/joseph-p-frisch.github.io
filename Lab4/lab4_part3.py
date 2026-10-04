from SimpleGraphics import *
import random

M = 60 # half window width and height (wS = h)
S = 5*M/6 # set length of each triangle (2*S = total length)

MakeWindow(M, False, bgcolor=[0,0,0])

def draw_equilateral_triangle(a,b,s): # symbol representing the balance and unity between wisdom, power, and courage.
    # a,b is first point, s is length of sides. This point represents the bottom left of the bottom left triangle.
    DrawPoly([a,a+s,a+(s/2)],[b,b,b+s*(3**(1/2)/2)],YELLOW,1,None)

def draw_rupees(h): # Who doesn't like collecting Rupee's
    w = h / 2 # h,w are the major and minor axis lengths where h=2w
    c = []
    for i in range(21):
        a = random.uniform(-M+5,M) # a,b is origin point of rupee
        b = random.uniform(-M+7.5,M-20)
        if i % 3 == 0:
            c = [0,0,1]
        if i % 3 == 1:
            c = [1,0,0]
        if i % 3 == 2:
            c = [0,1,0]
        DrawPoly([a,a-w,a-2*w,a-2*w,a-w,a],[b,b+(h/2),b,b-h,b-(3*h/2),b-h],FillColor=c,EdgeWidth=0,EdgeColor=None)

def draw_triforce(a,b,s):
    draw_equilateral_triangle(a,b,s) # (a,b) is bottom left
    draw_equilateral_triangle(a+s,b,s) # (a+s,b) is bottom right
    draw_equilateral_triangle(a+(s/2),b+s*(3**(1/2))/2,s) # (a+(s/2), b + s*sqrt(3)/2) is top
    Title("Legend of Zelda - Triforce", BLACK, 18)
    DrawText(-42, 52, "I am a fan of the Legend of Zelda.", WHITE, 18)


draw_triforce(-50,-50*(3**(1/2))/2,S)
draw_rupees(M/12)
ShowWindow(duration=10)
CloseWindow()