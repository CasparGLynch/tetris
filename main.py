import pygame.time

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                # screen event handling
                event = self.current_window.key_updates(event=event)
                if event is not None:
                    self.screen.fill(background_color)
                    self.current_window = GameWindow()
            # screen timing based updates
            self.current_window.time_updates()

            # loop to update all areas that require it in screen
            for element in self.current_window.display():
                rect = element.rect
                surface = element.surface
                self.screen.fill(background_color, rect)
                self.screen.blit(surface, (rect.x, rect.y))
                self.display.update(rect)

        else:
            print('Main game loop exited')


if __name__ == '__main__':
    Main().run()
