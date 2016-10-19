def main():
    while True:
        number = int(input("give me a number: "))
        x = range(1, number+1)
        b = []
        for elem in x:
            if number % elem == 0:
                b.append(elem)
        print("Divisors of "+str(number)+"are: "+str(b))
if __name__ == "__main__": main()