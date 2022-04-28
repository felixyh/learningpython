list1 = [1, 23, 4, 'hello']

for each in list1:
    if isinstance(each, str):
        list1.remove(each)

print(list1, '\n', sum(list1))




