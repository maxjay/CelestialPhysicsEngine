class Planet:
    def __init__(self, size, mass, x, y, vx, vy, charge=0):
        self.size = size
        self.mass = mass
        self.x = x
        self.y = y
        self.vy = vx
        self.vy = vy
        self.charge = charge

class Star(Planet):
    def __init__(self, *args):
        super().__init__(self, *args)


if __name__ == "__main__":
    a = Planet(0,0,0,0,0,0)
    star = Star(0,0,0,0,0,0)