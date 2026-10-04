from SimpleGraphics import *
M = 10
MakeWindow(M, False, BLUE)
s=10
f=BLACK
Title("Part 1", f, 18)
DrawText(-8.5, 2, "Disk", f, s)
DrawDisk(-8, 0, 1.5, FillColor=BLACK)
DrawText(-4.5, 2, "Star", f, s)
DrawStar(-4, 0, 1.4, FillColor=YELLOW, EdgeColor=BLUE, EdgeWidth=2)
DrawText(-1, 2, "Rect", f, s)
DrawRect(-0.5, 0, 2, 2, theta=45, EdgeWidth=3, EdgeColor=WHITE)
DrawText(3, 2, "Line Seg", f, s)
DrawLineSeg(3, 0, 5, 0, LineColor=RED, LineWidth=1)
DrawText(7, 2, "Polygon", f, s)
DrawPoly([7, 9, 9, 7], [-1, -1, 1, 1], FillColor=None, EdgeWidth=3, EdgeColor=GREEN)
ShowWindow(duration=M)
CloseWindow()