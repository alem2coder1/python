import pygame
import sys
import random
import time
from pygame.locals import *
import mysql.connector

# 定义颜色变量
black_colour = pygame.Color(28, 56, 20)
white_colour = pygame.Color(255, 144, 20)
red_colour = pygame.Color(255, 34, 20)
grey_colour = pygame.Color(150, 150, 150)
db_config = {
    'host': 'localhost',
    'user': 'my_booksite_bda',
    'password': '12344321',
    'database': 'my_booksite',
    'port': 3306,
}

# 初始化pygame
pygame.init()

# 定义游戏结束函数
def gameover(gamesurface):
    # 设置提示字体的格式
    gameover_font = pygame.font.SysFont("MicrosoftYaHei", 16)
    # 设置提示字体的颜色
    gameover_colour = gameover_font.render('GameOver', True, grey_colour)
    # 设置提示位置
    gameover_location = gameover_colour.get_rect()
    gameover_location.midtop = (310, 200)
    # 绑定以上设置到句柄
    gamesurface.blit(gameover_colour, gameover_location)
    # 提示运行信息
    pygame.display.flip()
    # 休眠5秒
    time.sleep(5)
    # 退出游戏
    pygame.quit()
    # 退出程序
    sys.exit()

# 定义用户登录函数
def user_login():
    print("Welcome to Snake Game!")
    name = input("Please enter your username: ")
    password = input("Please enter your password: ")
    # 连接到数据库
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    # 执行查询语句
    query = "SELECT level, speed FROM userpy WHERE name = %s AND password = %s"
    cursor.execute(query, (name, password))
    user_info = cursor.fetchone()
    # 关闭数据库连接
    cursor.close()
    connection.close()
    if user_info:
        print(f"Welcome back, {name}!")
        print(f"Your current level is {user_info[0]} and speed is {user_info[1]}.")
        return user_info[0], user_info[1]
    else:
        print("User not found. Please register first.")
        sys.exit()

# 定义保存用户信息函数
def save_user_info(level, speed):
    # 连接到数据库
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    # 执行更新语句
    query = "UPDATE userpy SET level = %s, speed = %s WHERE name = 'alem'"
    cursor.execute(query, (level, speed))
    connection.commit()
    # 关闭数据库连接
    cursor.close()
    connection.close()

# 定义主函数
def main(ftpsClock=None):
    # 获取用户信息
    level, speed = user_login()
    # 创建一个窗口
    gamesurface = pygame.display.set_mode((640, 480))
    # 设置窗口的标题
    pygame.display.set_caption('贪吃蛇')
    # 初始化变量
    # 初始化贪吃蛇的起始位置
    snakeposition = [100, 100]
    # 初始化贪吃蛇的长度
    snakelength = [[100, 100], [80, 100], [60, 100]]
    # 初始化目标方块的位置
    square_purpose = [300, 300]
    # 初始化一个数来判断目标方块是否存在
    square_position = 1
    # 初始化方向，用来使贪吃蛇移动
    derection = "right"
    change_derection = derection
    # 初始化吃掉的目标方块数量
    eaten_count = 0
    # 食物持续时间
    food_duration = 5  # 持续5秒
    # 食物生成时间间隔
    food_interval = 10  # 每10秒生成一次食物
    last_food_time = time.time()

    # 进行游戏主循环
    while True:
        # 检测按键等pygame事件
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后，退出程序
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # 判断键盘事件,用w,s,a,d来表示上下左右
                if event.key == K_RIGHT or event.key == ord('d'):
                    change_derection = "right"
                if event.key == K_LEFT or event.key == ord('a'):
                    change_derection = "left"
                if event.key == K_UP or event.key == ord('w'):
                    change_derection = "up"
                if event.key == K_DOWN or event.key == ord('s'):
                    change_derection = "down"
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        # 判断移动的方向是否相反
        if change_derection == 'left' and not derection == 'right':
            derection = change_derection
        if change_derection == 'right' and not derection == 'left':
            derection = change_derection
        if change_derection == 'up' and not derection == 'down':
            derection = change_derection
        if change_derection == 'down' and not derection == 'up':
            derection = change_derection

        # 根据方向，改变坐标
        if derection == 'left':
            snakeposition[0] -= 20
        if derection == 'right':
            snakeposition[0] += 20
        if derection == 'up':
            snakeposition[1] -= 20
        if derection == 'down':
            snakeposition[1] += 20

        # 增加蛇的长度
        snakelength.insert(0, list(snakeposition))

        # 判断是否吃掉目标方块
        if snakeposition[0] == square_purpose[0] and snakeposition[1] == square_purpose[1]:
            square_position = 0
            eaten_count += 1
            # 每吃掉一个食物，蛇长度增加一个单位
            snakelength.append(list(snakelength[-1]))  # 将蛇尾的位置加入到蛇身列表中，使其长度增加一个单位
            if eaten_count % 3 == 0:  # 每吃掉三个方块，速度加快一秒
                speed += 1
                level += 1
                save_user_info(level, speed)
        else:
            snakelength.pop()

        # 判断是否生成新的食物
        if time.time() - last_food_time > food_interval:
            square_position = 0
            last_food_time = time.time()

        # 重新生成目标方块
        if square_position == 0:
            # 随机生成x,y,扩大二十倍，在窗口范围内
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            square_purpose = [int(x * 20), int(y * 20)]
            square_position = 1

        # 绘制pygame显示层
        gamesurface.fill(black_colour)
        for position in snakelength:
            pygame.draw.rect(gamesurface, white_colour, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(gamesurface, red_colour, Rect(square_purpose[0], square_purpose[1], 20, 20))
        # 刷新pygame显示层
        pygame.display.flip()

        # 判断是否死亡
        if snakeposition[0] < 0 or snakeposition[0] > 620:
            gameover(gamesurface)
        if snakeposition[1] < 0 or snakeposition[1] > 460:
            gameover(gamesurface)
        for snakebody in snakelength[1:]:
            if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                gameover(gamesurface)

        # 控制游戏速度
        ftpsClock.tick(speed)


if __name__ == "__main__":
    clock = pygame.time.Clock()
    main(clock)
