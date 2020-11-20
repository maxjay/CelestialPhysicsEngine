from vector import Vector

class Planet:
    def __init__(self, size, mass, x=0, y=0, vx=0, vy=0, charge=0):
        self.size = size
        self.mass = mass
        self.pos = Vector(x, y)
        self.speed = Vector(vx, vy)
        self.charge = charge

    def __str__(self):
        return f'[Size: {self.size}, Mass: {self.mass}, Pos: {self.pos}, Speed: {self.speed}, Charge: {self.charge}]'

class Star(Planet):
    def __init__(self, *args):
        super().__init__(self, *args)

if __name__ == "__main__":
    a = Planet(0,0,0,0,0,0)
    star = Star(0,0,0,0,0,0)