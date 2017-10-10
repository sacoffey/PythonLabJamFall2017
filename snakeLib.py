import pygame

#Updates the snake links coordinates by shifting, then draws each new link on the screen
def updateLinks(screen, RGB, snakeLinks, snakeSize, newX, newY):
	prevX = 0
	prevY = 0
	for link in snakeLinks:
		prevX = link['x']
		prevY = link['y']
		link['x'] = newX
		link['y'] = newY
		newX = prevX
		newY = prevY
		pygame.draw.rect(screen, RGB, pygame.Rect(link['x'],link['y'],snakeSize,snakeSize))
	return snakeLinks
		
		
#When called every frame, creates a rainbow effect
def rainbowRGB(RGB):
	if(RGB[0] == 250 and RGB[1] < 250 and RGB[2] == 0):
		RGB[1] += 10
	elif(RGB[0] > 0 and RGB[1] == 250 and RGB[2] == 0):
		RGB[0] -= 10
	elif(RGB[0] == 0 and RGB[1] == 250 and RGB[2] < 250):
		RGB[2] += 10
	elif(RGB[0] == 0 and RGB[1] > 0 and RGB[2] == 250):
		RGB[1] -= 10
	elif(RGB[0] < 250 and RGB[1] == 0 and RGB[2] == 250):
		RGB[0] += 10
	elif(RGB[0] == 250 and RGB[1] == 0 and RGB[2] > 0):
		RGB[2] -= 10
	
	return RGB
	
