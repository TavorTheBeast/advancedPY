class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name):
        self.name_ = name
        self.hunger_ = 0

    def get_name(self):
        return self.name_

    def is_hungry(self):
        return self.hunger_ > 0

    def feed(self):
        if self.hunger_ > 0:
            self.hunger_ -= 1

    def talk(self):
        print("Animal talk")


class Dog(Animal):
    def talk(self):
        print("Woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("Meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.stink_count_ = 6

    def talk(self):
        print("Tsssss")

    def stink(self):
        print("Dear Lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good morning, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.color_ = "Green"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = []

    dog = Dog("Brownie")
    zoo_lst.append(dog)

    cat = Cat("Zelda")
    zoo_lst.append(cat)

    skunk = Skunk("Stinky")
    zoo_lst.append(skunk)

    unicorn = Unicorn("Keith")
    zoo_lst.append(unicorn)

    dragon = Dragon("Lizzy")
    zoo_lst.append(dragon)

    for animal in zoo_lst:
        print(animal.get_name())
        animal.talk()

        while animal.is_hungry():
            animal.feed()

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

        print()

    doggo = Dog("Doggo")
    zoo_lst.append(doggo)

    kitty = Cat("Kitty")
    zoo_lst.append(kitty)

    stinky_jr = Skunk("Stinky Jr.")
    zoo_lst.append(stinky_jr)

    clair = Unicorn("Clair")
    zoo_lst.append(clair)

    mc_fly = Dragon("McFly")
    zoo_lst.append(mc_fly)

    for animal in zoo_lst:
        print(animal.get_name())
        animal.talk()

        while animal.is_hungry():
            animal.feed()

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

        print()

    print("Zoo name:", Animal.zoo_name)


if __name__ == "__main__":
    main()
