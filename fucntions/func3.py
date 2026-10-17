def add_numbers(numbers): 
    result = 0
    for number in numbers:
        result += number
    return result


result = add_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10])
print(result)

def changenum(li):
    li[0] = 10

mylist = [1, 2, 3,4,5]
changenum(mylist)
print(mylist)