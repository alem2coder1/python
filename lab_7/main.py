import pygame
import sys

# 初始化 Pygame，initialization
pygame.init()

# 设置窗口尺寸
win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
icon = pygame.image

# 设置窗口标题
pygame.display.set_caption("My Pygame pp2")

# 定义颜色
RED = (255, 0, 0)
BLUE = (0, 0, 255)
circle_x = win_width // 2
circle_y = win_height // 2
circle_radius = 50
circle_speed_x = 0
circle_speed_y = 0

running = True
while running:
    # 事件处理，event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 根据按键事件改变速度方向
            if event.key == pygame.K_UP:
                circle_speed_x = 0
                circle_speed_y = -5
            elif event.key == pygame.K_DOWN:
                circle_speed_x = 0
                circle_speed_y = 5
            elif event.key == pygame.K_LEFT:
                circle_speed_x = -5
                circle_speed_y = 0
            elif event.key == pygame.K_RIGHT:
                circle_speed_x = 5
                circle_speed_y = 0

    # 更新圆形位置
    circle_x += circle_speed_x
    circle_y += circle_speed_y

    # 确保圆形不会超出窗口边界
    if circle_x - circle_radius < 0:
        circle_x = circle_radius
    elif circle_x + circle_radius > win_width:
        circle_x = win_width - circle_radius
    if circle_y - circle_radius < 0:
        circle_y = circle_radius
    elif circle_y + circle_radius > win_height:
        circle_y = win_height - circle_radius

    # 填充窗口背景为白色
    win.fill((255, 255, 255))

    # 绘制蓝色圆形
    pygame.draw.circle(win, BLUE, (circle_x, circle_y), circle_radius)

    # 更新显示
    pygame.display.update()

    # 控制帧率
    pygame.time.Clock().tick(60)
# 游戏主循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充窗口背景为白色
    win.fill((255, 255, 255))

    # 绘制红色矩形
    pygame.draw.rect(win, RED, (100, 100, 50, 50))
    pygame.draw.circle(win, BLUE, (win_width // 2, win_height // 2), 50)
    # 更新显示
    pygame.display.update()

# 退出 Pygame
pygame.quit()
sys.exit()
