# Exmple: Function to add two number
# def my_adder(a,b):
#     total = a + b
#     return total
# my_total = my_adder(4,15)
# print(my_total)

# Exmple: Function to determine if given state has no sales tax
def has_no_seles_tax(state):

    state_with_no_sales_tax = ['AK', 'DE', 'MT', 'MH', 'OR']

    if state.upper() in state_with_no_sales_tax:
        return True
    else:
        return False

user_state = "DE"
tax = has_no_seles_tax(user_state)
print(tax)
