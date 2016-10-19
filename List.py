def main():
    number = int(input("Give me number: "))
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for element in a:
        if element<number:
            b.append(element)
    print(b)

if __name__ == "__main__": main()