

# this is a comment

class Animal:
    '''
    Describes a basic animal
    '''

    #__AnimalNoise = None

    def __init__(self, animalNoise):
        self.__AnimalNoise = animalNoise
        print("Animal created")

    @property
    def AnimalNoise(self):
        return self.__AnimalNoise

    @AnimalNoise.setter
    def AnimalNoise(self, value):
        self._AnimalNoise = value




