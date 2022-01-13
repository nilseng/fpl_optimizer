from Person import Person

class Coach(Person):
    def __init__(self, name, age, team):
        super().__init__(name, age)
        self.team = team