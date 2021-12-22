# Julio Claros
# 114153234
# 2018-13-11
# HW 6


class Robot:
    """
    Robot class that identifies a robot object under an optional name parameter,
    where base attributes of energy and compound set to 20 and None
    """

    def __init__(self, *name, **kwname):
        if name:
            self.name = str(name)
        elif kwname:
            self.name = str(kwname)
        else:
            self.name = None
        self.energy = 20
        self.compound = None

    def __add__(self, other):
        """
        Function takes two robot objects together and returns them as parameters
        for CompoundRobot function

        Return:
            self (object) Robot 1 as first parameter for CompoundRobot
            other (object) Robot 2 as second parameter for CompoundRobot
        """
        return CompoundRobot(self, other)


class CompoundRobot(Robot):
    """
    Class that joins two robot objects and appends both instances into a
    components list, adds energy levels, and updates compound attributes
    """

    def __init__(self, robot1, robot2):
        self.components = list()
        self.components.append(robot1)
        self.components.append(robot2)
        robot1.compound = self
        robot2.compound = self
        self.energy = robot1.energy + robot2.energy

    def __iadd__(self, other):
        """
        Function that takes an already compounded robot object and adds another
        instance of a robot object, adds energy levels, and updates robot
        compound attribute.

        Returns:
            self (object) instance of compounded robot
        """
        self.components.append(other.name)
        other.compound = self
        self.energy = self.energy + other.energy
        return self
