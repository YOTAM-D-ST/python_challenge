def find_letter():
    count_f = 0
    count_b = 0
    before = False
    after = False
    special_ch = ''
    data =input("enter")#open("text_lvl3").read()
    for ch in data:
        if after and not ('A' <= ch <= 'Z'):
            print(special_ch, end="")
        if before:
            if 'A' <= ch <= 'Z':
                count_f = count_f + 1
                if count_f == 3:
                    after = True
            else:
                before = False
                count_f = 0
                special_ch = ""

        if 'a' <= ch <= 'z':
            if count_b == 3:
                before = True
                special_ch = ch
                count_b = 0

            else:
                count_b = 0
        if 'A' <= ch <= 'Z':
            count_b = count_b + 1


def main():
    find_letter()


if __name__ == '__main__':
    main()
