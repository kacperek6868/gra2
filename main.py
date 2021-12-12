import sys
import pygame
import datetime
import math
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440
CZAS_KOLIZJI = datetime.timedelta(seconds=2)
REKAX = 300
REKAY = 0
SRODEK_REKI = (58, 285)
REKA_IMAGE = "reka3.png"
FONT = pygame.freetype.Font("CollegiateBlackFLF.ttf", 24)


class TextScore(pygame.sprite.Sprite):
    def __init__(self, fontname="CollegiateBlackFLF.ttf", fontsize=200, colorkey=WHITE, transparency=255, text='15'):
        super().__init__()

        self.GAME_FONT = pygame.freetype.Font(fontname, fontsize)
        self.text = text
        text_surface, rect = self.GAME_FONT.render(text, (0, 0, 0))
        self.original_image = text_surface.convert_alpha()
        self.image = self.original_image
        #self.temp_filename = filename
        self.temp_colorkey = colorkey
        self.temp_transparency = transparency
        self.rotated_image = None
        self.rotated_image_rect = None
        self.angle_temp = 0

        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        self.image.set_colorkey(colorkey)
        self.image.set_alpha(transparency)
        self.rect = self.image.get_rect()
        self.angle = 0

    def update(self, pos=(120, 120)):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def updateText(self, text):
        self.text = text
        text_surface, rect = self.GAME_FONT.render(self.text, (0, 0, 0))
        self.original_image = text_surface.convert_alpha()
        self.image = self.original_image
        self.rotated_image = None
        self.rotated_image_rect = None
        self.angle_temp = 0

        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        self.image.set_colorkey(self.temp_colorkey)
        self.image.set_alpha(self.temp_transparency)
        self.rect = self.image.get_rect()


class Menu(pygame.sprite.Sprite):
    def __init__(self, filename, colorkey=BLACK, transparency=255):
        super().__init__()

        self.original_image = pygame.image.load(filename).convert()
        self.image = self.original_image

        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        self.image.set_colorkey(colorkey)
        self.image.set_alpha(transparency)
        self.rect = self.image.get_rect()

class Hearts(pygame.sprite.Sprite):
    def __init__(self, filename, rect):
        super().__init__()

        self.rect.x = rect[0]
        self.rect.y = rect[1]
        self.original_image = pygame.image.load(filename).convert_alpha()
        self.image = self.original_image
        self.temp_filename = filename
        #self.temp_colorkey = colorkey
        #self.temp_transparency = transparency

        self.rotated_image = None
        self.rotated_image_rect = None
        self.angle_temp = 0

        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        #self.image.set_colorkey(colorkey)
        #self.image.set_alpha(transparency)
        self.rect = self.image.get_rect()
        self.angle = 0

    def update(self, pos):
        # print("klik w miejscu: ", pos)
        self.angle_temp = math.atan2(self.rect.x - pos[0], self.rect.y - pos[1]) / math.pi * 180
        # print("kąt: ", angle_temp)
        self.image = pygame.transform.rotate(self.original_image, self.angle_temp)
        # print("pozycja snajpera: ", (self.rect.x, self.rect.y))

    def take_damage(self, filename):
        self.temp_image = self.original_image
        self.original_image = pygame.image.load(filename).convert_alpha()
        self.image = self.original_image


    def damage_restore(self):
        self.original_image = self.temp_image
        self.original_image = pygame.image.load(self.temp_filename).convert_alpha()
        self.image = self.original_image


