from .AnimalLibrary import Animal

class Dog(Animal):
    def __init__(self, name, tailWagNumber):
        self.__Name = name
        self.__tailWagginess = tailWagNumber

    @property
    def Name(self):
        return self.__Name

    @property
    def TailWagginess(self):
        return self.__tailWagginess

