import pygame

pygame.init()

win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Music Player")

music_list = ["music1.mp3", "music2.mp3", ]
current_music_index = 0
pygame.mixer.music.load(music_list[current_music_index])
font = pygame.font.SysFont(None, 36)

button_width, button_height = 200, 100
button_x, button_y = (win_width - button_width) // 2, (win_height - button_height) // 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

playing = False


def draw_button():
    pygame.draw.rect(win, WHITE, (button_x, button_y - 150, button_width, button_height))
    pygame.draw.rect(win, WHITE, (button_x - 200, button_y, button_width, button_height))
    pygame.draw.rect(win, WHITE, (button_x + 200, button_y, button_width, button_height))

    text_play_pause = font.render("Play/Pause", True, BLACK)
    text_previous = font.render("Previous", True, BLACK)
    text_next = font.render("Next", True, BLACK)

    win.blit(text_play_pause, (button_x + button_width / 2 - text_play_pause.get_width() / 2,
                               button_y - 150 + button_height / 2 - text_play_pause.get_height() / 2))
    win.blit(text_previous, (button_x - 200 + button_width / 2 - text_previous.get_width() / 2,
                             button_y + button_height / 2 - text_previous.get_height() / 2))
    win.blit(text_next, (button_x + 200 + button_width / 2 - text_next.get_width() / 2,
                         button_y + button_height / 2 - text_next.get_height() / 2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_x <= mouse_pos[0] <= button_x + button_width and \
                    button_y - 150 <= mouse_pos[1] <= button_y - 150 + button_height:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif button_x - 200 <= mouse_pos[0] <= button_x - 200 + button_width and \
                    button_y <= mouse_pos[1] <= button_y + button_height:
                current_music_index = (current_music_index - 1) % len(music_list)
                pygame.mixer.music.load(music_list[current_music_index])
                if playing:
                    pygame.mixer.music.play()
            elif button_x + 200 <= mouse_pos[0] <= button_x + 200 + button_width and \
                    button_y <= mouse_pos[1] <= button_y + button_height:
                current_music_index = (current_music_index + 1) % len(music_list)
                pygame.mixer.music.load(music_list[current_music_index])
                if playing:
                    pygame.mixer.music.play()

    win.fill(BLACK)
    draw_button()
    pygame.display.update()

pygame.quit()
