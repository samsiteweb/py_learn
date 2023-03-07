my_list = ['k', 'b', 'c']
my_sec_list = ['e', 'd']
print(my_list + my_sec_list)
add_list = my_list + my_sec_list
add_list.sort()
add_list.reverse()
# add_list.pop(2)
add_list.append("h")
add_list[2] = "great"
print(add_list)

a = my_list.pop()

print(a)