import pygame
import random
import math

from pygame.constants import WINDOWEVENT_HIT_TEST
from physics import Physics, time_scale, time_subdiv, AU
from planet import Planet, Star
from vector import Vector

WIDTH = 1280
HEIGHT = 720
CENTER = Vector(WIDTH/2, HEIGHT/2)

distance_scale = AU/10000
planet_scale = distance_scale/10000


class Simulate(Physics):
    def __init__(self):
        super().__init__()
        self.tracking = 0
        self.last_tracking = 0
        self.tracking_progress = 0
        self.trail_offset = True

    def populate(self):
        self.addPlanet(Planet(7.149e7, 1.89819e27, -740.52e9, 0, 0, 13720*time_scale, (238, 178, 123))) # Jupiter

        self.addPlanet(Planet(6.2e3, 1.4762e15, -206.62e9-23463000, 0, 0, 26500*time_scale + 1351.3*time_scale, (120, 120, 120))) # Deimos
        self.addPlanet(Planet(11.27e3, 1.066e16, -206.62e9-9376000, 0, 0, 26500*time_scale + 2138*time_scale, (145, 128, 117))) # Phobos
        self.addPlanet(Planet(3.389e6, 6.39e23, -206.62e9, 0, 0, 26500*time_scale, (255, 50, 50))) # Mars

        self.addPlanet(Planet(1.737e6, 7.348e22, -147.09e9-384400000, 0, 0, (30290*time_scale)+(1022*time_scale), (120, 120, 120))) # Moon
        self.addPlanet(Planet(6.371e6, 5.972e24, -147.09e9, 0, 0, 30290*time_scale, (0,100,255))) # Earth

        self.addPlanet(Planet(6.052e6, 4.868e24, -107.48e9, 0, 0, 35260*time_scale, (240, 219, 202))) # Venus

        self.addPlanet(Planet(2.440e6, 3.3011e23, -46e9, 0, 0, 58980*time_scale, (146, 142, 143))) # Mercury

        self.addPlanet(Planet(6.9634e8, 1988500e24, 0, 0, 0, 0)) # Sun

        self.tracking = len(self.objects)-1
        self.last_tracking = self.tracking

    def toggle_trail_offset(self):
        self.trail_offset = not self.trail_offset

    def draw(self, screen):
        tracking = self.objects[self.tracking]
        offset_pos = tracking.pos
        if self.tracking != self.last_tracking:
            self.tracking_progress += 0.02
            if self.tracking_progress >= 1:
                self.tracking_progress = 0
                self.last_tracking = self.tracking
            else:
                offset_pos = self.objects[self.last_tracking].pos.lerp(offset_pos, math.sin(self.tracking_progress*math.pi/2))
        screen.fill((0, 0, 0))
        for planet in self.objects:
            #print(tuple(((planet.pos)/distance_scale)-offset))
            for i in range(len(planet.trail)-1):
                # trail_offset = [trail_tracking.trail[i], trail_tracking.trail[i+1]]
                pygame.draw.line(screen, tuple((j*(i/512) for j in planet.color)), tuple(self._offset_trail(planet, i, offset_pos)/distance_scale+CENTER), tuple(self._offset_trail(planet, i+1, offset_pos)/distance_scale+CENTER), 1)
            pygame.draw.circle(screen, planet.color, tuple(((planet.pos-offset_pos)/distance_scale)+CENTER), max(math.log(planet.size/planet_scale), 1))
        pygame.display.flip()

    def _offset_trail(self, planet, i, offset):
        if self.trail_offset:
            offset = self.objects[self.last_tracking].trail[i].lerp(self.objects[self.tracking].trail[i], math.sin(self.tracking_progress*math.pi/2))
        return planet.trail[i] - offset

def update_scales():
    global planet_scale
    planet_scale = distance_scale/10000

def main():
    global distance_scale, time_scale
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
            if event.type == pygame.MOUSEWHEEL:
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    if event.y > 0:
                        time_scale *= 1.5
                    else:
                        time_scale /= 1.5
                    sim.update_time_scale(time_scale)
                else:
                    if event.y > 0:
                        distance_scale *= 2
                    else:
                        distance_scale /= 2
                    update_scales()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB:
                    if event.mod & pygame.KMOD_CTRL:
                        if event.mod & pygame.KMOD_SHIFT:
                            sim.tracking = (sim.tracking + 1) % len(sim.objects)
                        else:
                            sim.tracking = (sim.tracking - 1) % len(sim.objects)
                    else:
                        sim.toggle_trail_offset()
        sim.draw(screen)
        for i in range(time_subdiv):
            sim.compute(i == time_subdiv-1)
        # print(sim)
        clock.tick(60)
    pygame.quit()
main()
