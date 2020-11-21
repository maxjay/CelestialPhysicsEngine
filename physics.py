from scipy import constants
from vector import Vector

AU = 1.496e11

c = constants.speed_of_light
G = constants.gravitational_constant
time_subdiv = 50
time_scale = 21600/time_subdiv
#G = (6.674e-11 * time_scale**2) / distance_scale**3

class Physics:
    def __init__(self):
        self.objects = []

    def addPlanet(self, planet):
        self.objects.append(planet)

    @staticmethod
    def gravitationalForce(planetA, planetB):
        r = planetA.pos - planetB.pos
        d = abs(r)
        if d == 0:
            return Vector()
        return ((G*planetA.mass*planetB.mass)/d**2) * (r/d)

    def compute(self, update_trail=False):
        for i in range(len(self.objects)):
            force = Vector(0,0)
            a = self.objects[i]
            for j in range(len(self.objects)):
                force -= self.gravitationalForce(a, self.objects[j])
            #force = (force / distance_scale) * time_scale**2
            force = force * time_scale**2
            a.speed += force/a.mass
        for a in self.objects:
            a.pos += a.speed
            if update_trail:
                if len(a.trail) > 512:
                    a.trail = a.trail[1:]
                a.trail.append(a.pos.copy())

    def __str__(self):
        return str("\n".join([str(i) for i in self.objects]))

if __name__ == "__main__":
    from planet import Planet, Star
    a = Physics()
    a.addPlanet(Planet(10, 1988500e24, 2.992e11, 2.992e11, 0, 0))
    a.addPlanet(Planet(1, 6e24, 1.496e11, 2.992e11, 0, 29780*time_scale))
    print(a)
    for i in range(3):
        a.compute()
        print(a)
