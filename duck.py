class Duck:
    def __init__(breed, quack, colour):
        breed.quack = quack
        breed.colour = colour

    def get_info(breed):
        print(breed.quack, breed.colour)

    def __str__(breed):
        return f'This is a DUCK class with info {breed.quack}'