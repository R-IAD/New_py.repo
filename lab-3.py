mylist = ["riad", "nageh", "wadee"]


def capFirst(s):
    result = ""
    listd = s.split()
    for i in listd:
        i = i.capitalize()
        result += i + " "
    return result


mylist = "riad nageh wadee"
print(capFirst(mylist))
