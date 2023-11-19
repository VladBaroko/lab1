class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Human(Animal):
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Person(Human):
    def __init__(self, name, tax_number):
        super().__init__()
        self.name = name
        self.tax_number = tax_number

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r}, tax_number={self.tax_number!r})'


class Pet(Animal):
    def __init__(self, owner, name):
        super().__init__()
        self.owner = owner
        self.name = name

    def change_owner(self, new_owner):
        self.owner = new_owner

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(owner={self.owner!r}, name={self.name!r})'


class Enterprise:
    def __init__(self, name):
        self.name = name
        self.owned_pets = []

    def own_pet(self, pet):
        self.owned_pets.append(pet)

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r}, owned_pets={self.owned_pets!r})'


class Vaccine:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r}, manufacturer={self.manufacturer!r})'


class Chip:
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(code={self.code!r})'


class AnimalChip(Chip):
    pass


class Dog(Pet):
    def __init__(self, owner, name, chip):
        super().__init__(owner, name)
        self.chip = chip

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(owner={self.owner!r}, name={self.name!r}, chip={self.chip!r})'


# Приклад використання:

if __name__ == '__main__':
    person1 = Person("Alice", "T12345")
    person2 = Person("Bob", "T67890")

    enterprise = Enterprise("TechCorp")

    dog_chip = AnimalChip("123ABC")
    dog = Dog(person1, "Buddy", dog_chip)

    vaccine = Vaccine("COVID-19", "Pfizer")

    print(person1)
    print(person2)
    print(enterprise)

    enterprise.own_pet(dog)

    print(dog)
    print(vaccine)
