class C:
    @staticmethod   #该修饰符表示static()是静态方法
    def static (arg1 , arg2 , arg3 ) :
        print (arg1 , arg2 , arg3 , arg1 + arg2 + arg3)

    def nostatic (self) :
        print ("I'm the fucking normal method")


c1 = C()
c2 = C()


# 静态方法只在内存中生成一个，节省开销
print(c1.static is C.static)
print(c1.nostatic is C.nostatic)
print(c1.static)
print(c2.static)
print(C.static)


# 普通方法每个实例对象都有独立的一个，开销较大
print(c1.nostatic)
print(c2.nostatic)
print(C.nostatic)
