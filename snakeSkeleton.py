##	PyPython Skeleton code
##	HKN Lab Jam Fall 2017

#Imports are like includes; gives us ability to use external functions, classes, etc
import pygame
import snakeLib

#Define the size of the screen
screenX = 500
screenY = 500

#Initialize an instance of pygame
pygame.init()

#Instantiate the screen
screen = pygame.display.set_mode((screenX,screenY))

#Create a clock - This will be how we control frame rate
clock = pygame.time.Clock()

#Some helper variables to keep track of the snake and dot
#Notice the variables are nontyped (no 'int's 'string's, etc)
snakeX = 5
snakeY = 5
prevX = snakeX
prevY = snakeY
snakeSize = 20
dotX = 100
dotY = 100
dotSize = 15

#Create a list to keep track of the size of the snake
snakeLinks = []
snakeLinks.append({'x':snakeX,'y':snakeY})

#Create a 3 element list; declares colors
RGB = [250,0,0]

#Variables to help with control of logic
done = False

###TODO: Add start screen


#Loops forever
while not done:
	#Checks event queue; just quit for now
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	#Get the keys pressed and check them
	pressed = pygame.key.get_pressed()
	
	#Save previous value of snake head
	prevX = snakeX
	prevY = snakeY
	
	#Test if done or change coordinates of snake head
	if pressed[pygame.K_SPACE]:
		done = True
	elif pressed[pygame.K_UP]:
		snakeY -= snakeSize
	elif pressed[pygame.K_DOWN]:
		snakeY += snakeSize
	elif pressed[pygame.K_LEFT]:
		snakeX -= snakeSize
	elif pressed[pygame.K_RIGHT]:
		snakeX += snakeSize
	
	###TODO: Update snake to constantly move
	###TODO: Add constraints to screen
		
	#Check if snake head near dot; add another snake link if so
	if abs(snakeX - dotX) < snakeSize and abs(snakeY - dotY) < snakeSize:
		snakeLinks.append({'x':prevX,'y':prevY})
		
		###TODO: Change location of dot to random coordinates
		
	#Refresh the screen contents
	screen.fill((0,0,0))

	#Update the snake link's coordinates and draw them
	snakeLinks = snakeLib.updateLinks(screen, (255,255,255), snakeLinks, snakeSize, snakeX, snakeY)

	#Draw the dot
	pygame.draw.rect(screen, RGB, pygame.Rect(dotX,dotY,dotSize,dotSize))
	RGB = snakeLib.rainbowRGB(RGB)

	#Update the display
	pygame.display.flip()
	
	#Set frame rate
	clock.tick(10)
