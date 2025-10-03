import pygame
import sys
import math
import numpy as np

# Initialize Pygame
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

# Create simple jump sound using numpy
def create_simple_beep():
    duration = 0.15
    sample_rate = 22050
    frames = int(duration * sample_rate)

    # Create a simple sine wave using numpy
    t = np.linspace(0, duration, frames, False)
    # Create a "boing" sound - frequency drops over time
    frequency = 600 * np.exp(-t * 8)  # Frequency starts at 600Hz and drops
    wave = np.sin(2 * np.pi * frequency * t) * np.exp(-t * 5) * 0.3

    # Convert to 16-bit integers
    wave = (wave * 32767).astype(np.int16)

    # Make it stereo
    stereo_wave = np.column_stack((wave, wave))

    return pygame.sndarray.make_sound(stereo_wave)

# Create victory sound
def create_victory_sound():
    duration = 0.8
    sample_rate = 22050
    frames = int(duration * sample_rate)

    # Create a happy ascending melody
    t = np.linspace(0, duration, frames, False)

    # Victory melody: C-E-G-C (do-mi-sol-do)
    note_duration = duration / 4
    melody = np.zeros(frames)

    frequencies = [262, 330, 392, 523]  # C4, E4, G4, C5

    for i, freq in enumerate(frequencies):
        start_idx = int(i * note_duration * sample_rate)
        end_idx = int((i + 1) * note_duration * sample_rate)
        if end_idx > frames:
            end_idx = frames

        note_t = t[start_idx:end_idx] - t[start_idx]
        note_wave = np.sin(2 * np.pi * freq * note_t) * np.exp(-note_t * 2) * 0.4
        melody[start_idx:end_idx] = note_wave

    # Convert to 16-bit integers
    melody = (melody * 32767).astype(np.int16)

    # Make it stereo
    stereo_melody = np.column_stack((melody, melody))

    return pygame.sndarray.make_sound(stereo_melody)

# Try to create sounds
jump_sound = None
victory_sound = None

try:
    jump_sound = create_simple_beep()
    print("Jump sound created successfully!")
except Exception as e:
    print(f"Jump sound creation failed: {e}")
    jump_sound = None

try:
    victory_sound = create_victory_sound()
    print("Victory sound created successfully!")
except Exception as e:
    print(f"Victory sound creation failed: {e}")
    victory_sound = None

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)
YELLOW = (255, 255, 0)
CLOUD_WHITE = (248, 248, 255)
TREE_GREEN = (34, 139, 34)
TREE_BROWN = (139, 69, 19)

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

# Physics variables
velocity_y = 0
gravity = 0.8
jump_strength = -15
on_ground = False

# Floor position (y coordinate where floor starts)
floor_y = 400

# Floor segments (to create gaps)
floor_segments = [
    (0, floor_y, 250, 100),      # Left side of floor
    (400, floor_y, 300, 100),    # Right side of floor (gap from 250-400)
]

# Platforms (x, y, width, height)
platforms = [
    (200, 350, 120, 20),  # First platform
    (400, 280, 120, 20),  # Higher platform
    (600, 220, 100, 20),  # Even higher platform
]

# Character size
char_width = 50
char_height = 50

# Goal area (x, y, width, height)
goal_area = (650, 170, 50, 50)
level_complete = False
victory_sound_played = False

