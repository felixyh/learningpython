# 按要求编写描述符 Record：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件：record.txt
import time as t


class Record:
    def __init__(self, initval, name):
        self.log_file = '/Users/felix_yang/PycharmProjects/learningpython/46/record.txt'
        self.Value = initval
        self.name = name
        self.action = None
        self.atime = None

    def __get__(self, instance, owner):
        self.action = '读取'
        self.atime = t.strftime("%a %b %d %H:%M:%S %Y %z", t.gmtime())
        self.event = '{} 变量于北京时间 {} 被 {}, {}={}'.format(self.name,
                                                        self.atime,
                                                        self.action,
                                                        self.name,
                                                        self.Value
                                                        )
        self._logging(self.event)
        return self.Value

    def __set__(self, instance, value):
        self.Value = value
        self.action = '修改'
        self.atime = t.strftime("%a %b %d %H:%M:%S %Y %z", t.gmtime())
        self.event = '{} 变量于北京时间 {} 被 {}, {}={}'.format(self.name,
                                                        self.atime,
                                                        self.action,
                                                        self.name,
                                                        self.Value
                                                        )
        self._logging(self.event)

    def _logging(self, event):
        with open(self.log_file, 'a') as f:
            f.write(event)
            f.write('\n')


