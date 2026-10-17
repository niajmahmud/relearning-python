bd_division_info = {}

bd_division_info["Barishal"] = {"district": 6, "upazila": 39, "union": 333}
bd_division_info["Dhaka"] = {"district": 13, "upazila": 93, "union":1833}
bd_division_info["Khulna"] = {"district": 10, "upazila": 59, "union":270}
bd_division_info["Mymensingh"] = {"district": 4, "upazila": 34, "union":350}
bd_division_info["Rajshahi"] = {"district": 8, "upazila": 70, "union":558}
bd_division_info["Rangpur"] = {"district": 8, "upazila": 58, "union":536}
bd_division_info["Sylhet"] = {"district": 4, "upazila": 38, "union": 334}

divisions = bd_division_info.keys()
print(divisions)
print(type(divisions))

for division in divisions: 
    print("Division ", division, " upazilla ", bd_division_info[division]["upazila"])

for item in bd_division_info:
    print(item)

for key in bd_division_info:
    print(key)
    print(bd_division_info[key])

for key, value in bd_division_info.items(): 
    print(key)
    print(value)

