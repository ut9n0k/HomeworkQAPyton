from homework_12.beaver import Beaver
from homework_12.platypus import Platypus

if __name__ == '__main__':
    beaver = Beaver()
    platypus = Platypus()

    # polimorphism for fun
    print(beaver.make_noise())
    print(platypus.make_noise())

    # inheritance
    print(platypus.feeding)
