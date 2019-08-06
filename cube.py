import pygame, sys, math, random, time, datetime
from pygame.locals import*
from solve import*
from cubeconstants import*
from moves import*
from positions import*

pygame.init()
DISPLAYSURF.fill(BACKCOLOR)
pygame.display.set_caption('Cube')

def MESSUP(MESSUPMOVES):
    MOVES=[RCLOCK,RCOUNTERCLOCK,LCOUNTERCLOCK,LCLOCK,MIDCLOCK,MIDCOUNTERCLOCK,TCOUNTERCLOCK,TCLOCK,UCLOCK,UCOUNTERCLOCK,MIDRIGHT,MIDLEFT,BCOUNTERCLOCK,BCLOCK,FCOUNTERCLOCK,FCLOCK]
    for number in range(MESSUPMOVES):
        MOVE=random.choice(MOVES)
        MOVE()
        DRAWCUBE()
        pygame.display.update()
        pygame.time.delay(100)


MESSUPMOVES=30

TIMER=0

SOLVE=0

COUNTER=0

DISPLAYTEXT ('Moves: '+str(MOVECOUNT),100,900,W)
DISPLAYTEXT ('Time: ' +"%0*d"%(2,TIMER//60)+':'+"%0*d"%(2,TIMER%60),100,800,W)
DISPLAYTEXT('Manual',700,0,W)
DRAWCUBE()
pygame.display.update()
pygame.time.delay(1000)
MESSUP(MESSUPMOVES)
DRAWCUBE()
pygame.display.update()

STARTTIME=pygame.time.get_ticks()//1000

pygame.time.set_timer(USEREVENT+1,1)

MOVES=[]

STAGE='TOPLAYER'

while True:
    for event in pygame.event.get():
        if event.type==USEREVENT+1:
            DISPLAYTEXT ('Time: ' +"%0*d"%(2,TIMER//60)+':'+"%0*d"%(2,TIMER%60),100,800,BACKCOLOR)
            TIMER=pygame.time.get_ticks()//1000-STARTTIME
            DISPLAYTEXT ('Time: ' +"%0*d"%(2,TIMER//60)+':'+"%0*d"%(2,TIMER%60),100,800,W)
            pygame.display.update()
            DISPLAYTEXT (str(COUNTER),800,100,BACKCOLOR)
            COUNTER=1
            if SOLVE==1:
                if len(MOVES)>0:
                    NEXT=MOVES[0]
                    NEXT()
                    MOVECOUNT+=1
                    del(MOVES[0])
                    DISPLAYTEXT ('Moves: '+str(MOVECOUNT-1),100,900,BACKCOLOR)
                    DISPLAYTEXT ('Moves: '+str(MOVECOUNT),100,900,W)
                    DRAWCUBE()
                    pygame.display.update()
                else:
                    MOVES=NEXTMOVE(STAGE)
                    if (MOVES=='NEXTSTAGE')&(STAGE=='TOPLAYER'):
                        STAGE='MID'
                        MOVES=[]
                    if (MOVES=='NEXTSTAGE')&(STAGE=='MID'):
                        STAGE='MIDLAYER1'
                        MOVES=[]
                    if (MOVES=='NEXTSTAGE')&(STAGE=='MIDLAYER1'):
                        STAGE='MIDLAYER2'
                        MOVES=[]
                    if (MOVES=='NEXTSTAGE')&(STAGE=='MIDLAYER2'):
                        STAGE='BOTTOMCROSS'
                        MOVES=[]
                    if (MOVES=='NEXTSTAGE')&(STAGE=='BOTTOMCROSS'):
                        STAGE='BOTTOMCORNERS1'
                        MOVES=[]
                    if (MOVES=='NEXTSTAGE')&(STAGE=='BOTTOMCORNERS1'):
                        STAGE='BOTTOMCORNERS2'
                        MOVES=[]
                    if (MOVES=='NEXTSTAGE')&(STAGE=='BOTTOMCORNERS2'):
                        STAGE='LASTSTAGE'
                        MOVES=[]
                    if MOVES=='STOP':
                        SOLVE=0
                        DISPLAYTEXT('Automatic',700,0,BACKCOLOR)
                        DISPLAYTEXT('Manual',700,0,W)
                        MOVES=[]
                    DRAWCUBE()
                    pygame.display.update()

        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if SOLVE==0:
                if event.key==K_e:
                    RCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_d:
                    RCOUNTERCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_q:
                    LCOUNTERCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_a:
                    LCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_w:
                    MIDCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_s:
                    MIDCOUNTERCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_UP:
                    CUBEUP()
                if event.key==K_DOWN:
                    CUBEDOWN()
                if event.key==K_u:
                    TCOUNTERCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_y:
                    TCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_m:
                    UCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_n:
                    UCOUNTERCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_j:
                    MIDRIGHT()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_h:
                    MIDLEFT()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_RIGHT:
                    CUBERIGHT()
                if event.key==K_LEFT:
                    CUBELEFT()
                if event.key==K_PERIOD:
                    CUBECLOCK()
                if event.key==K_COMMA:
                    CUBECOUNTERCLOCK()
                if event.key==K_o:
                    BCOUNTERCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_p:
                    BCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_l:
                    FCOUNTERCLOCK()
                    MOVECOUNT=MOVECOUNT+1
                if event.key==K_SEMICOLON:
                    FCLOCK()
                    MOVECOUNT=MOVECOUNT+1
            if event.key==K_RETURN:
                if SOLVE==0:
                    SOLVE=1
                    STAGE='TOPLAYER'
                    DISPLAYTEXT('Manual',700,0,BACKCOLOR)
                    DISPLAYTEXT('Automatic',700,0,W)
                else:
                    SOLVE=0
                    DISPLAYTEXT('Automatic',700,0,BACKCOLOR)
                    DISPLAYTEXT('Manual',700,0,W)
            DISPLAYTEXT ('Moves: '+str(MOVECOUNT-1),100,900,BACKCOLOR)
            DISPLAYTEXT ('Moves: '+str(MOVECOUNT),100,900,W)

            DRAWCUBE()
            pygame.display.update()
        SIDE=0
        if CUBE[SIDE][RMID][CMID]==CUBE[SIDE][RTOP][CMID]==CUBE[SIDE][RBOT][CMID]==CUBE[SIDE][RMID][CLEFT]==CUBE[SIDE][RTOP][CLEFT]==CUBE[SIDE][RBOT][CLEFT]==CUBE[SIDE][RMID][CRIGHT]==CUBE[SIDE][RTOP][CRIGHT]==CUBE[SIDE][RBOT][CRIGHT]:
            SIDE=1
        if CUBE[SIDE][RMID][CMID]==CUBE[SIDE][RTOP][CMID]==CUBE[SIDE][RBOT][CMID]==CUBE[SIDE][RMID][CLEFT]==CUBE[SIDE][RTOP][CLEFT]==CUBE[SIDE][RBOT][CLEFT]==CUBE[SIDE][RMID][CRIGHT]==CUBE[SIDE][RTOP][CRIGHT]==CUBE[SIDE][RBOT][CRIGHT]:
            SIDE=2
        if CUBE[SIDE][RMID][CMID]==CUBE[SIDE][RTOP][CMID]==CUBE[SIDE][RBOT][CMID]==CUBE[SIDE][RMID][CLEFT]==CUBE[SIDE][RTOP][CLEFT]==CUBE[SIDE][RBOT][CLEFT]==CUBE[SIDE][RMID][CRIGHT]==CUBE[SIDE][RTOP][CRIGHT]==CUBE[SIDE][RBOT][CRIGHT]:
            SIDE=3
        if CUBE[SIDE][RMID][CMID]==CUBE[SIDE][RTOP][CMID]==CUBE[SIDE][RBOT][CMID]==CUBE[SIDE][RMID][CLEFT]==CUBE[SIDE][RTOP][CLEFT]==CUBE[SIDE][RBOT][CLEFT]==CUBE[SIDE][RMID][CRIGHT]==CUBE[SIDE][RTOP][CRIGHT]==CUBE[SIDE][RBOT][CRIGHT]:
            SIDE=4
        if CUBE[SIDE][RMID][CMID]==CUBE[SIDE][RTOP][CMID]==CUBE[SIDE][RBOT][CMID]==CUBE[SIDE][RMID][CLEFT]==CUBE[SIDE][RTOP][CLEFT]==CUBE[SIDE][RBOT][CLEFT]==CUBE[SIDE][RMID][CRIGHT]==CUBE[SIDE][RTOP][CRIGHT]==CUBE[SIDE][RBOT][CRIGHT]:

            DRAWCUBE()
            pygame.display.update()

            WIN()
            pygame.display.update()

            pygame.time.delay(5000)

            pygame.quit()
            sys.exit()
