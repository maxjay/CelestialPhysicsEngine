from scipy import constants
from vector import Vector

G = constants.gravitational_constant
c = constants.speed_of_light

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
        return ((G*planetA.mass*planetB.mass)/d**2) * r

    def compute(self):
        for i in range(len(self.objects)):
            force = Vector(0,0)
            a = self.objects[i]
            for j in range(len(self.objects)):
                force += self.gravitationalForce(a, self.objects[j])
            a.pos += force

    def __str__(self):
        return str("\n".join([str(i) for i in self.objects]))

if __name__ == "__main__":
    from planet import Planet, Star
    a = Physics()
    a.addPlanet(Planet(1,1,1,1,0,0,0))
    a.addPlanet(Planet(1,1,3,3,0,0,0))
    print(a)
    a.compute()
    print(a)
