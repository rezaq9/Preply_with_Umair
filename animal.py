# there will be attirbute name, color and speak

class Animal:
    def __init__(self, name, color, speak):
        self.name = name
        self.color = color
        self.speak = speak

    def talk(self):
        return print(f'the {self.name} says {self.speak}')
    
    
class Birds(Animal):
    pass