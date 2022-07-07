dict1 = {}
dict1[1] = 1
dict1['1'] = 2
dict1[1.0] = 3

result = 0
for each in dict1:
    print(dict1[each])
    result += dict1[each]

print(result)