import pygame, random

MOVECOUNT=0

W=(255,255,255)
B=(0,0,255)
E=(255,128,0)
G=(0,200,0)
R=(255,0,0)
Y=(255,255,0)

BACKCOLOR=(0,0,0)

WINDOWWIDTH=1200
WINDOWHEIGHT=1000

CUBEWIDTH=290
CUBEHEIGHT=290

SFRONT=0
STOP=1
SRIGHT=2
SUNDER=3
SLEFT=4
SBACK=5

RTOP=0
RMID=1
RBOT=2

CLEFT=0
CMID=1
CRIGHT=2

XOFFSET=(WINDOWWIDTH-CUBEWIDTH)/2+CUBEWIDTH
YOFFSET=(WINDOWHEIGHT-CUBEHEIGHT)/2

DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

#        F
CUBE=[[[B,B,B],
       [B,B,B],
       [B,B,B]],
#        T
      [[W,W,W],
       [W,W,W],
       [W,W,W]],
#        R
      [[E,E,E],
       [E,E,E],
       [E,E,E]],
#        U
      [[Y,Y,Y],
       [Y,Y,Y],
       [Y,Y,Y]],
#        L
      [[R,R,R],
       [R,R,R],
       [R,R,R]],
#        B
      [[G,G,G],
       [G,G,G],
       [G,G,G]]]


def WIN():
    myfont = pygame.font.SysFont("monospace", 100)

    label = myfont.render("You Win!!!", 1, (255,255,255))
    DISPLAYSURF.blit(label, (100, 100))

def DISPLAYTEXT(MESSAGE,X,Y,COLOR):
    fontobject=pygame.font.SysFont('monospace', 75)
    if len(MESSAGE) != 0:
        DISPLAYSURF.blit(fontobject.render(MESSAGE, 0, COLOR),(X,Y))
