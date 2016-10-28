import pygame

class Scene:
    def __init__(self, engine):
        self.x = 0
        self.y = 0

        self.engine = engine
        self.sprites = pygame.sprite.LayeredDirty(())
        self.ending = False

        self.scene_lifetime = 0

    def start(self):
        """
        Called when scene is started.
        :return: None
        """
        pass

    def end(self):
        """
        Set this scene to ending.
        :return: None
        """
        self.ending = True

    def do_tick(self, time_passed):
        """
        Choose whether to call tick or tick_end.
        Advances engine to next scene if tick_end finishes.
        :param time_passed: Time passed in ms since last tick
        :return: None
        """
        self.scene_lifetime += time_passed
        if self.ending:
            end_status = self.tick_end(time_passed)
            if end_status:
                self.engine.next_scene()
        else:
            self.tick(time_passed)

    def tick(self, time_passed):
        """
        Tick method while scene is alive.
        :param time_passed: Time passed in ms
        :return: None
        """
        pass

    def tick_end(self, time_passed):
        """
        Called when scene is ending.
        Allows for transitions out of scene.
        :param time_passed: Time passed in ms
        :return: None
        """
        return True

    def add(self, sprite):
        """
        Add a sprite to this scene.
        :param sprite: Sprite to add
        :return: None
        """
        self.sprites.add(sprite)

    def remove(self, sprite):
        """
        Remove a sprite from this scene.
        :param sprite: Sprite to remove
        :return: None
        """
        self.sprites.remove(sprite)

    def draw(self, surface):
        """
        Draw this scene's sprite to the given surface.
        :param surface: Surface to draw to
        :return: None
        """
        self.sprites.draw(surface)

    def key_press(self, key, unicode):
        """
        Handle key presses sent to this scene.
        :param key: Key code
        :param unicode: Unicode value of key
        :return: None
        """
        pass

    def get_scene(self):
        """
        Required as scene is parent to sprites.
        :return: self
        """
        return self

    def is_showing(self):
        """
        Required as scene is parent to sprites.
        :return: True
        """
        return True