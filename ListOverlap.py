import random


def main():
    a = []
    b = []
    c = []
    for x in range(0, 15):
        a.append(random.randint(0, 30))
    for x in range(0, 12):
        b.append(random.randint(0, 30))
    for elem in a:
        if elem in b and elem not in c:
            c.append(elem)
    print(c)


if __name__ == "__main__": main()