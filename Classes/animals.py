import pdb


class Animal:
    def __init__(self, color, food_type):
        print("I am init.")
        self.color = color
        self.food_type = food_type

    def move(self):
        print("Animal moves")

    def eat(self):
        print('Animal eat')
        print(f"This animal eats {self.food_type}")

    def breath(self):
        print("Animal breath")

    def main(self):
        self.move()
        self.eat()
        self.breath()


my_animal1 = Animal('blue', 'meat')
print(f"color of animal 1: {my_animal1.color}")
# my_animal1.move()
# my_animal1.eat()
my_animal1.main()

print('***********************')

my_animal2 = Animal('red', 'vag')
print(f"color of animal 2: {my_animal2.color}")
# my_animal2.eat()
my_animal2.main()
pdb.set_trace()
