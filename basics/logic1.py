num_list = [10, 20, 30, 40, 50]
print(5 in num_list) # false
print(20 in num_list) #true

saarc = ["bangladesh", "afghanistan", "bhutan", "nepal", "india", "pakistan", "sri lanka"]
print("countries of saarc are: ", saarc); 

country = input("enter couontry you want to check: ")
if country in saarc: 
    print(country, "is a member of saarc")
else: 
    print(country, "is not a member of saarc")

print("program ended")