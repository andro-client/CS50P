x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

a = float(input("What's a? "))
b = float(input("What's b? "))

z = round(a + b)
c = round(a / b, 2)
print(f"{z:,}")
print(f"{c:,}")

# just like in java you can use in an f string
# .2f or similar after :
print(f"{c:.2f}")

def area(width, length):
    print(f"Area es = {length*width:.2f}")

area(10.5,10.5)

