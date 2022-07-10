# my_list = ['house', 'car', 'bike', 'boat']
# for i in my_list:
#     print(i)
#     print('-------------')
#
# fruits = ['Orange', 'Apple', 'Banana']
# for j in fruits:
#     print(j)

quote = "Give a man a program,frustrate him for a day. Teac a man to program,frustrate him for a lifetime "
world = []
for i in quote.split():
    if len(i) <=3:
        world.append(i)
print(world)