# remove forst element from list

# using pop method 
def popfirst(listdata:list)-> list:
    listdata.pop(0)
    return listdata

# using del list
def popfirst1(listdata:list) -> list:
    del listdata[0]
    return listdata

# using sliceing 
def popfirst2(listdata:list) -> list:
    return listdata[1:]
 
# using popleft dequeue
def popfirst3(listdata:list)->list:
    from collections import deque
    res = deque(listdata)
    print(res)
    res.popleft()
    return list(res)

# using remove method
def popfirst4(listdata:list)->list:
    listdata.remove(listdata[0])
    return listdata

# using list comprehension
def popfirst(listdata:list)->list:
    return [i for i in listdata[1:]]


if __name__ =="__main__":
    list_data =[1,3,5,6,7,8,8]
    print(popfirst.__name__,popfirst(list_data))
    print(popfirst1.__name__,popfirst1(list_data))
    print(popfirst2.__name__,popfirst2(list_data))
    print(popfirst3.__name__,popfirst3(list_data))
    print(popfirst4.__name__,popfirst4(list_data))