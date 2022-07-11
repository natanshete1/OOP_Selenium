
# simple try-catch
# try:
#     a = 5 / 0
# except:
#     print("dont divide by 0")

# Exmple: catch specific exception
# try:
#     a = 5 / 0
# except ZeroDivisionError:
#     print("dont divide by 0")


# Exmple: print the actual error
# try:
#     a = 5 / 0
# except Exception as e:
#     print(f"Error has happened: {e}")

# Exmple: re-raise
try:
    a = 5 / 0
    print(foo)
except Exception as e:
    print("Sending notification")
    raise
