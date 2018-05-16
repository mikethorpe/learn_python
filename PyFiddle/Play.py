from libraries.AnimalLibrary import Animal
from libraries.DogLibrary import Dog

def PrintAnimalNoise(animal):

    print(animal.AnimalNoise)

brian = Animal("moo!")

PrintAnimalNoise(brian)

brian.AnimalNoise = "growl"

PrintAnimalNoise(brian)

steve = Dog("Steve", 1)



