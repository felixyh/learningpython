[TOC]

----

# 000. 愉快的开始



# 001. 我和Python的第一次亲密接触



# 002. 用Python设计第一个游戏



# 003. 小插曲之变量和字符串



# 004. 改进我们的小游戏



# 005. 闲聊之Python的数据类型

## 知识点

### 数据类型

Python的一些数值类型： 整型，布尔类型，浮点型， e记法

```
>>> type(5)
<class 'int'>
>>> 
>>> type(True)
<class 'bool'>
>>> 
>>> type(False)
<class 'bool'>
>>> 
>>> True + False
1
>>> type(True+False)
<class 'int'>
>>> 
>>> 0.0000000001
1e-10
>>> 
>>> 1.5e10
15000000000.0
>>> 
>>> type(1.5e10)
<class 'float'>
>>> 
>>> type(0.000000000001)
<class 'float'>
```



### 类型转换

- BIF 函数： int(), str(), float()
- 浮点数转成整数，不是四舍五入，而是直接向下去整

```
>>> a = '520'
>>> b = int(a)
>>> b
520
>>> 
>>> 
>>> b = int('小甲鱼')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '小甲鱼'

>>> a = 5.99
>>> b = str(a)
>>> b
'5.99'

>>> b = int(a)
>>> b
5
```



### 判断类型

- *type()*, 返回值True，False
- 函数 _isinstance( __ obj, __class_or_tuple)_， 返回值True，False
- 字符串模块 str.isdigital(), 返回值True，False



## 课后作业

### Quiz

1. 在 Python 中，int 表示整型，那你还记得 bool、float 和 str 分别表示什么吗？ 
2. 你知道为什么布尔类型(bool)的 True 和 False 分别用 1 和 0 来代替吗？ 
3. 使用 int() 将小数转换为整数，结果是向上取整还是向下取整呢？ 
4. 我们人类思维是习惯于“四舍五入”法，你有什么办法使得 int() 按照“四舍五入”的方式取整吗？ 
5. 取得一个变量的类型，视频中介绍可以使用 type() 和 isinstance()，你更倾向于使用哪个？ 
6. Python3 可以给变量命名中文名，知道为什么吗？ 
7. 【该题针对零基础的鱼油】你觉得这个系列教学有难度吗？ 

### Practice

1. 针对视频中小甲鱼提到的小漏洞，再次改进我们的小游戏：当用户输入错误类型的时候，及时提醒用户重新输入，防止程序崩溃。 

   如果你尝试过以下做法，请举下小手： 

   ```python
   temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：") 
   # 这种想法是因为type(1)会返回<class 'int'>，如果type(temp)返回结果一致说明输入是整数。 
   
   while type(temp) != type(1):
   	print("抱歉，输入不合法，", end='') 
   	temp = input("请输入一个整数：")
   ```

   或者可能这样:

   ```python
   temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
   # not操作符的作用是将布尔类型的结果翻转：即取反的意思，not True == Flase
   while not isinstance(temp, int):
     print("抱歉，输入不合法，", end='')
     temp = input("请输入一个整数：")
   ```

   以上方法的思路是正确的，不过似乎忽略了一点儿：就是input()的返回值始终是字符串，所以type(temp)永远是<class 'str'> ！ 其实有蛮多的做法可以实现的，不过就目前我们学习过的内容来看，还不足够。 所以，在让大家动手完成这道题之前，小甲鱼介绍一点新东西给大家！

   > s为字符串 
   >
   > s.isalnum() 所有字符都是数字或者字母，为真返回 Ture，否则返回 False
   >
   > s.isalpha() 所有字符都是字母，为真返回 Ture，否则返回 False
   >
   > s.isdigit() 所有字符都是数字，为真返回 Ture，否则返回 False 
   >
   > s.islower() 所有字符都是小写，为真返回 Ture，否则返回 False
   >
   > s.isupper() 所有字符都是大写，为真返回 Ture，否则返回 False

   好了，文字教程就到这里，大家赶紧趁热打铁，改造我们的小游戏吧！ 

   

   ```python
   # Design the game, guess a number, try maximum 3 times
   import random
   
   print("This is the game program")
   
   secret = random.randint(1, 10)
   
   guess = 0
   count = 3
   
   while count > 0 and guess != secret:
       temp = input("please input a number:")
       
       ## 判断输入格式是否正确
       while not temp.isdigit():
           temp = input("your input is not a number, please input again, please input a correct number:")
       guess = int(temp)
       if guess > secret:
           print("your guess number is big, input a smaller one")
       else:
           print("your input number is small, input a bigger one")
   
       count = count - 1
   
   if guess == secret:
       print('your guess is exactly right!! Congrats!')
   else:
       print('You already tried three times, game over!')
   ```

   ​		

