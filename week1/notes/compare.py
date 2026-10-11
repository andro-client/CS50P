x = int(input("What's x? "))
y = int(input("What's y? "))

# boolean or true/false
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")

if x < y or x > y:
    print("x is not equal to y")

# same meaning but better structure
if x != y:
    print("x is not equal to y")
