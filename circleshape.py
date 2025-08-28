import pygame
import math

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


    def collision_check(self, circle_object):
            x_ab = (self.position.x - circle_object.position.x)**2
            y_ab = (self.position.y - circle_object.position.y)**2
            distance = math.sqrt(x_ab + y_ab)
            return distance < (self.radius + circle_object.radius)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass