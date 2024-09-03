def main():
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        print(text)

        print(get_num_words(text))

        chars_dict = get_chars_dict(text)

        sorted_list = chars_dict_to_sorted_list(chars_dict)

        for char in sorted_list:
            print(char)


def get_num_words(text):
    return len(text.split())


def get_chars_dict(text):
    _dict = {}
    for letter in text.lower():
        if letter in _dict:
            _dict[letter] += 1
        else:
            _dict[letter] = 1
    return _dict


def chars_dict_to_sorted_list(dictionary):
    return [
        f"The '{x[0]}' character was found {x[1]} times"
        for x in sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
        if x[0].isalpha()
    ]


main()
