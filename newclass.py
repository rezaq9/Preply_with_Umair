

class Countries:
    def __init__(country, name, capital, best_food):
        country.name = name
        country.capital = capital
        country.best_food = best_food

    def get_info(country):
        print(country.name, country.capital)

    def get_best_food(country):
        print(f"The name of country is {country.name} and its best food is {country.best_food}")

    def change_best_food(country, new_food):
        country.best_food = new_food
        print('the food is changed to ', country.best_food)



if __name__ == "__main__":
    c1 = Countries("USA", "Washington DC", "pizza")
    c1.get_best_food()

    c2 = Countries("India", "Delhi", "roganjosh")
    c2.get_best_food()
    c2.change_best_food("biryani")
    c2.get_best_food()

