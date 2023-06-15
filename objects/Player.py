import pygame

import defs
from objects.Object import Object
from utils.Position import Position


class Player(Object):
    __max_speed = 3

    def __init__(self, position: Position, center: bool = False):
        self.size = defs.screen_width // 8
        image = pygame.image.load('sprites/player.png')
        self.moving_right = image.convert_alpha()
        image = pygame.transform.flip(image, True, False)
        self.moving_left = image.convert_alpha()
        player_rect = self.moving_left.get_rect()

        if center:
            # initialize in center
            player_rect.center = (defs.screen_width // 2, defs.screen_height // 2)
            position = Position(defs.screen_width // 2, defs.screen_height // 2)
        else:
            player_rect.center = (position.x, position.y)
        self.velocity_x = 0
        self.velocity_y = 0
        self.move_left = 0
        self.move_right = 0
        self.move_up = 0
        self.move_down = 0

        super().__init__(position=position,
                         surface=self.moving_right,
                         rect=player_rect,
                         update=True,
                         is_interactive=True)

    def handle_key(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.move_up = 1
            if event.key == pygame.K_s:
                self.move_down = 1
            if event.key == pygame.K_a:
                self.move_left = 1
            if event.key == pygame.K_d:
                self.move_right = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.move_up = 0
            if event.key == pygame.K_s:
                self.move_down = 0
            if event.key == pygame.K_a:
                self.move_left = 0
            if event.key == pygame.K_d:
                self.move_right = 0

    def time_update(self):
        keys_x = - self.move_left + self.move_right
        keys_y = - self.move_up + self.move_down

        if (keys_x == -1) and (abs(self.velocity_x) < self.__max_speed):
            self.velocity_x -= 0.4
        if (keys_x == 1) and (abs(self.velocity_x) < self.__max_speed):
            self.velocity_x += 0.4
        if keys_x == 0:
            if self.velocity_x > 0.4:
                self.velocity_x -= 0.4
            elif self.velocity_x < -0.4:
                self.velocity_x += 0.4

        if (keys_y == -1) and (abs(self.velocity_y) < self.__max_speed):
            self.velocity_y -= 0.4
        if (keys_y == 1) and (abs(self.velocity_y) < self.__max_speed):
            self.velocity_y += 0.4
        if keys_y == 0:
            if self.velocity_y > 0.4:
                self.velocity_y -= 0.4
            elif self.velocity_y < -0.4:
                self.velocity_y += 0.4

        if (-0.45 < self.velocity_y < 0.45) and (keys_y == 0):
            self.velocity_y = 0
        if (-0.45 < self.velocity_x < 0.45) and (keys_x == 0):
            self.velocity_x = 0
        new_position = Position(self.position.x + self.velocity_x, self.position.y + self.velocity_y)
        self.update_rect_new_position(new_position)
        self.update = True

    def get_surface(self):
        if self.move_right == 1:
            self.surface = self.moving_right
        if self.move_left == 1:
            self.surface = self.moving_left
        return self.surface