2. 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用） 

   这样定义闰年的:能被4整除但不能被100整除,或者能被400整除都是闰年。 

   ```python
   # 判断闰年
   # 能被4整除但不能被100整除,或者能被400整除都是闰年。
   
   temp = input('清输入一个年份：')
   while not temp.isdigit():
       temp = input('输入的不是年份，清重新输入：')
   
   year = int(temp)
   
   # 采用取余数的方法
   if (year % 4 == 0) and (year % 100 != 0):
       print('%d 是闰年' % year)
   else:
       if year % 400 == 0:
           print('%d 是闰年' % year)
       else:
           print('%d 不是闰年' % year)
   ```

   



3. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！ 

   参考知识点总结内容

# 006. Pyhon之常用操作符

## 知识点

### 算术操作符

```
>>> a = b = c = d = 10
>>> a += 1
>>> b -= 3
>>> c *= 10
>>> d /= 8
>>> a
11
>>> b
7
>>> c
100
>>> d
1.25
```

- 幂运算： **

- 地板除法：//

  > **python3.0**
  >
  > /总是执行真除法，不管操作数的类型，都返回浮点数结果（即使能整除，如4/2==2.0）；
  > //执行Floor除法，会截断余数直接返回一个整数，如果有任何一个操作数是浮点数则返回浮点数（如4//2==2,3//2==1, 4.0//2==2.0）
  >
  > 总之：在python3.0中，/为真除法，不会截断，且结果无论能否整除都是浮点数；//为地板除法，会对除法的结果进行取整返回，至于返回的结果是否是浮点数取决于操作数中有无浮点数，如两个操作数都是整数那么就直接返回一个取整后的整数，如果操作数中有浮点数则返回结果是浮点数。
  >
  > **python2.0**
  >
  > /表示传统除法，如果两个操作数都是整数的话执行截断除法，否则执行浮点除法，//执行Floor除法，同3.0

### 优先级问题

- 先乘除后加减，遇到括号先算括号

  ```
  >>> -3 * 2 + 5 / -2 -4
  -12.5
  ```

- 比较操作符优先级大于逻辑操作符

  ```
  >>> 3 < 4 and 4 < 5
  True
  ```

- 加括号让代码可读性更高

  ```
  >>> (3 < 4 ) and ( 4 < 5 )
  True
  ```

- 幂预算操作符比起左侧运算符优先级高，比其右侧操作符优先级低

  ```
  >>> - 3 ** 2
  -9
  >>> -(3 ** 2)
  -9
  >>> 3 ** -2
  0.1111111111111111
  >>> 3 ** (-2)
  0.1111111111111111
  ```

### 逻辑操作符

- and
- or
- not

not or and 的优先级是不同的：not > and > or 

#### 短路逻辑（short-circuit logic)

逻辑操作符有个有趣的特性：在不需要求值的时候不进行操作。这么说可能比较“高深”，举个例子，表达式 x and y，需要 x 和 y 两个变量同时为真(True)的时候，结果才为真。因此，如果当 x 变量得知是假(False)的时候，表达式就会立刻返回 False，而不用去管 y 变量的值。 这种行为被称为短路逻辑（short-circuit logic）或者惰性求值（lazy evaluation），这种行为同样也应用与 or 操作符

```
首先，and’、‘or’和‘not’的优先级是not>and>or
其次，逻辑操作符and 和or 也称作短路操作符（short-circuitlogic）或者惰性求值（lazy evaluation）：
它们的参数从左向右解析，一旦结果可以确定就停止。
 
and ：x and y 返回的结果是决定表达式结果的值。如果 x 为真，则 y 决定结果，返回 y ；如果 x 为假，x 决定了结果为假，返回 x。
       由于是短路操作符，是因为and运算符必须所有的运算数都是true才会把所有的运算数都解析，并且返回最后一个变量，
>>> 3 and 4
4
>>> 4 and 3
3
>>> 0 and 3
0
>>> 3 and 0
0
 
or ： x or y   逻辑（or），即只要有一个是true，即停止解析运算数，返回最近为true的变量，
>>> 3 or 4
3
>>> 4 or 3
4
>>> 3 or 0
3
>>> 0 or 3
3
 
not : 返回表达式结果的“相反的值”。如果表达式结果为真，则返回false；如果表达式结果为假，则返回true。
>>> not 3
False
>>> not 0
True
```





<img src="/Users/felix/Library/Application Support/typora-user-images/image-20220402102743013.png" alt="image-20220402102743013" style="zoom:20%;" />

## 课后作业

### Quiz

