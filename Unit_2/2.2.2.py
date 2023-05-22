class Octopus:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


# Main program
octopus1 = Octopus("Octavio", 3)
octopus2 = Octopus("Octavia", 5)

octopus1.birthday()

print("Age of", octopus1.name, ":", octopus1.get_age())
print("Age of", octopus2.name, ":", octopus2.get_age())
