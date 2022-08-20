import urllib.request


def main():
    link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
    nothing = ""
    count_place_in_str = 0
    count = 0
    digit_in = False
    for i in range(400):
        print(count)
        count = count + 1
        with urllib.request.urlopen(link) as response:
            html = str(response.read())
            print(html)
        # checks if a number appear in the text
        digit_in = False
        for ch in html:
            if ch.isdigit():
                digit_in = True
            # when two numbers of nothings appears
        if html.count("nothing") > 1:
            nothing = html[html.rfind("is ") + 3:-1]
            # when no numbers appears
        if not digit_in:
            nothing = str(int(nothing) // 2)
        else:
            for ch in html:
                if ch.isdigit():
                    nothing = html[count_place_in_str:-1]
                    count_place_in_str = 0
                    break
                count_place_in_str = count_place_in_str + 1
                # make the link
        link = link[:link.find('=') + 1] + nothing
        print(link)


if __name__ == '__main__':
    main()
