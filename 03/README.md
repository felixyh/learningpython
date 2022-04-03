# lesson
------


## 变量
在使用变量之前，需要对其赋值
变量的命名理论上可以取任何合法的名字，但座位一个优秀的程序员，请尽量给变量一个专业的名字

## 插曲之字符串

到目前为止，我们所认知的字符串就是引号内的任何东西。我们把字符串叫做文本，文本和数字是截然不同的

如果字符串中需要出现单引号或者双引号怎么办？

有两种办法：
- 第一种使用我们的转义符号（\）
- 第二种？

## 原始字符串

原始字符串的使用非常简单，在字符串前面追加一个r
```python
str = r'C:\now'
```

## 长字符串
三重引号字符串
```python
str = """五岭逶迤腾细浪
乌蒙磅礴走泥路
金沙排水云崖暖
大渡桥横铁索寒
"""
```

# Practice
## Quiz
0. 以下哪个变量的命名不正确？为什么？

    (A) MM_520  (B) _MM520_  (C) 520_MM  (D) _520_MM

Answer：C

1. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？
```python
>>>myteacher = '小甲鱼'
>>>yourteacher = myteacher
>>>yourteacher = '黑夜'
>>>print(myteacher)
```

Answer: 小甲鱼


2. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？
```
>>> myteacher = '小甲鱼'
>>> yourteacher = myteacher
>>> myteacher = '黑夜'
>>> print(yourteacher)
```


Answer: 小甲鱼

3. 在不上机的情况下，以下代码你能猜到屏幕会打印什么内容吗？
```python
>>>first = 520
>>>second = '520'
>>>first = second
>>>print(first)
```

Answer: 520



4. 除了使用反斜杠（\）进行字符转义，还有什么方法可以打印：Let's go! 这个字符串？

Answer:
```python
>>> str = "Let's go!"
>>> str
"Let's go!"
>>> print(str)
Let's go!
```

5. 如果非要在原始字符串结尾输入反斜杠，可以如何灵活处理？

Answer:
```python
>>> str = r'C:\now' + '\\'
>>> str
'C:\\now\\'
>>> print(str)
C:\now\
```

6. 在这一讲中，我们说变量的命名需要注意一些地方，但小甲鱼在举例的时候貌似却干了点儿“失误”的事儿，你能看得出小甲鱼例子中哪里有问题吗？

Answer: 在例子中小甲鱼起了个 str 名字的变量，但事实上我们发现，str 的颜色跟普通变量貌似不同？没错，str() 和 print() 都是内置函数，但 Python 貌似不介意我们对内置函数进行赋值操作，所以这点我们以后就要注意啦，否则可能会出现以下的 BUG

## Practice：

0. 还记得我们第一讲的动动手的题目吗？这一次要求使用变量，计算一年有多少秒？

提示：可以以 DaysPerYear（每年天数），HoursPerDay（每天小时数），MinutesPerHour（每小时分钟数），SecondsPerMinute（每分钟秒数）为变量名。

Answer: 

```python
>>> DaysPerYear = 365
>>> HoursPerDay = 24
>>> MinutesPerHour = 60
>>> SecondsPerMinute = 60
>>> SecondsPerYear = DaysPerYear * HoursPerDay * MinutesPerHour * SecondsPerMinute
>>> SecondsPerYear
31536000

>>> print(SecondsPerYear)
31536000
```

1. 关于最后提到的长字符串（三重引号字符串）其实在 Python3 还可以这么写，不妨试试，然后比较下哪种更方便？

```python
>>> string = (
"我爱鱼C，\n"
"正如我爱小甲鱼，\n"
"他那呱唧呱唧的声音，\n"
"总缠绕于我的脑海，\n"
"久久不肯散去……\n")
```

Answer:  三重引号字符串


2. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

Answer: 
a. 学习了变量，以及变量的使用和命名
b. 学习了字符串，转义字符串，原始字符串，长字符串

