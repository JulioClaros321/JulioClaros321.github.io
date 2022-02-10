class Robot:
    
    def __init__(self):
        self.energy = 20
        self.compound = None
    def charge(self, amount_of_energy):
        if self.compound is None:
            self.energy = self.energy + amount_of_energy
        else:
            raise RuntimeError
    def sustain_damage(self, amount_of_damage):
        if self.compound is None:
            self.energy = self.energy - amount_of_damage
        else:
            raise RuntimeError  
    def inflict_damage(self, robot):
        if self.compound is None:
            damage = self.energy * .2
            robot.sustain_damage(damage)
        else:
            raise RuntimeError

class CompoundRobot(Robot):
    def __init__(self, robot1, robot2):
        super().__init__()
        self.energy = 0
        self.components = []
        self.add_robot(robot1)
        self.add_robot(robot2)

    def add_robot(self, new_robot):
        self.energy += new_robot.energy
        self.components.append(new_robot)
        new_robot.energy = 0
        new_robot.compound = self

def main():
    bot1 = Robot()
    bot2 = Robot()
    Cbot = CompoundRobot(bot1, bot2)
    bot3 = Robot()
    bot3.inflict_damage(Cbot)
    Cbot.inflict_damage(bot3)
    print(Cbot.energy)
    print(bot3.energy)
            

if __name__ == '__main__':
    main()
        