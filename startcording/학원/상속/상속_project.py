class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        print("{} is born".format(self.name))
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    def __del__(self):
        Person.population -= 1
        print("{} is dead".format(self.name))


man = Person("jamse")
woman = Person("emily")
print("전체 인구수: {}명".format(Person.get_population()))
del man
print("전체 인구수: {}명".format(Person.get_population()))