name = input("What's your name? ")

# in parameters for a definition you can
# set a default value with =
def hello(to="world"):
    print("hello,", to)

hello(name)
