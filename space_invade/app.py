# welcome to the game of vilonce probably in space
# we start with importing the important modules for python to know what to do with the jibberish that follows

import pygame
import os
import time
import random
pygame.font.init()

# this below makes a window as per pygame's instructions

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space")

# images imported (pooly, idk how to do this correctly)
red_ship = pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/pixel_ship_red_small.png')
green_ship = pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/pixel_ship_green_small.png')
blue_ship = pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/pixel_ship_blue_small.png')
yellow_ship = pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/pixel_ship_yellow.png')

RED_Lazer = pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/pixel_laser_red.png')
GREEN_Lazer = pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/pixel_laser_green.png')
BLUE_Lazer = pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/pixel_laser_blue.png')
YELLOW_Lazer = pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/pixel_laser_yellow.png')

BG = pygame.transform.scale(pygame.image.load('/home/liam/Documents/Learn_Pyth-master/space_invade/assets/background-black.png'), (WIDTH, HEIGHT))

# classes first so things can be organised

class Ship:

    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
       # pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50, 50), 2) #this is a box lol
       window.blit(self.ship_img, (self.x, self.y))
       for laser in self.lasers:
           laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.laser.remove(laser)


    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1


    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(x, y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(x, y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health=100)
        self.ship_img = yellow_ship
        self.laser_img = YELLOW_Lazer
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Fighters(Ship):
    COLOR_dic = {
                "red": (red_ship, RED_Lazer),
                "green": (green_ship, GREEN_Lazer),
                "blue": (blue_ship, BLUE_Lazer)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.lasers = self.COLOR_dic[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return self.y <= height and self.y >= 0

    def collision(self, obj):
        return collide(obj, self)




# here comes the main funtions
#this one does the laser hits
# def collide (obj1, obj2):
#     offset_x = obj2.x - obj1.x
#     offset_y = obj2.y - obj1.y
#     return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

# here this one is the game parameters
def main():
    run = True
    FPS = 60
    level = 3
    lives = 2
    main_font = pygame.font.SysFont("Cantarell", 30)
    lost_font = pygame.font.SysFont("Cantarell Bold", 80)
    player_vel = 5
    lost = False
    lost_count = 0
    enemies = []
    wave = 5
    enemey_vel = 2
    player1 = Player(300, 650)


    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0)) #blit creates a "surface" with images at the specified coordinates
        lives_label = main_font.render(f'Lives: {lives}', 1, (255,255,255))
        level_label = main_font.render(f'Level: {level}', 1, (255,255,255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player1.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Fukin' Suq", 1, (255,255,255))
            WIN.blit(lost_label, (100, 350))


        pygame.display.update()


# lol without the following you cannot quit this
    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player1.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
        else:
            continue


        if len(enemies) == 0:
            level += 1
            wave += 5
            for i in range(wave):
                enemy = Fighters(random.randrange(25, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1.x -= player_vel
        if keys[pygame.K_RIGHT]:
            player1.x += player_vel
        if keys[pygame.K_DOWN]:
            player1.y += player_vel
        if keys[pygame.K_UP]:
            player1.y -= player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()


        for enemy in enemies[:]:
            enemy.move(enemey_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)








main()
