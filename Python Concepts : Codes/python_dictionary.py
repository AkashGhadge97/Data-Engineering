#Dictionary in Python
dict1 = {}
print(type(dict1))

#Insert value in dictionary
dict2 = {}
dict2['name'] = 'Akash'
dict2['age'] = 25
dict2['skills'] = ['Python','Java']
dict2['States_Visited'] = ('KA','HM')
dict2[45] = 'Random Key'
dict2['Grades'] = {'Sem1' : 9.87, 'sem2' : 9.88}
print(dict2)

#How to access the value of a particular key
print(dict2['name'])

#Length of dictionary
print(len(dict2))

print(dict2['skills'][1])

print(dict2['Grades']['Sem1'])

total_keys = dict2.keys()
print(total_keys)

total_values = dict2.values()
print(total_values)

# How to iterate over dictionary
for key,value in dict2.items():
    print(key,value)

#Compare Dictionary
dict3 = {'a' : 1 , 'b' : 2, 'c' : 3}
dict4 = {'c' : 3 , 'b' : 2, 'a' : 1}

print(dict3 == dict4)

#How to to delete specific key,value pair from dictionary
del(dict3['a'])
print(dict3)

#How to check if particular key is present in dictionary or not
result = dict2.keys().has_key('name')
print(result)