from pygame.event import Event


class Window:
    def __init__(self):
        self.screen_rects = []

    def key_updates(self, event: Event):
        raise NotImplementedError()

    def time_updates(self):
        raise NotImplementedError()

    def display(self):
        raise NotImplementedError()
