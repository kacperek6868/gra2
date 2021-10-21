# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys, pygame, datetime
pygame.init()


clock = pygame.time.Clock()
fps = 60

screen_width = 2560
screen_height = 1440

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('tło_gry')


#wartości
tlo_scroll = 0
scroll_speed = 2

#zdjecia
tlo_tyl = pygame.image.load('tło_tło_tło.png')

run = True
while run:

    clock.tick(fps)

    #wyswietlanie i poruszanie tłem

    screen.blit(tlo_tyl, (tlo_scroll, 0))
    tlo_scroll -= scroll_speed
    if abs(tlo_scroll) > 21590:
        tlo_scroll = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