1. Python 的 floor 除法现在使用 “//” 实现，那 3.0 // 2.0 您目测会显示什么内容呢？ 

   1.0； *有任何一个操作数是浮点数则返回结果为浮点数*

2. a < b < c 事实上是等于？ 

   a < b and b < c

3. 不使用 IDLE，你可以轻松说出 5 ** -2 的值吗？ 

   0.04

4. 如何简单判断一个数是奇数还是偶数？ 

   a % 2 == 0 ; a % 2 == 1

5. 请用最快速度说出答案：not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9

   not or and 的优先级是不同的：not > and > or 

   ```
   >>> not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
   4
   >>> 
   >>> (not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)
   4
   ```

   

6. 还记得我们上节课那个求闰年的作业吗？如果还没有学到“求余”操作，还记得用什么方法可以“委曲求全”代替“%”的功能呢？ 

   ```python
   # 判断闰年
   # 能被4整除但不能被100整除,或者能被400整除都是闰年。
   
   temp = input('清输入一个年份：')
   while not temp.isdigit():
       temp = input('输入的不是年份，清重新输入：')
   
   year = int(temp)
   
   if (year/4 == int(year/4)) and (year/100 != int(year/100)):
       print('%d 是闰年' % year)
   else:
       if year/400 == int(year/400):
           print('%d 是闰年' % year)
       else:
           print('%d 不是闰年' % year)
   ```

   

### Practice

1. 请写一个程序打印出 0~100 所有的奇数。 

   ```python
   # 打印出 0~100 所有的奇
   
   number = 0
   
   while number <= 100:
       if number % 2 == 1:
           print(number)
       number += 1
   ```

   

2. 我们说过现在的 Python 可以计算很大很大的数据，但是......真正的大数据计算可是要靠刚刚的硬件滴，不妨写一个小代码，让你的计算机为之崩溃？ 

   ```python
   
   ```

   

3. 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。 （小甲鱼温馨提示：步子太大真的容易扯着蛋~~~） 

   题目：请编程求解该阶梯至少有多少阶？ 

   119 级

   ```python
   # 爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
   
   # 设定初始值为7级台阶
   stage = 7
   
   # 算出的符合条件的结果，当为1 的时候，表示第一个算出的，也是至少有多少级台阶
   result = 0
   
   while stage > 0 and result != 1:
       if (stage % 7 == 0) and (stage % 2 == 1) and (stage % 5 == 4) and (stage % 6 == 5):
           print('至少有 %d 级台阶' % stage)
           result = 1
       stage += 7
   ```

   

# 007. 了不起的分支和循环-1

## 知识点

### 打飞机编程

- 判断： 该不该做某事； if... else; if...elif....else
- 循环： 持续的做某事； while 循环，for 循环

# 008. 了不起的分支和循环-2

## 知识点

### 分支编程实例

按照100分制，90分以上成绩为A， 80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。

- 程序-1

  ```python
  score = int(input('请输入一个分数：'))
  if 100 >= score >= 90:
    print('A')
  if 90 > score >= 80:
    print('B')
  if 80 > score >= 60:
    print('C')
  if 60 > score >= 0:
    print('D')
  if score < 0 or score > 100:
    print('输入错误！')
  ```

  

- 程序-2

  ```python
  score = int(input('请输入一个分数：'))
  if 100 >= score >= 90:
    print('A')
  else:
    if 90 > score >= 80:
      print('B')
    else:
      if 80 > score >= 60:
        print('C')
      else:
        if 60 > score >= 0:
          print('D')
        else:
          print('输入错误！')
  ```

  

- 程序-3

  ```python
  score = int(input('请输入一个分数：'))
  if 100 >= score >= 90:
    print('A')
  elif 90 > score >= 80:
    print('B')
  elif 80 > score >= 60:
    print('C')
  elif 60 > score >= 0:
    print('D')
  else:
    print('输入错误！')
  ```

  

### 编程思维

1. 应该考虑程序的高效性； if and elif....； 程序-1 所有的if 每次都要执行一遍，效率低下; 程序-3 体现了python的简洁和可读性好

2. Python 可以有效避免“悬挂” else

   - 什么是“悬挂else”

   - 我们举个例子，初学C语言的朋友可能很容易被以下代码欺骗：C 语言采用就近if。。。else 匹配原则

     ```c
     if ( hi > 2 )
       if ( hi > 7 )
         		printf( "好棒！好棒！" )；
     else
       print( "切～" )；
     ```

   - Python 采用强制规定锁进原则，否则程序无法跑起来，给程序猿自己决定if-else 搭配

