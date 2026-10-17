str = input("enter a string: "); 
str1 = ""
str2 = ""
str3 = ""
str4 = ""
for c in str:
    if c >= 'A' and c <= 'Z': 
        str1 = str1 + c; 
print(str1)

for c in str:
    if c>= 'a' and c <= 'z': 
        str2 = str2 + c; 
print(str2)

for c in str: 
    if c >= '1' and c <='9':
        str3 = str3 + c; 
print(str3)

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
for c in str: 
    if c not in s and c not in s.lower(): 
        str4 = str4 + c; 
print(str4)