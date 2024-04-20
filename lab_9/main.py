import pygame
import random

pygame.init()

# 定义窗口大小和方块大小
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 600
BLOCK_SIZE = 30

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 定义形状的列表
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[1, 1, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[1, 1, 0],
     [0, 1, 1]],

    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 1, 1],
     [1, 0, 0]],

    [[1, 1, 1],
     [0, 0, 1]]
]


class TetrisGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('俄罗斯方块')
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_shape = self.new_shape()

    def new_shape(self):
        shape = random.choice(SHAPES)
        color = random.choice(list(pygame.color.THECOLORS.keys()))  # 将dict_keys转换为列表
        return {'shape': shape, 'color': pygame.color.Color(color),
                'x': SCREEN_WIDTH // 2 // BLOCK_SIZE * BLOCK_SIZE - len(shape[0]) * BLOCK_SIZE // 2, 'y': 0}

    def draw_shape(self, shape, offset):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, shape['color'], (shape['x'] + x * BLOCK_SIZE + offset[0], shape['y'] + y * BLOCK_SIZE + offset[1], BLOCK_SIZE, BLOCK_SIZE))

    def check_collision(self, shape, offset):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    board_x = (offset[0] + x * BLOCK_SIZE) // BLOCK_SIZE  # 使用传入的偏移量计算形状在板上的位置
                    board_y = (offset[1] + y * BLOCK_SIZE) // BLOCK_SIZE
                    if board_x < 0 or board_x >= len(self.board[0]) or board_y >= len(self.board) or \
                            self.board[board_y][board_x]:
                        return True
        return False
    def merge_shape(self):
        for y, row in enumerate(self.current_shape['shape']):
            for x, cell in enumerate(row):
                if cell:
                    board_x = (self.current_shape['x'] // BLOCK_SIZE) + x
                    board_y = (self.current_shape['y'] // BLOCK_SIZE) + y
                    self.board[board_y][board_x] = self.current_shape['color']  # 将颜色赋值给形状对应的位置
        self.current_shape = self.new_shape()
        if self.check_collision(self.current_shape['shape'], (0, 0)):
            self.game_over = True

    def check_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))
        return len(lines_to_clear)

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and not self.check_collision(self.current_shape['shape'], (-BLOCK_SIZE, 0)):
                        self.current_shape['x'] -= BLOCK_SIZE
                    elif event.key == pygame.K_RIGHT and not self.check_collision(self.current_shape['shape'], (BLOCK_SIZE, 0)):
                        self.current_shape['x'] += BLOCK_SIZE
                    elif event.key == pygame.K_DOWN and not self.check_collision(self.current_shape['shape'], (0, BLOCK_SIZE)):
                        self.current_shape['y'] += BLOCK_SIZE
                    elif event.key == pygame.K_UP:
                        rotated_shape = list(zip(*reversed(self.current_shape['shape'])))
                        if not self.check_collision(rotated_shape, (0, 0)):
                            self.current_shape['shape'] = rotated_shape

            if not self.check_collision(self.current_shape['shape'], (0, BLOCK_SIZE)):
                self.current_shape['y'] += BLOCK_SIZE
            else:
                self.merge_shape()
                lines_cleared = self.check_lines()
                print(f"Lines cleared: {lines_cleared}")

            self.screen.fill(WHITE)
            for y, row in enumerate(self.board):
                for x, color in enumerate(row):
                    if color:
                        pygame.draw.rect(self.screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

            self.draw_shape(self.current_shape, (0, 0))

            pygame.display.update()
            self.clock.tick(10)


if __name__ == '__main__':
    game = TetrisGame()
    game.run()
