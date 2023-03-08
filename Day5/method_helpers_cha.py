string = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#".lstrip(',:%,_,#')

print(string)

# Add the element "orange" as the fourth element of the following list


fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

fruits.insert(3, 'orange')

print(fruits)

# Check if the sets below are isolated (that is, they have no elements in common)

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

res = phone_brands.isdisjoint(tv_brands)

print(res)