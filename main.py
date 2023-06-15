import pygame.time

import defs
from defs import background_color, screen_width, screen_height
from windows.GameWindow import GameWindow
from windows.MainMenuWindow import MainMenuWindow


class Main:
    """
    Main class that runs the main game loop
    """
    __frame_rate = 60

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.is_running = True

        # first window is main menu
        self.current_window = MainMenuWindow()

        # pygame screen and display initialising
        self.screen = pygame.display.set_mode(size=(screen_width, screen_height))
        self.display = pygame.display
        self.display.set_caption('Simple Tetris')

    def run(self):
        self.screen.fill(background_color)
        self.display.flip()
        while self.is_running:
            self.clock.tick(self.__frame_rate)
            # event handling
            for pygame_event in pygame.event.get():
                if pygame_event.type == pygame.QUIT:
                    self.is_running = False
                # screen event handling
                event = self.current_window.key_updates(event=pygame_event)
                if event:
                    self.handle_event(event)

            # screen timing based updates
            self.current_window.time_updates()

            # loop to update all areas that require it in screen
            for element in self.current_window.display():
                rect = element.rect
                surface = element.surface
                rect_to_update = element.get_rect_to_updated()
                self.screen.fill(background_color, rect_to_update)
                self.screen.blit(surface, (rect.x, rect.y))
                self.display.update(rect_to_update)

        else:
            print('Main game loop exited')

    def handle_event(self, event_code):
        match event_code:
            case defs.SWITCH_TO_GAME:
                self.current_window = GameWindow()
                self.screen.fill(defs.background_color)
                self.display.flip()
            case _:
                return


if __name__ == '__main__':
    Main().run()
