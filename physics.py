from scipy import constants

G = constants.gravitational_constant
c = constants.speed_of_light

class Physics:
    def __init__(self):
        self.objects = []

    def addPlanet(self, planet):
        self.objects.append(planet)

    @staticmethod
    def componentForce(resultantForce):
        return 1,1

    @staticmethod
    def gravitationalForce(planetA, planetB):
        return 1

    def updatePos(self, resultForce, planet):
        planet.vx, planet.vy = Physics.componentForce(resultForce)

    def applyForces(self, forces):
        for force, planet in zip(forces, self.objects):
            self.updatePos(force, planet)

    def compute(self):
        forces = [0 for i in xrange(len(self.objects))]
        for i in xrange(len(self.objects)):
            a = self.objects[i]
            for j in xrange(i+1, len(self.objects)):
                forces[i] += self.gravitationalForce(a, self.objects[j])
        self.applyForces(forces)