class GameObject(pygame.sprite.Sprite):
    def __init__(self, filename, body=None):
        super().__init__()

        self.original_image = pygame.image.load(filename).convert_alpha()
        self.image = self.original_image
        self.temp_filename = filename
        #self.temp_colorkey = colorkey
        #self.temp_transparency = transparency
        self.body = body
        self.rotated_image = None
        self.rotated_image_rect = None
        self.angle_temp = 0

        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        #self.image.set_colorkey(colorkey)
        #self.image.set_alpha(transparency)
        self.rect = self.image.get_rect()
        self.angle = 0

    def update(self, pos):
        # print("klik w miejscu: ", pos)
        # print("rect: ",  self.rect, pos)
        #self.angle_temp = math.atan2(self.rect.x - pos[0], self.rect.y - pos[1]) / math.pi * 180
        #self.angle_temp = math.atan2(0 - pos[0], 0 - pos[1]) / math.pi * 180
        #self.angle_temp = math.atan2(self.rect.x - 0, self.rect.y - 1) / math.pi * 180
        # print("kąt: ", angle_temp)
        self.image = pygame.transform.rotate(self.original_image, self.angle_temp)
        print("rect: ", self.rect.y, pos)
        #self.blitRotate(image=self.original_image, pos=self.body.rect, originPos=SRODEK_REKI, angle=self.angle_temp)
        # print("pozycja snajpera: ", (self.rect.x, self.rect.y))

    def kolizja_start(self, filename):
        self.temp_image = self.original_image
        self.original_image = pygame.image.load(filename).convert_alpha()
        self.image = self.original_image
        #self.image.set_colorkey(colorkey)
        #self.image.set_alpha(transparency)
        print("kolizja start ", str(datetime.datetime.now()))
        # self.rect = self.image.get_rect()

    def kolizja_stop(self):
        self.original_image = self.temp_image
        print("kolizja stop ", str(datetime.datetime.now()))
        self.original_image = pygame.image.load(self.temp_filename).convert_alpha()
        self.image = self.original_image
        #self.image.set_colorkey(self.temp_colorkey)
        #self.image.set_alpha(self.temp_transparency)
        # self.image = self.original_image
        # self.image.set_colorkey(colorkey)
        # self.image.set_alpha(transparency)





    def przesun(self, pos):
        self.rect.x = self.rect.x + pos[0]
        self.rect.y = self.rect.y + pos[1]
        if self.body != None:
            self.body.rect.x = self.body.rect.x + pos[0]
            self.body.rect.y = self.body.rect.y + pos[1]


#self, image, pos, originPos, angle

    # def blitRotate(self, originPos, pos):
    #
    #     #angle to mouse
    #     #self.angle_temp = math.atan2(self.rect.x - pos[0], self.rect.y - pos[1]) / math.pi * 180
    #     angle = math.atan2(obiekt.rect.x - pos[0], obiekt.rect.y - pos[1]) / math.pi * 180
    #
    #
    #     # offset from pivot to center
    #     image_rect = self.image.get_rect(topleft=(self.rect.x - originPos[0], self.rect.y - originPos[1]))
    #     offset_center_to_pivot = pygame.math.Vector2((self.rect.x, self.rect.y)) - image_rect.center
    #
    #     # roatated offset from pivot to center
    #     rotated_offset = offset_center_to_pivot.rotate(-angle)
    #
    #     # roatetd image center
    #     rotated_image_center = (self.rect.x - rotated_offset.x, self.rect.y - rotated_offset.y)
    #
    #     # get a rotated image
    #     self.image = pygame.transform.rotate(self.image, angle)
    #     rotated_image_rect = self.image.get_rect(center=rotated_image_center)
    #
    #     # # rotate and blit the image
    #     # # surf.blit(rotated_image, rotated_image_rect)
    #     # #
    #     # # # draw rectangle around the image
    #     # # pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()), 2)

    def blitRotate(self, image, pos, originPos, angle):
        # offset from pivot to center
        image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # roatated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # roatetd image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        # rotate and blit the image
        # surf.blit(rotated_image, rotated_image_rect)

        # draw rectangle around the image



