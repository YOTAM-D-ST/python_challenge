def count_letters(str):
    dct = {}
    data = open("text_lvl2").read()
    for ch in data:
        if ch in dct:
            dct[ch] = dct[ch]+1
        else:
            dct[ch] = 1
    print(dct)


def main():
    count_letters(input("enter"))


if __name__ == '__main__':
    main()
