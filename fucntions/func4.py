def avg(li):
    result = 0
    for it in li:
        result+= it

    return result / len(li)

def multytable(num):
    
    for i in range(1, 11): 
        print(num, " x ", i, " = ", num * i)


mli = [10,20,30]
print(avg(mli))

multytable(int(input("enter number: ")))