# Bird animation
bird_x = 0
bird_frame = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    # User pressed down a key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_change_x
    if keys[pygame.K_RIGHT]:
        rect_x += rect_change_x
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_strength
        # Play jump sound
        if jump_sound:
            jump_sound.play()

    # Update bird animation
    bird_x += 2
    bird_frame += 1
    if bird_x > 750:  # Reset when off screen
        bird_x = -50

    # Apply gravity
    velocity_y += gravity
    rect_y += velocity_y

    # Reset ground state
    on_ground = False

    # Check all solid surfaces (platforms and floor segments)
    all_surfaces = platforms + floor_segments

    for surface in all_surfaces:
        surface_x, surface_y, surface_w, surface_h = surface

        # Check if character is overlapping with surface
        if (rect_x < surface_x + surface_w and
            rect_x + char_width > surface_x and
            rect_y < surface_y + surface_h and
            rect_y + char_height > surface_y):

            # If falling down and character's bottom is close to surface top
            if velocity_y > 0 and rect_y + char_height > surface_y and rect_y < surface_y:
                rect_y = surface_y - char_height
                velocity_y = 0
                on_ground = True

    # Check if character fell off the screen (death)
    if rect_y > 600:  # Fell below screen
        rect_x = 50   # Reset position
        rect_y = 50
        velocity_y = 0
        level_complete = False
        victory_sound_played = False  # Reset so victory sound can play again

    # Check win condition
    goal_rect = pygame.Rect(goal_area[0], goal_area[1], goal_area[2], goal_area[3])
    char_rect = pygame.Rect(rect_x, rect_y, char_width, char_height)
    if char_rect.colliderect(goal_rect):
        if not level_complete and not victory_sound_played:
            # Play victory sound only once
            if victory_sound:
                victory_sound.play()
            victory_sound_played = True
        level_complete = True

    # Clear the screen and set the screen background
    screen.fill(SKY_BLUE)

    # Draw sun
    pygame.draw.circle(screen, YELLOW, (600, 80), 40)

    # Draw simple 8-bit clouds
    # Cloud 1
    pygame.draw.rect(screen, CLOUD_WHITE, (100, 100, 60, 30))
    pygame.draw.rect(screen, CLOUD_WHITE, (110, 90, 40, 20))
    pygame.draw.rect(screen, CLOUD_WHITE, (120, 110, 30, 20))

    # Cloud 2
    pygame.draw.rect(screen, CLOUD_WHITE, (300, 60, 80, 35))
    pygame.draw.rect(screen, CLOUD_WHITE, (315, 50, 50, 25))
    pygame.draw.rect(screen, CLOUD_WHITE, (330, 75, 40, 25))

    # Draw background trees
    # Tree 1
    pygame.draw.rect(screen, TREE_BROWN, (50, 300, 15, 100))  # trunk
    pygame.draw.rect(screen, TREE_GREEN, (30, 280, 55, 40))   # leaves

    # Tree 2
    pygame.draw.rect(screen, TREE_BROWN, (750-25, 320, 20, 80))  # trunk (off right edge)
    pygame.draw.rect(screen, TREE_GREEN, (750-45, 300, 60, 40))   # leaves

    # Draw animated bird
    bird_y = 120 + int(10 * pygame.math.Vector2(0, 1).rotate(bird_frame * 5).y)  # Simple wave motion

    # Simple 8-bit bird (alternating wing positions)
    if (bird_frame // 10) % 2 == 0:  # Wings up
        pygame.draw.rect(screen, BLACK, (bird_x, bird_y, 8, 4))      # body
        pygame.draw.rect(screen, BLACK, (bird_x-2, bird_y-2, 4, 2))  # left wing up
        pygame.draw.rect(screen, BLACK, (bird_x+6, bird_y-2, 4, 2))  # right wing up
    else:  # Wings down
        pygame.draw.rect(screen, BLACK, (bird_x, bird_y, 8, 4))      # body
        pygame.draw.rect(screen, BLACK, (bird_x-2, bird_y+4, 4, 2))  # left wing down
        pygame.draw.rect(screen, BLACK, (bird_x+6, bird_y+4, 4, 2))  # right wing down

    # Draw floor segments
    for floor_segment in floor_segments:
        pygame.draw.rect(screen, BLACK, floor_segment)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)

    # Draw goal area
    pygame.draw.rect(screen, GREEN, goal_area)

    # Draw character
    pygame.draw.rect(screen, RED, [rect_x, rect_y, char_width, char_height])

    # Draw win message
    if level_complete:
        font = pygame.font.Font(None, 74)
        text = font.render("LEVEL COMPLETE!", True, BLACK)
        screen.blit(text, (175, 50))

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
sys.exit()
