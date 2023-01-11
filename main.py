import pygame.time


class Main:
    """
    Main class that runs the main game loop
    """
    __frame_rate = 60

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.is_running = True

        # all the windows that the main loop will switch between
        # Todo: Add the classes
        self.windows = {'main_menu': None,
                        'game_window': None}

        # first window is main menu
        self.current_window = self.windows['main_menu']

        # pygame screen and display initialising
        self.screen = pygame.display.set_mode(size=(300, 600))
        self.display = pygame.display
        self.display.set_caption('Simple Tetris')

    def run(self):
        self.display.flip()
        while self.is_running:
            self.clock.tick(self.__frame_rate)
            # event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                # screen event handling
                self.current_window.key_updates()
            # screen timing based updates
            self.current_window.time_updates()

            # loop to update all areas that require it in screen
            for updatable_object in self.current_window.display():
                # Todo write actual update logic
                pass

        else:
            print('Main game loop exited')


if __name__ == '__main__':
    Main().run()
