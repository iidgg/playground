# a cs50 watching the lecture while coding / 2023 week -6 python
def main():
    typo = getTypo()
    length = getLength()

    for i in range(length):
        if typo == "V":
            print("#")
        elif typo in ["H", "B"]:
            print("#" * length)

    print()


def getLength():
    while True:
        try:
            n = int(input("Length: "))
            if n > 0:
                return n
        except ValueError:
            print("bruh, i need a NUMBER!")


def getTypo():
    while True:
        try:
            t = input('Type? (Vertical "v"/Horizontal "h"/Both "b"): ').upper()

            if t in ["V", "H", "B"]:
                return t
        except:
            print("Something went wrong try again sweetie.")


main()
