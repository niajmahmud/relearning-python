bd_division_info = {}

bd_division_info["Barishal"] = {"district": 6, "upazila": 39, "union": 333}
bd_division_info["Chittagong"] = {"district": 11, "upazila": 97, "union":336}
bd_division_info["Dhaka"] = {"district": 13, "upazila": 93, "union":1833}
bd_division_info["Khulna"] = {"district": 10, "upazila": 59, "union":270}
bd_division_info["Mymensingh"] = {"district": 4, "upazila": 34, "union":350}
bd_division_info["Rajshahi"] = {"district": 8, "upazila": 70, "union":558}
bd_division_info["Rangpur"] = {"district": 8, "upazila": 58, "union":536}
bd_division_info["Sylhet"] = {"district": 4, "upazila": 38, "union": 334}

zila = 0
upazila = 0
union = 0


for key in bd_division_info:
    zila = zila + bd_division_info[key]["district"]
    upazila = upazila  + bd_division_info[key]["upazila"]
    union = union + bd_division_info[key]["union"]

print("total zilla: ", zila, "toal upazila: ", upazila," toal union ", union)