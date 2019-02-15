import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=None):
        if identifier is None:
          identifier = random.randint(1000000, 10000000)
        assert type(name) == str
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        s = self.price / self.weight
        if s < .5:
            return 'Not so stealable'
        elif s < 1:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        x = self.flammability * self.weight
        if x < 10:
            return '...fizzle'
        elif x < 50:
            return '...boom!'
        else:
            return '...BABOOM!'


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=None):
        if identifier is None:
          identifier = random.randint(1000000, 10000000)
        assert type(name) == str
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def punch(self):
        if self.weight < 5:
            return 'that tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'

    def explode(self):
        return "...it's a glove."

