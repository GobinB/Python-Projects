if __name__ == '__main__':
    phrase = "Do you like green eggs and ham? \n I do not like them, Sam-I-Am. \n I do not like green eggs and ham."
    phrase = phrase.upper()
    print(phrase)
    characters = set(phrase)
    for c in characters:
        if c.isalpha():
            (print("Character to substitute for ", c, "?"))
            s = input()
            phrase = phrase.replace(c, s)
            print(phrase)
    print(phrase)