class Player(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()

        self.original_image = pygame.image.load(filename).convert_alpha()
        self.image = self.original_image
        self.temp_filename = filename

        self.rect = self.image.get_rect()
        self.angle = 0

    def update(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def kolizja_start(self, filename):
        self.temp_image = self.original_image
        self.original_image = pygame.image.load(filename).convert_alpha()
        self.image = self.original_image
        #self.image.set_colorkey(colorkey)
        #self.image.set_alpha(transparency)
        print("kolizja start ", str(datetime.datetime.now()))


    def kolizja_stop(self):
        self.original_image = self.temp_image
        print("kolizja stop ", str(datetime.datetime.now()))
        self.original_image = pygame.image.load(self.temp_filename).convert_alpha()
        self.image = self.original_image

    def animacja(self, filename):
        self.temp_image = self.original_image
        self.original_image = pygame.image.load(filename).convert_alpha()
        self.image = self.original_image
        #self.image.set_colorkey(colorkey)
        #self.image.set_alpha(transparency)
        print("kolizja start ", str(datetime.datetime.now()))




    # def kolizja_stop(self):
    #     self.original_image = self.temp_image
    #     print("kolizja stop ", str(datetime.datetime.now()))
    #     self.original_image = pygame.image.load(self.temp_filename).convert_alpha()
    #     self.image = self.original_image

class Obsticle(GameObject):
    def __init__(self, filename, rect):
        super().__init__(filename)
        self.rect.x = rect[0]
        self.rect.y = rect[1]
        print(self.rect)

    def update(self, pos):
        self.rect.x = self.rect.x - 9
        self.rect.y = self.rect.y - 3

    def return_to_start(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        return random.randint(0, 4 * SCREEN_WIDTH)

    def kolizja(self):
        self.return_to_start((SCREEN_WIDTH + 1100, SCREEN_HEIGHT + 1600))



clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('tło_gry')

#define font
font = pygame.font.SysFont('Bauhaus 93', 60)



# wartości
tlo_scroll = 0
scroll_speed = 2
ziemia_scroll = 0
ziemia_speed = 20

# zdjecia
tlo_tyl = pygame.image.load('tło_tło_tło.png').convert()
tlo_ziemia = pygame.image.load('ziemia_1.png').convert_alpha()
tytul = pygame.image.load('tytul.png').convert_alpha()


#mis = pygame.image.load('mis111.png').convert_alpha()
mis = Player('mis111.png')
wynik = TextScore(fontname="CollegiateBlackFLF.ttf")
wynik.rect.x = 200
wynik.rect.y = 200

all_sprite_list = pygame.sprite.Group()
serca_list = pygame.sprite.Group()
#reka3 = pygame.image.load("reka3.png").convert_alpha()
obiekt = GameObject("reka3.png", body=mis)
przeszkoda = Obsticle(filename="skrzynka_rotate.png", rect=(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 500))
serce3 =Player("serce1.png",)
serce2 =Player("serce1.png") #, rect=(SCREEN_WIDTH - 450, SCREEN_HEIGHT - 1400)
serce1 =Player("serce1.png") #, rect=(SCREEN_WIDTH - 650, SCREEN_HEIGHT - 1400)
obiekt.rect.x = SCREEN_WIDTH / 2
obiekt.rect.y = SCREEN_HEIGHT / 2
serce3.rect.x = SCREEN_WIDTH - 250
serce3.rect.y = SCREEN_HEIGHT - 1400
serce2.rect = (SCREEN_WIDTH - 450, SCREEN_HEIGHT - 1400)
serce1.rect = (SCREEN_WIDTH - 650, SCREEN_HEIGHT - 1400)
# menu
restart_screen = Menu("restart_tło.png", GREEN)
restart_screen.image.set_alpha(0)
game_over_text = Menu("game_over.png", GREEN)
game_over_text.image.set_alpha(0)
game_over_text.rect.center = (1280, 400)
restart_text = Menu("restart.png", GREEN)
restart_text.image.set_alpha(0)
restart_text.rect.center = (1280, 900)
quit_text = Menu("quit.png", GREEN)
quit_text.image.set_alpha(0)
quit_text.rect.center = (1280, 1200)



# dodawanie do all sprite list

all_sprite_list.add(mis)
all_sprite_list.add(obiekt)
all_sprite_list.add(przeszkoda)
all_sprite_list.add(wynik)
#serca_list.add(serce1)
#dserca_list.add(serce2)
serca_list.add(serce3)
serca_list.add(serce2)
serca_list.add(serce1)
# all_sprite_list.add(restart_screen)
# all_sprite_list.add(quit_text)
# all_sprite_list.add(restart_text)
# all_sprite_list.add(game_over_text)

#srodek obrazka
w, h = obiekt.image.get_size()


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def mainMenu():
    menu_tlo_scroll = tlo_scroll
    menu_ziemia_scroll = ziemia_scroll
    #mis.rect.x = 930 - srodek
    mis.rect.x = 700
    mis.rect.y = -700
    timer_start = 0
    timer_end = 0
    obiekt.rect.x = mis.rect.x + REKAX
    while True:
        screen.fill((0, 0, 0))
        screen.blit(tlo_tyl, (menu_tlo_scroll, 0))
        menu_tlo_scroll -= 1
        if abs(menu_tlo_scroll) > 21590:
            menu_tlo_scroll = 0

        screen.blit(tlo_ziemia, (menu_ziemia_scroll, 0.28125 * menu_ziemia_scroll))
        menu_ziemia_scroll -= ziemia_speed
        if abs(menu_ziemia_scroll) > 12800:
            menu_ziemia_scroll = 0

        screen.blit(tytul, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mis.rect.y += 50


        if mis.rect.y > -700:
            mis.rect.y += 50
        if mis.rect.y == 550:
            Game(menu_ziemia_scroll, menu_tlo_scroll)

        all_sprite_list.draw(screen)
        clock.tick(fps)
        pygame.display.update()


#def spadanie():

def Game(game_ziemia_scroll, game_tlo_scroll):
    running = True
    jumping = False
    falling = False
    jumping_timer = 0
    pauza = SCREEN_WIDTH
    czy_kolizja = False
    score = 15
    score_temp = 15
    font = pygame.font.SysFont('Bauhaus 93', 60)
    czy_w_powietrzu = True
    animation_timer = 0
    zycia = 3
    czy_damage = False

    while running:

        keys = pygame.key.get_pressed()



        #animacja misia
        if czy_kolizja is False:
            if animation_timer % 45 == 0:
                mis.animacja("mis111.png")
                animation_timer = 0
            elif animation_timer % 30 == 0:
                mis.animacja("mis333.png")
            elif animation_timer % 15 == 0:
                mis.animacja("mis222.png")




        #mis.update((100, 100))


        #screen.fill((0, 0, 0))
        screen.blit(tlo_tyl, (game_tlo_scroll, 0))
        game_tlo_scroll -= 1
        if abs(game_tlo_scroll) > 21590:
            game_tlo_scroll = 0

        screen.blit(tlo_ziemia, (game_ziemia_scroll, 0.28125 * game_ziemia_scroll))
        game_ziemia_scroll -= 2 * ziemia_speed
        if abs(game_ziemia_scroll) > 12800:
            game_ziemia_scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if obiekt.rect.y >= 600:
            czy_w_powietrzu = False


        if keys[pygame.K_w]:
            #obiekt.rect.y -= 1
            obiekt.przesun((0, -3))
        if keys[pygame.K_s] and czy_w_powietrzu is True and jumping is False and falling is False:
            # obiekt.rect.y += 1
            obiekt.przesun((0, 3))
        if keys[pygame.K_a]:
            # obiekt.rect.y -= 1
            # obiekt.rect.x -= 3
            obiekt.przesun((-6, -2))
        if keys[pygame.K_d]:
            # obiekt.rect.y += 1
            # obiekt.rect.x += 3
            obiekt.przesun((+6, +2))
        if keys[pygame.K_SPACE] and czy_w_powietrzu is False and falling is False:
            jumping = True



        #skakanie

        if jumping is True:
            obiekt.przesun((0, -20))
            jumping_timer += 1

        if jumping_timer == 20:
            jumping = False
            falling = True

        if falling is True:
            obiekt.przesun((0, 20))
            jumping_timer += 1

        if czy_w_powietrzu is False:
            falling = False
            jumping_timer = 0

            # warunek na powrót skrzynki

        if przeszkoda.rect.x < -SCREEN_WIDTH - pauza:
            pauza = przeszkoda.return_to_start((SCREEN_WIDTH - 100, SCREEN_HEIGHT - 600))
            przeszkoda.rect.x = SCREEN_WIDTH-100
            przeszkoda.rect.y = SCREEN_HEIGHT-600
        if animation_timer % 2 == 0:
            przeszkoda.rect.x -= 1

        # screen.fill(WHITE)
        pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        obiekt.rect = (500, 500)

        #obiekt.blitRotate((90, 162), pos)
        obiekt.update(pos)
        all_sprite_list.draw(screen)
        serca_list.draw(screen)
        pygame.display.flip()


        # sprawdza czy gracz dotyka przeszkody

        if mis.rect.colliderect(przeszkoda):
            czy_kolizja = True
            czas_kolizji = datetime.datetime.now()
            obiekt.kolizja_start("reka_czerwony.png")
            mis.kolizja_start("mis1_czerwony.png")
            przeszkoda.kolizja()
            # restart_screen.image.set_alpha(255)
            # game_over_text.image.set_alpha(255)
            # restart_text.image.set_alpha(255)
            # quit_text.image.set_alpha(255)

            # restart i wychodzenie z gry

            if mouse == (1, 0, 0) and 1030 < pos[0] < 1530 and 832 < pos[1] < 968:
                restart_screen.image.set_alpha(0)
                game_over_text.image.set_alpha(0)
                restart_text.image.set_alpha(0)
                quit_text.image.set_alpha(0)

            if mouse == (1, 0, 0) and 955 < pos[0] < 1605 and 1132 < pos[1] < 1268:
                run = False


        if czy_kolizja:


            if animation_timer % 45 == 0:
                mis.animacja("mis1_czerwony.png")
                animation_timer = 0
            elif animation_timer % 30 == 0:
                mis.animacja("mis3_czerwony.png")
            elif animation_timer % 15 == 0:
                mis.animacja("mis2_czerwony.png")

            czy_damage = True


            if czas_kolizji + CZAS_KOLIZJI < datetime.datetime.now():
                mis.kolizja_stop()
                zycia -= 1
                obiekt.kolizja_stop()
                czy_kolizja = False
                czy_damage = False


        if czy_damage:
            if zycia == 3:
                serce1.kolizja_start("serce_puste.png")
                czy_damage = False
                mis.rect.x = 700
                mis.rect.y = -700
                obiekt.rect.x = SCREEN_WIDTH / 2
                obiekt.rect.y = SCREEN_HEIGHT / 2
                timer_start = 0
                timer_end = 0
                obiekt.rect.x = mis.rect.x + REKAX
                mis.kolizja_stop()
                obiekt.kolizja_stop()
                czy_kolizja = False
                running = False
            elif zycia == 2:
                    serce2.kolizja_start("serce_puste.png")
                    czy_damage = False
            elif zycia == 4:
                    serce3.kolizja_start("serce_puste.png")
                    czy_damage = False



        przeszkoda.update(pos)

        #screen.blit(obiekt.rotated_image, obiekt.rotated_image_rect)

        #drawing score
        if score % 20 == 0:
            score_temp += 1

        wynik.updateText(str(score_temp))
        #draw_text(str(score_temp), font, WHITE, int(SCREEN_WIDTH / 2), 20)
        #draw_text(str(score / 5), font, (255, 255, 255), screen, 20, 20)



        #all_sprite_list.draw(screen)
        czy_w_powietrzu = True
        score += 1
        animation_timer += 1
        clock.tick(fps)
        pygame.display.update()



mainMenu()

pygame.quit()