from random import randint

class Die:

    def __init__(self):
        self.sides = 6
        
    def roll_die(self):
        for roll in range(10):
            result = randint(1, self.sides)
            print(result)
            
roll = Die()
roll.roll_die()