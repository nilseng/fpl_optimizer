from Person import Person

class Player(Person):
    def __init__(self, name, age, weight):
        Person.__init__(self, name, age)
        self.weight = weight
