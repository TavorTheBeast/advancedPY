class Octopus:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        self._age = 0
        Octopus.count_animals += 1

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


# Main program
octopus1 = Octopus("Oscar")
octopus2 = Octopus()

print("Name of octopus1:", octopus1.get_name())
print("Name of octopus2:", octopus2.get_name())

octopus1.set_name("Oliver")
print("New name of octopus1:", octopus1.get_name())

print("count_animals:", Octopus.count_animals)
