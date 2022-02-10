class Robot:
    """ A class that simulates a robot"""
    
    def __init__(self):
        """ Sets an attribute energy to 20. This represents theamount of battery
        power a Robot object has. 
        Sets an attribute compound to None.This indicates that the Robot object 
        is not currently a component of a CompoundRobot object.
        """
        self.energy = 20
        self.compound = None
        
    def charge(self, amount):
        """ Determines the charge if the Robot if not a CompoundRobot

        Args:
        amount(int): an amount of energy

        Side Effects:
        Raises RunTimeError if Robot is a CompoundRobot
        """
        if self.compound is None:
            self.energy += amount
        else:
            raise RuntimeError
    
    def sustain_damage(self, amount):
        """ Reduces the object's energy attribute by amount if not a
        CoumpondRobot

        Args:
        amount(int): an amount of energy

        Side Effects:
        Raises RunTimeError if Robot is not a CompoundRobot
        """
        if self.compound is None:
            self.energy -= amount
        else:
            raise RuntimeError
    
    def inflict_damage(self, other):
        """ Calculates the amount of damage the Robot can do.

        Args:
        other: Another Robot object

        Side Effects:
        Raises RunTimeError if Robot is not a CompoundRobot
        """
        if self.compound is None:
            damage = self.energy * 0.2
            other.sustain_damage(damage)
        else:
            raise RuntimeError

class CompoundRobot(Robot):
    """ A child class of Robot, combines Robots into one
    """
    
    def __init__(self, robot1, robot2):
        """ Initializes the new CompoundRobot as a Robot. 
        Sets energy attribute to 0
        Creates an attribute called components and sets it equal to an empty 
        list.
        Calls its own add_robot() method twice: once for robot1 and again for 
        robot2

        Args:
        robot1(str):Robot objects that will be the first component of the new 
        CompoundRobot
        robot2(str):Robot objects that will be the second component of the new 
        CompoundRobot
    
        """
        super().__init__()
        self.energy = 0
        self.components = []
        self.add_robot(robot1)
        self.add_robot(robot2)
        
    def add_robot(self, robot):
        """ Increases energy attribute by the value of robot's energy attribute.
        Sets robot's energy attribute to 0 and its compound attribute to self. 

        Args:
        Robot(str)

        Side effects:
        appends robot to the components attribute

        """
        self.energy += robot.energy
        self.components.append(robot)
        robot.energy = 0
        robot.compound = self

def main():
    """ Instantiate three Robot objects and forms one CompoundRobot object. 
    Have the CompoundRobot fight another Robot 

    Side Effects:
    Print the energy of each of the two fighting Robot objects after each has
    inflicted damage on the other.
    """
    robot_1 = Robot()
    robot_2 = Robot()
    robot_3 = Robot()
    compound_robot = CompoundRobot(robot_1,robot_2)
    compound_robot.inflict_damage(robot_3)
    robot_3.inflict_damage(compound_robot)
    print(compound_robot.energy)
    print(robot_3.energy)

if __name__ == '__main__':
    main()