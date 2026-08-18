class robot:
    def __init__(self, robot, animal):
        self.robot = robot
        self.animal = animal

    def intro(self):
        return f"Hello! I am robot {self.robot}! I am a {self.animal}."

first_robot = robot("Tom", "cat")
second_robot = robot("Jerry", "mouse")

print(first_robot.intro())
print(second_robot.intro())