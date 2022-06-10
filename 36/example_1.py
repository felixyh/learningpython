class Turtle:  # python中的类名约定以大写字母开头； 函数名以小写字母开头
    """关于类的一个简单的例子"""
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法
    def climb(self):
        print('我正很努力的往前爬。。。')

    def run(self):
        print('我正飞快的向前跑。。。')

    def bite(self):
        print('咬死你，咬死你。。。')

    def eat(self):
        print('有的吃，真满足！')

    def sleep(self):
        print('困了，睡了，晚安。Zzzz')

#
# # 类的实例化
# turtle_01 = Turtle()
# turtle_01.sleep()
