class Particle(object):
    """A particle is a constituent unit of the universe.
    Attributes
    ----------
    c : charge in units of [e]
    m : mass in units of [kg]
    r : position in units of [meters]
    """
    roar = "I am a particle!"
    def __init__(self, charge, mass, position):
        """Initializes the particle with default values for
        charge c, mass m, and position r.
        """
        self.c = charge
        self.m = mass
        self.r = position
    
    def hear_me(self):
        myroar = self.roar + (
        " My charge is: " + str(self.c) +
        " My mass is: " + str(self.m) +
        " My x position is: " + str(self.r['x']) +
        " My y position is: " + str(self.r['y']) +
        " My z position is: " + str(self.r['z']))
        print(myroar)