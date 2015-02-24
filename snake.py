#SnakeGame

#Lowe Antony Balean
#Maricar Aringo
#Kristine Marie Razo

#BSIT3C

import pygame, sys
import random

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Snake')
screen=pygame.display.set_mode((600, 600))
bait = pygame.Surface((10, 10))
bait.fill((255, 0, 0))
snake = pygame.Surface((15, 15))
snake.fill((0, 255, 0))

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:return True
	else:return False
	
def die(screen, score):
	f=pygame.font.SysFont('Arial', 30)
	t=f.render('Game Over. Your score was '+str(score) , True, (255, 255, 255))
	screen.blit(t, (140, 280))
	pygame.display.update()
	pygame.time.wait(2000)
	sys.exit(0)
	
ab = [290, 290, 290, 290, 290]
cd = [290, 270, 250, 230, 210]
dirs = 0;score = 0
abc = (random.randint(0, 590), random.randint(0, 590))
f = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()

while True:
	clock.tick(10)
	for e in pygame.event.get():
		if e.type == QUIT:
			sys.exit(0)
		elif e.type == KEYDOWN:
			if e.key == K_UP and dirs != 0:dirs = 2
			elif e.key == K_DOWN and dirs != 2:dirs = 0
			elif e.key == K_LEFT and dirs != 1:dirs = 3
			elif e.key == K_RIGHT and dirs != 3:dirs = 1
	i = len(ab)-1
	while i >= 2:
		if collide(ab[0], ab[i], cd[0], cd[i], 20, 20, 20, 20):die(screen, score)
		i-= 1
	if collide(ab[0], abc[0], cd[0], abc[1], 20, 10, 20, 10):score+=1;ab.append(700);cd.append(700);abc=(random.randint(0,590),random.randint(0,590))
	if ab[0] < 0 or ab[0] > 580 or cd[0] < 0 or cd[0] > 580: die(screen, score)
	i = len(ab)-1
	while i >= 1:
		ab[i] = ab[i-1]
		cd[i] = cd[i-1]
		i -= 1
	if dirs==0:cd[0] += 20
	elif dirs==1:ab[0] += 20
	elif dirs==2:cd[0] -= 20
	elif dirs==3:ab[0] -= 20	
	screen.fill((0, 0, 0))	
	for i in range(0, len(ab)):
		screen.blit(snake, (ab[i], cd[i]))
	screen.blit(bait, abc)
	t= f.render('Score:'+str(score), True, (255, 255, 255))
	screen.blit(t, (10, 10))
	pygame.display.update()
