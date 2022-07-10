#
# main_number = 15
# user_input = 0
# while user_input != main_number:
#     user_input = input("Guess a number 0 to 20:")
#     user_input = int(user_input)
#     print(f"You entered: {user_input}")
#     print(user_input != main_number)
# print("Done!!!")

#  Example 1
# main_number = 15
# while True:
#     user_input = input("Enter a number 0 to 20:")
#     print(f"You entered: {user_input}")
#     if int(user_input) == main_number:
#         break
# print("Done!!!")

# Example 2
# given a country print its capital city if it is in the given set of data, else print 'unknown
# capitals = {
#     "Peru": "Lima",
#     "Philippines": "Manila",
#     "Spain": "Madrid",
#     "Ethiopia": "Addis Ababa",
#     "Ghana": "Accra"
# }
#
# user_input = 'spain'
# for country, capital in capitals.items():
#     print("current country:" + country)
#     if user_input.lower() == country.lower():
#         print("Capital is:" + capital)
#         break


# Example 3
# given a dicionary whit book prices and list of courses, calculate total cost of books
book_prices = {"calculus": 300, "physics": 255, "chemistry": 400, "english": 150, "theater": 100}
my_courses = ["physics", "english", "psychology", "calculus", "history"]
# total_cost = 0
# for course in my_courses:
#     if course not in book_prices.keys():
#         continue
#     total_cost += book_prices[course]
#     total_cost = total_cost + book_prices[course]
# print(f"Total book cost {total_cost}")

