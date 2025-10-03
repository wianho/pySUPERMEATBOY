import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    # User pressed down a key
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_UP]:
        rect_y -= rect_change_y
    if keys[pygame.K_DOWN]:
        rect_y += rect_change_y
    if keys[pygame.K_LEFT]:
        rect_x -= rect_change_x
    if keys[pygame.K_RIGHT]:
        rect_x += rect_change_x

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    # Draw here
    pygame.draw.rect(screen, RED, [rect_x, rect_y, 100, 100])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
sys.exit()
