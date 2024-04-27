
# 连接databes，添加两个button，一个可以删除数据，一个可以添加数据，用pygame，scrren.blit. where .. selecet from ...add to databes,remove...AVG..limit,abset`
import pygame
import mysql.connector

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MySQL in Pygame")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
color1 = (26, 188, 156)
color2 = (126, 121, 145)
db_config = {
    'host': 'localhost',
    'user': 'my_booksite_bda',
    'password': '12344321',
    'database': 'my_booksite',
    'port': 3306,
}

def add_content():
    name = input("атын жазыңыз: ")
    age = int(input("Жасын жазыңыз: "))
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "INSERT INTO person (name, age) VALUES (%s, %s);"
    cursor.execute(query, (name, age))
    connection.commit()
    print("Сәтті сақталды!")
    cursor.close()
    connection.close()

def delete_content():
    id_to_delete = int(input("Enter ID to delete: "))
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    query = "DELETE FROM person WHERE ID = %s;"
    cursor.execute(query, (id_to_delete,))
    connection.commit()
    print("Сәтті жойылды!")
    cursor.close()
    connection.close()

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

#
query = "SELECT * FROM person ORDER BY ID;"
cursor.execute(query)
result = cursor.fetchall()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if add_button_rect.collidepoint(mouse_pos):
                add_content()
            elif delete_button_rect.collidepoint(mouse_pos):
                delete_content()

    screen.fill(WHITE)


    font = pygame.font.Font(None, 24)
    y = 40
    for row in result:
        text = f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}"
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, y))
        y += 20


    add_button_rect = pygame.draw.rect(screen, color1, (50, 50, 100, 50))
    delete_button_rect = pygame.draw.rect(screen, color2, (50, 150, 100, 50))


    add_text = font.render("Қосу", True, BLACK)
    delete_text = font.render("Жою", True, BLACK)
    screen.blit(add_text, (65, 65))
    screen.blit(delete_text, (65, 165))


    pygame.display.flip()

pygame.quit()


