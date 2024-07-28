import random



def main():
    s = 10
    d = get_level()
    for _ in range(10):
        x = prob(d)
        s -= x
    print(s)








def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n <= 3:
                return n
            else:
                continue
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        integ = random.randint(0, 10)
    elif level == 2:
        integ = random.randint(10, 100)
    else:
        integ = random.randint(100, 1000)
    return integ

def prob(d):
    k = 0
    one = generate_integer(d)
    two = generate_integer(d)
    while k < 3:
        answer = input(f"{one} + {two} = ")
        if answer.isnumeric():
            answer = int(answer)
        else:
            k += 1
            print("EEE")
            continue
        if int(one) + int(two) == answer:
            return 0

        else:
            k += 1
            print("EEE")
            continue
    if k == 3:
        ans = int(one) + int(two)
        print(f"{one} + {two} = {ans}")
        return 1


if __name__ == "__main__":
    main()
