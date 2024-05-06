import pygame
import mysql.connector

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MySQL in Pygame")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color1 = (26, 188, 156)
color2 = (126, 121, 145)

db_config = {
    'host': 'localhost',
    'user': 'my_booksite_bda',
    'password': '12344321',
    'database': 'my_booksite',
    'port': 3306,
}

def is_alpha_string(s):
    return s.isalpha()

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) <= 11


def add_content():
    name = input("Enter name: ")
    if is_alpha_string(name):
        phone = input("Enter phone: ")
        if is_valid_phone(phone):
            try:
                connection = mysql.connector.connect(**db_config)
                cursor = connection.cursor()
                query = "INSERT INTO phonebook (name, phone) VALUES (%s, %s);"
                cursor.execute(query, (name, phone))
                connection.commit()
                print("Successfully inserted!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
            finally:
                cursor.close()
                connection.close()
        else:
            print("Invalid phone number!")
    else:
        print("Invalid name!")

def delete_content():
    name_to_delete = input("Enter name to delete: ")
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "DELETE FROM phonebook WHERE name = %s;"
        cursor.execute(query, (name_to_delete,))
        connection.commit()
        print("Successfully deleted!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

query = "SELECT name, phone FROM phonebook ORDER BY name ASC;"
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

                cursor.execute(query)
                result = cursor.fetchall()
            elif delete_button_rect.collidepoint(mouse_pos):
                delete_content()

                cursor.execute(query)
                result = cursor.fetchall()

    screen.fill(WHITE)

    font = pygame.font.Font(None, 24)
    y = 40
    for row in result:
        text = f"Name: {row[0]}, Phone: {row[1]}"
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, y))
        y += 20

    add_button_rect = pygame.draw.rect(screen, color1, (50, 50, 100, 50))
    delete_button_rect = pygame.draw.rect(screen, color2, (50, 150, 100, 50))

    add_text = font.render("Add", True, BLACK)
    delete_text = font.render("Delete", True, BLACK)
    screen.blit(add_text, (65, 65))
    screen.blit(delete_text, (65, 165))

    pygame.display.flip()

pygame.quit()
