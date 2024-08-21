class Cat:
    def __init__(cat, name, colour, behaviour,status):
        cat.name = name
        cat.colour = colour
        cat.behaviour = behaviour
        cat.status = status

    def see_behaviour(cat):
        print('cat is {}'.format(cat.behaviour))

    def change_behaviour(cat, new_behaviour):
        cat.behaviour = new_behaviour
        print('the behaviour is changed to {}'.format(cat.behaviour))

    def what_cat_doing(cat):
        print('{} is {}'.format(cat.name,cat.status))

    def change_status(cat, new_status):
        cat.status = new_status

    
if __name__ == "__main__":

    c1 = Cat('kitty', 'black', 'friendly','sleeping')
    c1.see_behaviour()
    c1.change_behaviour('aggressive')
    c1.see_behaviour()

    c1.what_cat_doing()


    c2 = Cat('sora', 'black', 'friendly','running')
    c2.what_cat_doing()
    c2.change_status('sleeping')
    c2.what_cat_doing()


    hello = Cat('hello', 'black', 'friendly','eating')
    hello.what_cat_doing()

