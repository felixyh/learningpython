# 再来一个有趣的案例：编写描述符 MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle
# （腌菜，还记得吗？）的文件中。如果属性被删除了，文件也会同时被删除，属性的名字也会被注销。
import os
import pickle


class MyDes:
    def __init__(self, name):
        self.attr_file = None
        self.name = name
        self.Value = None

    def __get__(self, instance, owner):
        return self.Value

    def __set__(self, instance, value):
        self.attr_file = '/Users/felix_yang/PycharmProjects/learningpython/46/ %s.pkl' % self.name
        self.Value = value
        self._storeattr(self.Value)

    def __delete__(self, instance):
        self.attr_file = '/Users/felix_yang/PycharmProjects/learningpython/46/ %s.pkl' % self.name
        os.remove(self.attr_file)
        del self

    def _storeattr(self, attr):
        with open(self.attr_file, 'wb') as pickle_file:
            pickle.dump(attr, pickle_file)
