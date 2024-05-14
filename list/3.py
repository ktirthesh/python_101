# convert all string list into the integer list


# using eval function
def convert(listdata:list)->list:
    return [eval(i) for i in listdata]


# using int native method
def convert1(listdata:list)-> list:
    for index in range(0,len(listdata)):
        listdata[index] =int(listdata[index])
    return listdata

# using list conmprehsion 
def convert2(listdata:list)->list:
    return [int(i) for i in listdata]

# using map method
def convert3(listdata :list)-> list:
    return list(map(int,listdata))

# convert all int if the mixed data  type is present 
def convert4(listdata:list)->list:
    return [round(float(i)) for i in listdata]

# uding ast.literal_eval method
def convert5(listdata:list) -> list:
    import ast
    return [ast.literal_eval(i) for i in listdata]

def convert6(listdata :list)-> list:
    import json
    return json.loads('[' + ','.join(listdata) + ']')

if __name__ =="__main__":
    list1 =['1','4','3','5','6']
    list2 =['1.0','4.7','-3.9','5.2','6.3']
    print(convert.__name__,convert(list1))
    print(list1,)
    print(convert1.__name__,convert1(list1))   
    print(convert2.__name__,convert2(list1))   
    print(convert3.__name__,convert3(list1))   
    print(convert4.__name__,convert4(list1))   
    # print(convert5.__name__,convert5(list1))   
    print(convert6.__name__,convert6(list2))   
