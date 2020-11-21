import pygame
import random
import math

from pygame.constants import WINDOWEVENT_HIT_TEST
from physics import Physics, distance_scale, time_scale, AU
from planet import Planet, Star
from vector import Vector

WIDTH = 1920
HEIGHT = 1080
planet_scale = distance_scale/10000


class Simulate(Physics):
    def __init__(self):
        super().__init__()

    def populate(self):
        self.addPlanet(Planet(6.9634e8, 1988500e24, 1.5*AU, 0.5*AU, 0, 0))
        self.addPlanet(Planet(6.371e6, 5.972e24, 0.5*AU, 0.5*AU, 0, 29780*time_scale, (0,100,255)))
        self.addPlanet(Planet(1.737e6, 7.348e22, 0.5*AU-384400000, 0.5*AU, 0, (29780*time_scale)+(1022*time_scale), (120, 120, 120)))
        self.addPlanet(Planet(3.389e6, 6.39e23, 0*AU, 0.5*AU, 0, 24070*time_scale, (255, 50, 50)))

    def draw(self, screen):
        offset = self.objects[0].pos/distance_scale - Vector(WIDTH/2, HEIGHT/2)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for planet in self.objects:
            print(tuple(((planet.pos)/distance_scale)-offset))
            pygame.draw.circle(screen, planet.color, tuple(((planet.pos)/distance_scale)-offset), max(math.log(planet.size/planet_scale), 1))
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    running = True
    clock = pygame.time.Clock()
    sim = Simulate()
    sim.populate()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        sim.draw(screen)
        sim.compute()
        print(sim)
        clock.tick(60)
    pygame.quit()
main()
