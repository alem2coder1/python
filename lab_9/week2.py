import pygame
import random
pygame.init()
screen = pygame.display.set_mode((900, 360))
background = pygame.image.load("image/wall.jpeg")

right = [
    pygame.image.load("image/r1.png"),
    pygame.image.load("image/r2.png"),
    pygame.image.load("image/r3.png"),
    pygame.image.load("image/r4.png"),
]
left = [
    pygame.image.load("image/l1.png"),
    pygame.image.load("image/l2.png"),
    pygame.image.load("image/l3.png"),
    pygame.image.load("image/l4.png"),

]
coin_image = pygame.image.load("image/coin_image.jpg")

jump_images = [
    pygame.image.load("image/r4.png"),
    pygame.image.load("image/l4.png"),
]

clock = pygame.time.Clock()
x, y = (100, 220)
counter = 0
background_pos = 0

done = False
jump = False
is_still_pressed = False
jump_direction = -10
direction = left  # 初始朝向为左
direction_move = 0  # 初始化移动方向

while not done:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not jump:  # 确保不处于跳跃状态时才能触发跳跃
                jump = True
                jump_direction = -10  # 重置跳跃方向

        if event.type == pygame.KEYUP and event.key != pygame.K_SPACE:
            is_still_pressed = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if not jump:  # 如果不是跳跃状态，才改变朝向
                direction = right
            direction_move = -10
            is_still_pressed = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if not jump:  # 如果不是跳跃状态，才改变朝向
                direction = left
            direction_move = 10
            is_still_pressed = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if not jump:  # 确保不处于跳跃状态时才能触发跳跃
                jump = True
                y -= 100  # 提高照片的高度

    x += direction_move
    if not jump:
        counter += 1
    if x >= 450:
        x -= 10
        background_pos += -10
    elif x <= 0:
        x = 0
        background_pos += 10

    if background_pos <= -900:
        background_pos = 0
    if jump:
        y += jump_direction
        if y < 80:  # 修改跳跃的高度
            jump_direction = 10
        if y == 220:
            jump = False
            jump_direction = -10

    screen.blit(background, (background_pos, 0))
    screen.blit(background, (background_pos + 900, 0))
    if jump:
        if direction == right:
            screen.blit(jump_images[counter % 2], (x, y))
        else:
            screen.blit(jump_images[counter % 2], (x, y))
    else:
        screen.blit(direction[counter % 4], (x, y))
    clock.tick(10)

print("Finished")