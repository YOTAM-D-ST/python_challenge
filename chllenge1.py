def translate(str):
    new_str = ""
    for ch in str:
        if 'a' <= ch < 'y':
            ch = chr(ord(ch) + 2)
        elif ch == 'y':
            ch = 'a'
        elif ch == 'z':
            ch = 'b'
        new_str += ch
    print(new_str)


def main():
    translate(
        "http://www.pythonchallenge.com/pc/def/map.html")


if __name__ == '__main__':
    main()
