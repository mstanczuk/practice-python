def main():
    word = input("Give me word: ")
    newWord = ""
    for c in word:
        newWord = c + newWord
    if word == newWord:
        print("given word is a palindrome!!")
    else:
        print("given word is not a palindrome")


if __name__ == "__main__": main()
