# fibonacci 数列通过生成器来实现

def fiboGen(m):
    a, b = 0, 1
    while b < m:
        yield b
        a, b = b, a + b
    return 'done'


f = fiboGen(10)
for i in f:
    print(i)



