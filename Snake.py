import pygame # importing pygame
import time # importing time
import random

pygame.init()

#Colors are here, color_name = (R,G,B)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
#The variables to be used for game
screen_height = 600
screen_width = 800

block_size = 10
FPS = 15

font = pygame.font.SysFont(None, 25)

#Makes a new snake
def snake(snake_list):
	''' This code checks for the (x,y) coordinates in snakeList and makes new snake 
	at that point. The XnY keeps getting updated, thus it will move along with head.'''
	for XnY in snake_list:
		pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def message_to_screen(msg, color):
	screen_text = font.render(msg,True ,color)
	gameDisplay.blit(screen_text, [screen_width/2, screen_height/2])

#Used for frames per seconds
clock = pygame.time.Clock() 

#Modifications For Screen
gameDisplay = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Trial')


def gameLoop():
	#A boolean for running the window till the condition is false
	gameExit = False
	gameOver = False

	lead_x = screen_width/2
	lead_y = screen_height/2

	lead_x_change = 0
	lead_y_change = 0

	snakeList = []
	snakeLength = 1

	randAppleX = random.randrange(0, screen_width-block_size,10)
	randAppleY = random.randrange(0, screen_height-block_size,10)
	#Event Handling
	while not gameExit:

		while gameOver == True:
			message_to_screen("Game Over!! \n Press C to Play Again or Q to Quit", red)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameExit = True
						gameOver = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:	
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
					lead_x_change = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
					lead_y_change =0


		lead_x += lead_x_change			
		lead_y += lead_y_change

		#Logical Code
		if lead_x > (screen_width - block_size) or lead_x < 0:
			gameOver = True

		if lead_y > (screen_height - block_size) or lead_y < 0:
			gameOver = True		
		
	#Graphics and Rendering code
		gameDisplay.fill(white)
		pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY,block_size,block_size])	
		
		snakeHead = []
		snakeHead.append(lead_x)#It copies the current x - coordinate
		snakeHead.append(lead_y)#Same as above but y - coordinate
		snakeList.append(snakeHead)#It appends the list each time in the loop

		#This code make sures that the list wouldn't append infinitely
		#if len(snakeList) > snakeLength:
		#	del snakeList [0]

		#for eachSegment in snakeList[:-1]:
		#	if eachSegment == snakeHead:
		#		gameOver = True

		snake(snakeList)
		pygame.display.update()		

		if lead_x == randAppleX and lead_y == randAppleY:
			randAppleX = random.randrange(0, screen_width-block_size,10)
			randAppleY = random.randrange(0, screen_height-block_size,10)
			snakeLength += 1

		clock.tick(15)

	pygame.quit()
	quit()

gameLoop()
