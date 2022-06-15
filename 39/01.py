# 在类中定义一个变量，用来追踪有多少个实例被创建;
#
# 实例化一个对象，变量+1；销毁一个对象，变量-1

class InstanceCount:
    count = 0

    def __init__(self):
        InstanceCount.count += 1

    def __del__(self):
        InstanceCount.count -= 1


instance1 = InstanceCount()
print('目前共计有%d个实例被创建' % InstanceCount.count)
instance2 = InstanceCount()
print('目前共计有%d个实例被创建' % InstanceCount.count)
del instance1
print('目前共计有%d个实例被创建' % InstanceCount.count)
del instance2
print('目前共计有%d个实例被创建' % InstanceCount.count)
