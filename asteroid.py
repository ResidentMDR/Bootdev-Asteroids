from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Smallest asteroid nothing more to do
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        log_event("asteroid_split")

        # Compute settings for new asteroids
        random_angle = random.uniform(20, 50)
        first_new_asteroid_vector = self.velocity.rotate(random_angle)
        second_new_asteroid_vector = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        # spawn new asteroids
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

        # speed them up
        new_asteroid_1.velocity = first_new_asteroid_vector * 1.2
        new_asteroid_2.velocity = second_new_asteroid_vector * 1.2
