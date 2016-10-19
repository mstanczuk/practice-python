def main():
    num = int(input("Give me first number: "))
    check = int(input("Give me number to divide by: "))
    if num%check==0:
        print("given number is evenly divided by "+str(check))
    else:
        print("given number is not evenly divided by "+str(check))

if __name__ == "__main__": main()