3. 条件表达式（三元操作符）

   有了这个三元操作符的条件表达式，你可以使用一条语句来完成以下的条件判断和赋值操作：

   ```python
   x, y = 4, 5
   if x > y:
     small = x
   else:
     small = y
   
   # 这个例子可以改进为
   small = x if x < y else y
   ```

4. 断言 （assert）

   assert 这个关键字我们称之为断言，当这个关键字后面的条件为假的时候，程序自动崩溃并抛出AssertionError的异常。

   举个例子：

   ```python
   >>> assert 3 > 4
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   AssertionError
   ```

   一般来说我们可以用它再程序中置入检查点，当需要确保程序中的某个条件一定为真才能让程序正常工作的话，assert 关键字就非常有用了



## 课后作业

### Quiz

1. if not (money < 100): 上边这行代码相当于？ 

   if money >= 100

2. assert 的作用是什么？ 

   在程序中置入检查点，当需要确保程序中的某个条件一定为真才能让程序正常工作的话，assert 关键字就非常有用

3. 假设有 x = 1，y = 2，z = 3，请问如何快速将三个变量的值互相交换？ 

   x, y, z = z, y, x

4. 猜猜 (x < y and [x] or [y])[0] 实现什么样的功能？

   三元运算的功能, 相当于  =  [x] if x < y else [y] 

5. 你听说过成员资格运算符吗？ 

   in 运算符

### Practice

1. 视频中小甲鱼使用 if elif else 在大多数情况下效率要比全部使用 if 要高，但根据一般的统计规律，一个班的成绩一般服从正态分布，也就是说平均成绩一般集中在 70~80 分之间，因此根据统计规律，我们还可以改进下程序以提高效率

   > 题目备忘：按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。 

```python
score = int(input('请输入一个分数：'))
if 80 > score >= 60:
  print('C')
elif 90 > score >= 80:
  print('B')
elif 60 > score >= 0:
  print('D')
elif 100 >= score >= 90:
  print('A')
else:
  print('输入错误！')
```



2. Python 的作者在很长一段时间不肯加入三元操作符就是怕跟C语言一样搞出国际乱码大赛，蛋疼的复杂度让初学者望而生畏，不过，如果你一旦搞清楚了三元操作符的使用技巧，或许一些比较复杂的问题反而迎刃而解。 请将以下代码修改为三元操作符实现： 

   ```python
   x, y, z = 6, 5, 4 
   if x < y:
     small = x 
     if z < small:
       small = z 
   elif y < z:
     small = y 
   else:
     small = z
   ```

可以改为：

```python
small = x if (x < y and z >= x) else (y if y < z else z)
```



3. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！ 

# 009. 了不起的分支和循环-3

## 知识点

### while 循环

### for 循环

虽然说pytohn 是由C 语言编写而来，但是他的for 循环跟C 语言循环不太一样，python的for 循环会自动捕获iteration 异常并且结束循环，因此显得更为智能和强大

- range()
  - 语法：range(start, stop[, step=1])
  - 这个BIF 有三个参数，其中用中括号括起来的两个表示的参数是可选的
  - step=1 表示第三个参数的值默认是1
  - range这个BIF的作用是生成一个从start 参数的值开始到stop 参数的值结束的数字序列

### break 和 continue

continue 用来终止本轮循环，开始下一轮循环



## 课后作业

### Quiz

1. 下面的循环会打印多少次"I Love FishC"？ 

   ```python
   for i in range(0, 10, 2):
     print('I Love FishC')
   ```

​		5次

2. 下面的循环会打印多少次"I Love FishC"？ 

   ```python
   for i in 5:
     print('I Love FishC')
   ```

   0次, "TypeError: 'int' object is not iterable"

3. 回顾一下 break 和 continue 在循环中起到的作用？ 

   Break 是终止循环，跳出循环体； Continue 是结束本次循环，立即开始下次循环

4. 请谈下你对列表的理解？ 

   列表本质上是一个可迭代器

5. 请问 range(10) 生成哪些数？ 

   0，1，2， 3， 4，5 ，6，7 ，8， 9

6. 目测以下程序会打印什么？ 

   ```python
   while True:
     while True:
       break
       print(1)
     print(2)
     break
   print(3)
   ```

​		2

​		3

7. 什么情况下我们要使循环永远为真？ 

8. 【学会提高代码的效率】你的觉得以下代码效率方面怎样？有没有办法可以大幅度改进(仍然使用while)？ 

   ```python
   i = 0
   string = 'ILoveFishC.com'
   while i < len(string)):
     print(i)
     i += 1
   ```

   

### Practice

1. 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含**"\*"**则不计算在内。 

   

2. 编写一个程序，求 100~999 之间的所有水仙花数。 

> 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。 



2. 三色球问题 

> 有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。 



3. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！ 







