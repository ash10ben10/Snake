import pygame, sys

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Labyrinth Escape')
screen = pygame.display.set_mode([800, 600])

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.image.fill((0, 255,0))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
                
class Wall(pygame.sprite.Sprite):   

    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Room(object):
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

class Room1(Room):
    def __init__(self):
        Room.__init__(self)
        walls = [[0, 0, 20, 250, (255, 255, 255)],
                 [0, 350, 20, 250, (255, 255, 255)],
                 [780, 0, 20, 250, (255, 255, 255)],
                 [780, 350, 20, 250, (255, 255, 255)],
                 [20, 0, 760, 20, (255, 255, 255)],
                 [20, 580, 760, 20, (255, 255, 255)],
                 [0, 250, 20, 280, (255, 255, 255)],
                 [90, 20, 20, 70, (0, 0, 255)],
                 [90, 120, 20, 70, (0, 0, 255)],
                 [190, 70, 80, 20, (0, 0, 255)],
                 [200, 190, 80, 20, (0, 0, 255)],
                 [390, 20, 20, 400, (0, 0, 255)],
                 [490, 50, 20, 550, (0, 0, 255)],
                 [310, 50, 20, 530, (0, 0, 255)],


                 ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

def main():
    player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
                    
        player.move(current_room.wall_list)

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        screen.fill((0,0,0))

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
