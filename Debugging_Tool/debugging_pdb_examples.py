import pdb

# demo 1
# print("I am the 1st line")
# fname = "natan"
# lname = "shete"
# pdb.set_trace()
# print("I am the 2st line")
# print("I am the 3st line")
# print(f"first name is '{fname}' and last name is '{lname}'")


# demo 2
def get_user_name(name):
    user_names = {"natan": "ak",
                  "joe": "joa99",
                  "mary": "marryrocks2020"}
    print(f'The user "{user_names[name]}" is logged in.')
    return user_names[name]

user_1 = get_user_name("natan")
print("User 1:" + user_1)
pdb.set_trace()

user_2 = get_user_name("joe")
print("User 2:" + user_2)
