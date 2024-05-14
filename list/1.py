# convert list to Tuple

# using the tuple method to convet the list into tuple
def convert(listdata:list) ->tuple:
    return tuple(listdata)


# using tuple comprehension
def convert1(listdata:list)-> tuple:
    return tuple(i for i in listdata)



def convert2(listdata:list) -> tuple:
    return ( *listdata, )


# def without using builtin function
def convert3(listdata : list)-> tuple:
    main_tuple =()
    for i in listdata:
        main_tuple += (i ,)
    return main_tuple


if __name__=="__main__":
    list1=[1,3,5,6]
    print(convert(list1))
    print(convert1(list1))
    print(convert2(list1))
    print(convert3(list1))
