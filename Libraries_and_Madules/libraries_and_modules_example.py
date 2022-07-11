import random

# example of 'random' module
# my_num = random.randint(100,200)
# print(my_num)

# my_num_ = random.randrange(30)
# print(my_num_)


# example of 'random' list
# my_list = ['aaa','bbb','ccc','ddd','eee']
# random.shuffle(my_list)
# print(my_list)

# pike won from the list
# my_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
# random.choice(my_list)
# print(my_list)


my_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
random.sample(my_list,3)
print(my_list)
