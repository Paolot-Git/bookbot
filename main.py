def main():
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        print(text)

        words = text.split()
        print(len(words))

        _dict = {}
        text_lower = text.lower()
        for letter in text_lower:
            if letter in _dict:
                _dict[letter] += 1
            else:
                _dict[letter] = 1
        _list = [
            f"The '{x[0]}' character was found {x[1]} times"
            for x in _dict.items()
            if x[0].isalpha()
        ]
        print(_list)


main()


def sort_on(dict):
    return dict["num"]
