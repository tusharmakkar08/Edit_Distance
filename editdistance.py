import pygame, sys, game, text
from pygame.locals import *

edit_sx1 = 20
edit_sy1 = 25
edit_sx2 = 20
edit_sy2 = 50

results = game.begin()
matrix = results[0]
no_of_columns = len(results[1])
no_of_rows = len(results[2])
s1 = results[1]
s2 = results[2]
paths = results[3]
print matrix
for i in range(no_of_rows+1):
		for j in range(no_of_columns+1):
			print str(matrix[i,j])+' ',
		print '\n'

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 100)
BLUE = (0, 0, 255)
ScrSize = (1350,740)
Origin  = (0,0)
Gray    = (200,200,200)
Red     = (250,20,20)
Blue    = (20,20,100)
Buff    = (200,180,180)


pygame.init()
# set up the window
pygame.init()
windowSurface=pygame.display.set_mode(ScrSize)
pygame.display.set_caption('Levenstein Distance')
screenRect  = windowSurface.get_rect()
world = pygame.Surface((ScrSize[0]*2, ScrSize[1]*2))  
pygame.draw.line(windowSurface,BLUE,(20,100),(700,100),2)  
# set up fonts
basicFont = pygame.font.SysFont(None, 30)
windowSurface.fill(WHITE)
pygame.draw.polygon(windowSurface, WHITE, ((0,0),(1350,0),(1350,60),(0,60) ))
#print source string
str_x = 100
str_y = 90
for i in s1:
	text = basicFont.render(i, True, Red)
	textRect = text.get_rect()
	textRect.centerx = str_x
	textRect.centery = str_y - 10
	windowSurface.blit(text, textRect)
	str_x = str_x + 40
#print destination string
str_x = 30
str_y = 160
for i in s2:
	text = basicFont.render(i, True, Red)
	textRect = text.get_rect()
	textRect.centerx = str_x - 10
	textRect.centery = str_y
	windowSurface.blit(text, textRect)
	str_y = str_y + 40
#print matrix
pos_x = 60
pos_y = 120
for i in range(no_of_rows+1):
		for j in range(no_of_columns+1):
			print matrix[i,j]
			string = str(matrix[i,j])
			text = basicFont.render(string, True, BLACK)
			textRect = text.get_rect()
			textRect.centerx = pos_x
			textRect.centery = pos_y
			pygame.draw.circle(windowSurface,GREEN,(pos_x,pos_y),15)
			pygame.draw.circle(windowSurface,WHITE,(pos_x,pos_y),17,2)
			windowSurface.blit(text, textRect)
			pos_x = pos_x + 40
		print '\n'
		pos_x  = 60
		pos_y = pos_y + 40

pygame.display.update()
######        
ratio       = (1.0 * screenRect.width) / world.get_width()
scrollThick = 20
track = pygame.Rect(screenRect.left,screenRect.bottom - scrollThick,screenRect.width,scrollThick)   
knob        = pygame.Rect(track)  
knob.width   = track.width * ratio
scrolling   = False
######
pos_x = 0
pos_y = 0
num = matrix[0,0]
string = str(num)
text = basicFont.render(string, True, BLACK) #changed from red to black
textRect = text.get_rect()
textRect.centerx = 60
textRect.centery = 120
pygame.draw.circle(windowSurface,(255,200,0),(60,120),15)
windowSurface.blit(text, textRect)
flag = 0
for path in paths:
	for i in range(len(path)-1):
		pygame.time.delay(100)
		x0 = path[i][1]*40 + 60
		y0 = path[i][0]*40 + 120
		x1 = path[i+1][1]*40 + 60
		y1 = path[i+1][0]*40 + 120
		if path[i+1][0] == path[i][0] + 1 and path[i+1][1] == path[i][1] + 1:
			text = basicFont.render(s1[path[i][1]], True, BLACK) #changed from red to black
			textRect = text.get_rect()
			textRect.centerx = edit_sx1
			textRect.centery = edit_sy1
			windowSurface.blit(text, textRect)
			text = basicFont.render(s2[path[i][0]], True, BLACK) #changed from red to black
			textRect = text.get_rect()
			textRect.centerx = edit_sx2
			textRect.centery = edit_sy2
			windowSurface.blit(text, textRect)
			edit_sx1+=15
			edit_sx2+=15
		elif path[i+1][0] == path[i][0] + 1:
			text = basicFont.render('-', True, BLACK) #changed from red to black
			textRect = text.get_rect()
			textRect.centerx = edit_sx1
			textRect.centery = edit_sy1
			windowSurface.blit(text, textRect)
			text = basicFont.render(s2[path[i][0]], True, BLACK) #changed from red to black
			textRect = text.get_rect()
			textRect.centerx = edit_sx2
			textRect.centery = edit_sy2
			windowSurface.blit(text, textRect)
			edit_sx1+=15
			edit_sx2+=15
		else:
			text = basicFont.render(s1[path[i][1]], True, BLACK) #changed from red to black
			textRect = text.get_rect()
			textRect.centerx = edit_sx1
			textRect.centery = edit_sy1
			windowSurface.blit(text, textRect)
			text = basicFont.render('-', True, BLACK) #changed from red to black
			textRect = text.get_rect()
			textRect.centerx = edit_sx2
			textRect.centery = edit_sy2
			windowSurface.blit(text, textRect)
			edit_sx1+=15
			edit_sx2+=15
		pygame.time.delay(100)
		pygame.display.update()
		num = matrix[path[i+1][0],path[i+1][1]]
		string = str(num)
		text = basicFont.render(string, True, BLACK) #changed from red to black
		textRect = text.get_rect()
		textRect.centerx = x1
		textRect.centery = y1
		pygame.draw.circle(windowSurface,(255,200,0),(x1,y1),15)  #highlight circle color
		windowSurface.blit(text, textRect)
		pygame.display.update()
		if 	path == paths[len(paths)-1]:
			flag = 1
	if flag:
		break
	pygame.display.update()
	t=0
	while t!=1:
		t+=1
		event = pygame.event.wait()
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif ( event.type == MOUSEMOTION and scrolling):
			if event.rel[0] != 0:
				move = max(event.rel[0], track.left - knob.left)
				move = min(move, track.right - knob.right)
				if move != 0:
					knob.move_ip((move, 0))
							
		elif event.type == MOUSEBUTTONDOWN and knob.collidepoint(event.pos):
			scrolling = True
                   
		elif event.type == MOUSEBUTTONUP:
			scrolling = False
               
		pygame.draw.rect(windowSurface, Buff, track, 0 )
		pygame.draw.rect(windowSurface, Blue, knob.inflate(0,-5), 2)
		pygame.display.flip()
	while not pygame.event.get():
		pygame.time.delay(1)
	 
	for i in range(len(path)-1):
		x0 = path[i][1]*40 + 60
		y0 = path[i][0]*40 + 120
		x1 = path[i+1][1]*40 + 60
		y1 = path[i+1][0]*40 + 120
		num = matrix[path[i+1][0],path[i+1][1]]
		string = str(num)
		text = basicFont.render(string, True, BLACK)
		textRect = text.get_rect()
		textRect.centerx = x1
		textRect.centery = y1
		pygame.draw.circle(windowSurface,GREEN,(x1,y1),15)
		windowSurface.blit(text, textRect)	
		pygame.draw.circle(windowSurface,WHITE,(x1,y1),17,2)
		pygame.display.update()
	edit_sx1=20
	edit_sx2=20
	pygame.draw.polygon(windowSurface, WHITE , ((0,0),(0,60),(1350,60),(1350,0) ))
i = 0
# run the game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()

