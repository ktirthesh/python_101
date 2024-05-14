# convet list to string using python

# convert by using loop
# tc o(1)
from crypt import methods


def convert(listdata: list) -> str:
    return_str = ""
    for i in listdata:
        return_str += str(i)
    return return_str


# using join method
def convert1(listdata: list) -> str:
    return "".join(listdata)


# using list comprehension
# tc - o(n)

def convert2(listdata: list) -> str:
    return " ".join([str(i) for i in listdata])

# using map method


def convert3(listdata: str) -> str:
    return " ".join(map(str, listdata))

# using enumurate function


def convert4(listdata: list) -> str:
    return " ".join([str(ele) for i, ele in enumerate(listdata)])

# using in operator


class ListtoString:
    def __init__(self) -> None:
        pass

    def convert(self, listdata: list) -> str:
        return ""


class UsingInOperator(ListtoString):
    def convert(self, listdata: list) -> None:
        for i in listdata:
            print(i, end=" ")

# using functool.reduce method
# tc -> o(n)


def convert5(listdata: list) -> str:
    from functools import reduce
    result = reduce(lambda a, b: a+" "+str(b), listdata)
    return result

# using format methods


def convert6(listdata: str) -> str:
    resultstr = "".join(["{}" for i in range(len(listdata))])
    return resultstr.format(*listdata)


# convert using recurssion
def convert7(start: int, listdata: list, word: str) -> str:
    if len(listdata) == start:
        return word
    word += listdata[start] + " "
    return convert7(start+1, listdata, word)


if __name__ == "__main__":
    list1 = ["fdf", "fdf", "tirthesh"]

    print(convert.__name__, convert(list1))
    print(convert1.__name__, convert1(list1))

    print(convert2.__name__, convert2(list1))
    print(convert3.__name__, convert3(list1))
    print(convert4.__name__, convert4(list1))
    print(convert5.__name__, convert5(list1))
    print(convert6.__name__, convert6(list1))
    print(convert7.__name__, convert7(0, list1, ""))

    obj1 = UsingInOperator()
    obj1.convert(list1)
