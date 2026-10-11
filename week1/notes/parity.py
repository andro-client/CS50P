x = int(input("What's x? "))

if x % 2 != 0:
    print("number is odd")

else:
    print("number is even")


def main():
    n = int(input("What's n? "))
    if is_even(n):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    # return True if n % 2 == 0 else False
    return n % 2 == 0  # as the value is already a boolean


"""def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False"""

main()
