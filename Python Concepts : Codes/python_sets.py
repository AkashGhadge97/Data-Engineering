#Sets in python
set1 = set()
print(type(set1))

lst1 = [1,1,2,3,4,4,5,5,6,7,8,9,9,8]
print(lst1)

print(set(lst1))


set2 = {1,1,2,3,4,5,6,76}
print(set2)

set3 = {7,8,9,9}

set2.update(set3)
print(set2)

#Set Operations
set_a = {1,2,3,4,5,6}
set_b = {3,6,8,9,10}
print("Unions of Set a and b : " , set_a | set_b)
print("Intersection of Set a and b : " , set_a & set_b)
print("Difference of Set a and b : " , set_a - set_b)
print("Difference of Set b and a : " , set_b - set_a)


#Set Comparions
set_x = {1,2,3,4,5}
set_y = {1,2,3,5,4,5,1}
print(set_x == set_y)

test_set = {5,1,2,6,7}
print(test_set)
