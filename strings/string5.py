str = input("Enter string: ")
n = len(str)
str2 = ""

for i in range(n-1, -1, -1): 
    str2 = str2 + str[i]; 

print(str2)
if str == str2: 
    print("palyndrom")
else: print("not plndm")