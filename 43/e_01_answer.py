class A(object):
    count = 0

    def __init__(self):
        A.count += 1

    def getcount(self):
        return A.count


a = A()
a1 = A()
b = A()

print(a.getcount())
