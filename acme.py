import random


class Product:
    """Class with default values and methods"""

    price = 10
    weight = 20
    flammability = 0.5
    identifier = random.randint(0, 10000000)

    def __init__(self, name):
        self.name = name

    def stealability(self):
        """Method to determine category threshold"""
        x = self.price / self.weight
        if x < 0.5:
            return "Not so stealable..."
        elif x >= 0.5 and x < 1:
            return "Kinda stealable."
        else:
            return "Very Stealable!"

    def explode(self):
        """Method to determine category threshold"""
        x = self.flammability * self.weight
        if x < 10:
            return "...fizzle"
        elif x >= 10 and x < 50:
            return "..boom!"
        else:
            return "..BABOOM"


class BoxingGlove(Product):
    """subClass inheriting form Product Class"""

    weight = 10

    def explode(self):
        """Override inherited method"""
        return "...it is a glove"

    def punch(self):
        """New method for subClass"""
        x = self.weight
        if x < 5:
            return "That tickes"
        if x >= 5 and x < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
