#defines the asteroid class
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            init_angle = random.uniform(20, 50)
            asteroid1_vector = self.velocity.rotate(init_angle)
            asteroid2_vector = self.velocity.rotate(-init_angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid2 = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid1.velocity = asteroid1_vector * 1.2
            asteroid2.velocity = asteroid2_vector * 1.2


