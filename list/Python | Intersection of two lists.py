# find intersection of list in python
def intersection_by_list(list1, list2):
    return [value for value in list1 if value in list2]

# convert into set and return the list of & operation
def intersection_using_set(list1, list2):
    return list(set(list1) & set(list2))

# convert into the set and return thelist of intersection of both
def set_intersection_function(list1,list2):
    return list(set(list1).intersection(set(list2)))


def filter_and_lambda(list1,list2):
    return [list(filter(lambda x: x in list1,value)) for value in list2]

def reducer_and_lambda(list1,list2):
    from functools import reduce
    return reduce(lambda acc,x : acc +[x]if x in list2 and x  not in acc else acc,list1,[])

def main():
    example1 = [1, 4, 2, 4, 32, 2, 10]
    example2 = [3, 4, 5, 6, 71, 1]
    # using the list comprehension
    print(intersection_by_list(example1, example2))

    # using the set and & operator
    print(intersection_using_set(example1, example2))

    #using set intersection method
    print(set_intersection_function(example1,example2))

    example3 = [1,2,4,2,4,2]
    example4 = [[4,2,4,2,33,55,66,88],[11,33,5,6,8,2],[12,4,5,6,8,1]]

    # using filter and lambda function
    print(filter_and_lambda(example3,example4))

    # using reducer and lambda
    print(print(reducer_and_lambda(example1,example2)))

if __name__ == "__main__":
    main()
