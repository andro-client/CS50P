def convert(string):
    new_string = string.replace(":(", "🙁").replace(":)", "🙂")
    return new_string

def main():
    print(convert(input()))

main()


