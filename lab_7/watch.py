
import pygame
import sys
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Clock")

mickey_image = pygame.image.load("mickeyclock.jpeg")
mickey_width, mickey_height = mickey_image.get_width(), mickey_image.get_height()

center_x, center_y = screen_width // 2, screen_height // 2

hour_hand_length = 100
minute_hand_length = 150
second_hand_length = 200


def draw_clock():
    screen.fill((255, 255, 255))  # Fill screen with white color

    screen.blit(mickey_image, (center_x - mickey_width // 2, center_y - mickey_height // 2))

    current_time = datetime.now().time()
    hour = current_time.hour % 12  # Convert to 12-hour format
    minute = current_time.minute
    second = current_time.second

    hour_angle = (hour / 12) * 360 + (minute / 60) * 30 - 90
    minute_angle = (minute / 60) * 360 + (second / 60) * 6 - 90
    second_angle = (second / 60) * 360 - 90

    hour_x = center_x + hour_hand_length * math.cos(math.radians(hour_angle))
    hour_y = center_y + hour_hand_length * math.sin(math.radians(hour_angle))
    minute_x = center_x + minute_hand_length * math.cos(math.radians(minute_angle))
    minute_y = center_y + minute_hand_length * math.sin(math.radians(minute_angle))
    second_x = center_x + second_hand_length * math.cos(math.radians(second_angle))
    second_y = center_y + second_hand_length * math.sin(math.radians(second_angle))

    # Draw hands
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (hour_x, hour_y), 8)  # Hour hand
    pygame.draw.line(screen, (255, 0, 0), (center_x, center_y), (minute_x, minute_y), 4)  # Minute hand
    pygame.draw.line(screen, (0, 0, 255), (center_x, center_y), (second_x, second_y), 2)  # Second hand

    # Update the display
    pygame.display.flip()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock()
    pygame.time.delay(100)  # Delay to limit frame rate

pygame.quit()
sys.exit()
