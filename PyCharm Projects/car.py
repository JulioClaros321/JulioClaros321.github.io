""" Define a Car class. """

class Car:
    """ Models a car. Can drive forward and in reverse, turn left and
    right, consume gas, and refill its gas tank.
    
    Attributes:
        x (int): the car's x coordinate.
        y (int): the car's y coordinate.
        orient (str): the car's orientation ('n', 's', 'e', or 'w').
        gas (float): the amount of gas in the car's tank.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orient = 'n'
        self.gas = 10.0
    
    def drive(self, reverse=False):
        """ Drive forward or in reverse. Change position and consume gas.
        
        Args:
            reverse (bool): if True, drive in reverse.
            
        Side effects:
            Changes self.x, self.y, and self.gas.
        """
        if self.gas < 0.2:
            raise RuntimeError("Not enough gas to drive")
        adj_x = -1 if self.orient == 'w' else 1 if self.orient == 'e' else 0
        adj_y = -1 if self.orient == 'n' else 1 if self.orient == 's' else 0
        if reverse:
            adj_x *= -1
            adj_y *= -1
        self.x += adj_x
        self.y += adj_y
        self.gas -= 0.2
    
    def turn(self, dir):
        """ Turn left or right.
        
        Args:
            dir (str): 'l' for left or 'r' for right.
        
        Side effects:
            Changes self.orient.
        """
        directions = ['n', 'e', 's', 'w']
        current_dir_ix = directions.index(self.orient)
        adj = -1 if dir == 'l' else 1
        new_dir_ix = (current_dir_ix + adj) % len(directions)
        self.orient = directions[new_dir_ix]
        
    def refill(self):
        """ Refill the gas tank. """
        self.gas = 10.0
    
    def status(self):
        """ Print a status message. """
        orient_dict = {'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
        print(f"The car is at position ({self.x}, {self.y}).")
        print(f"The car is facing {orient_dict[self.orient]}.")
        print(f"There are {self.gas} units of gas in the tank.")


if __name__ == "__main__":
    c = Car()
    c.drive()
    c.turn('r')
    c.refill()
    c.status()
