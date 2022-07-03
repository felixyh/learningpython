# 编写 Demo 类，使得下边代码可以正常执行

# >>> demo = Demo()
# >>> demo.x
# 'FishC'
# >>> demo.x = "X-man"
# >>> demo.x
# 'X-man'

class Demo:
    def __getattr__(self, name):
        self.name = 'FishC'
        return self.name


demo = Demo()
demo.x
demo.x = "X-man"
demo.x

