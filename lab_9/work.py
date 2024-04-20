import pygame
import sys
import time
import math
from pygame.locals import *

# Define colors
black_colour = pygame.Color(0, 0, 0)
white_colour = pygame.Color(255, 255, 255)
red_colour = pygame.Color(255, 0, 0)
green_colour = pygame.Color(0, 255, 0)
blue_colour = pygame.Color(0, 0, 255)
grey_colour = pygame.Color(150, 150, 150)


# Game over function
def gameover(gamesurface):
    gameover_font = pygame.font.SysFont("MicrosoftYaHei", 16)
    gameover_colour = gameover_font.render('GameOver', True, grey_colour)
    gameover_location = gameover_colour.get_rect()
    gameover_location.midtop = (310, 200)
    gamesurface.blit(gameover_colour, gameover_location)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()



def draw_square(surface, color, x, y, size):
    pygame.draw.rect(surface, color, (x, y, size, size))



def draw_right_triangle(surface, color, x, y, base, height):
    points = [(x, y), (x + base, y), (x, y - height)]
    pygame.draw.polygon(surface, color, points)



def draw_equilateral_triangle(surface, color, x, y, side):
    height = side * math.sqrt(3) / 2
    points = [(x, y), (x + side, y), (x + side / 2, y - height)]
    pygame.draw.polygon(surface, color, points)


def draw_hexagon(surface, color, x, y, side_length):

    height = side_length * math.sqrt(3) / 2


    points = [(x + side_length * math.cos(math.radians(angle)),
               y + side_length * math.sin(math.radians(angle)))
              for angle in range(0, 360, 60)]
    pygame.draw.polygon(surface, color, points)



def draw_rhombus(surface, color, x, y, side, angle):
    half_diagonal = side / 2
    points = [(x + half_diagonal, y),
              (x + side, y + half_diagonal),
              (x + half_diagonal, y + side),
              (x, y + half_diagonal)]
    rotated_points = []
    for px, py in points:
        # Rotate the points
        rotated_x = math.cos(math.radians(angle)) * (px - x) - math.sin(math.radians(angle)) * (py - y) + x
        rotated_y = math.sin(math.radians(angle)) * (px - x) + math.cos(math.radians(angle)) * (py - y) + y
        rotated_points.append((rotated_x, rotated_y))
    pygame.draw.polygon(surface, color, rotated_points)



def main():
    pygame.init()
    pygame.time.Clock()
    ftpsClock = pygame.time.Clock()
    gamesurface = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Shapes Drawing')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        gamesurface.fill(white_colour)

        # 画正方形
        draw_square(gamesurface, red_colour, 50, 50, 100)

        # 画直角三角形
        draw_right_triangle(gamesurface, green_colour, 200, 450, 100, 100)

        # 画等边三角形
        draw_equilateral_triangle(gamesurface, blue_colour, 400, 450, 100)

        # 四菱形
        draw_rhombus(gamesurface, grey_colour, 600, 450, 100, 105)

        # 六菱形
        draw_hexagon(gamesurface, black_colour, 300, 100, 100)

        pygame.display.update()
        ftpsClock.tick(30)


if __name__ == "__main__":
    main()
