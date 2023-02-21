def add(a, b):
    return a + b


def swap_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += (ch).capitalize()
        else:
            result += ch.lower()
    return result


def main():
    mylist = "Riad Nageh Wadee"

    print(swap_case(mylist))


# ------------------------------------

if __name__ == "__main__":
    main()
