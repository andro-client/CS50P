print("Hello world!")

name = input("What is your name? ")
print("Nice to meet you "+name)

# if you want to use "" inside a string, which already requires ""
# you have to switch either to ''
# or use \\
print("Hello 'friend'")
print("Hello \"friend\"")

# print format strings allow you to directly insert a variable inside quotes
print(f"Hello {name}")

# Using methods we can remove whitespaces from strings
# name = name.strip()

# Capitalize the name
# name = name.capitalize()

# Capitalize all the words
# name = name.title()

# You can chain period methods (name.strip().title())
name = name.strip().title()

# Split value into two different variables
aa, last = name.split(" ")
print(aa)

""" end="" makes it so print by default doesn't skip to the next line
 you can insert variables in a few different ways, with a + sign and with a ,
 inserting a variable with a , produces a blank space in print function
 because it automatically comes with a parameter sep=" " (separator) """
print("Nice to meet you", name, end=".", sep="...")