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

- break 用来终止这一层的循环，跳出
- continue 用来终止本轮循环，开始下一轮循环
- Break 和 Continue 都只能影响一层



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

   保证循环体的内容一定要执行的情况下

8. 【学会提高代码的效率】你的觉得以下代码效率方面怎样？有没有办法可以大幅度改进(仍然使用while)？ 

   ```python
   i = 0
   string = 'ILoveFishC.com'
   while i < len(string)):
     print(i)
     i += 1
   ```

   ```python
   # 修改后的程序，避免每次循环都要run 一次len() 函数
   string = 'ILoveFishC.com'
   count = len(string)
   i = 0
   while i < count:
     print(i)
     i += 1
   ```

   

### Practice

1. 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含**"\*"**则不计算在内。 

   ```python
   # 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含**"\*"**则不计算在内。
   
   password = "novirus"
   count = 0
   while True:
       if count <= 2:
           userInputPass = input('please input the password:')
           if userInputPass == password:
               print('your password input is correct! Congrats!')
               break
           else:
               if '*' not in userInputPass:
                   count += 1
               print('your password input is incorrect, please input again!')
   
       else:
           print('you already input 3 times, the password input is frozen!')
           break
   ```

   ```python
   # 优化一下上述程序
   
   password = "novirus"
   count = 3
   while True:
       if count > 0:
           userInputPass = input('please input the password:')
           if userInputPass == password:
               print('your password input is correct! Congrats!')
               break
           elif '*' not in userInputPass:
               count -= 1
               print('your password input is incorrect, you have %d tries left' % count)
           else:
               print('your password input is incorrect, you have %d tries left' % count)
               continue
       else:
           print('you already input 3 times, the password input is frozen!')
           break
   ```

   

   ```python
   ## 进一步优化
   
   password = "novirus"
   count = 3
   while count:
       userInputPass = input('please input the password:')
       if userInputPass == password:
           print('your password input is correct! Congrats!')
           break
       elif '*' in userInputPass:
           print('your password input is incorrect, you have %d tries left' % count )
           continue
       else:
           print('your password input is incorrect, you have %d tries left' % (count-1))
       count -= 1
   ```

   

2. 编写一个程序，求 100~999 之间的所有水仙花数。 

> 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。 

```python
# 1. 编写一个程序，求 100~999 之间的所有水仙花数。
#
# > 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。

for number in range(100, 1000):
    hundreds = number // 100
    tens = (number // 10) % 10
    single = number % 10

    if number == hundreds ** 3 + tens ** 3 + single ** 3:
        print(number, end=' ')
```



```python
# 另外一种方法，通过字符串和整型的互相转换
for number in range(100, 1000):
    numstr = str(number)
    if number == int(numstr[0])**3 + int(numstr[1])**3 + int(numstr[2])**3:
        print(number, end=' ')
```

3. 三色球问题 

> 有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，蓝球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。 

```python
# 3. 三色球问题
#
# > 有红、黄、蓝三种颜色的求，其中红球 3 个，黄球 3 个，蓝球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。


# x + y + z = 8
# x is red, y is yellow, z is blue

for x in range(0, 4):
    for y in range(0, 4):
        for z in range(2, 7):
            if x + y + z == 8:
                print('totally we can have %d red, %d yellow, %d blue' % (x, y, z))
```

4. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！ 



# 010. 列表：一个打了激素的数组-1

## 知识点

### 创建列表

- 创建一个普通列表
- 创建一个混合列表
- 创建一个空列表

```python
>>> member = ['小布丁', '小甲鱼']
>>> 
>>> member
['小布丁', '小甲鱼']
>>> type(member)
<class 'list'>
>>> 
>>> 
>>> number = [1, 2, 3, 4]
>>> 
>>> number
[1, 2, 3, 4]
>>> 
>>> 
>>> mix = [1, '小甲鱼', 3.14, [1, 2, 3] ]
>>> 
>>> mix
[1, '小甲鱼', 3.14, [1, 2, 3]]
>>> 
>>> 
>>> empty = []
>>> 
>>> empty
[]
```



### 向列表添加元素

- append()

  ```
  >>> member.append('福禄娃娃')
  >>> 
  >>> member
  ['小布丁', '小甲鱼', '福禄娃娃']
  >>> 
  >>> len(member)
  3
  ```

- extend()

  ```
  >>> member.extend(['竹林小溪', 'crybaby'])
  >>> 
  >>> member
  ['小布丁', '小甲鱼', '福禄娃娃', '竹林小溪', 'crybaby']
  >>> 
  >>> len(member)
  5
  ```

- insert()

  ```
  >>> member.insert(0, '牡丹')
  >>> 
  >>> member
  ['牡丹', '小布丁', '小甲鱼', '福禄娃娃', '竹林小溪', 'crybaby']
  >>> 
  >>> len(member)
  6
  ```

> append() 和 extend()  只有一个参数，默认都是添加到列表的末尾
>
> extend() 是用一个列表追加另一个列表，所以参数是一个列表
>
> insert() 第一个参数是插入位置



## 课后作业

### Quiz

1. 列表都可以存放一些什么东西？

   整数，浮点数，字符串，对象

2.  向列表增加元素有哪些方法？

   append(), extend(), insert() 

3. append() 方法和 extend() 方法都是向列表的末尾增加元素，请问他们有什么区别？ 

   extend() 的参数是列表

4. member.append(['竹林小溪', 'Crazy迷恋']) 和 member.extend(['竹林小溪', 'Crazy迷恋']) 实现的效果一样吗？

    不一样，append 增加的是一个元素：1个列表对象； extend 增加的是2个元素：列表中的2个元素

5. 有列表 name = ['F', 'i', 'h', 'C']，如果小甲鱼想要在元素 'i' 和 'h' 之间插入元素 's'，应该使用什么方法来插入？ 

   name.insert(2, 's')

### Practice

1. 自己动手试试看，并分析在这种情况下，向列表添加数据应当采用哪种方法比较好？ 

> 假设给定以下列表： 
>
> member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳'] 
>
> 要求将列表修改为： 
>
> member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88] 
>
> 方法一：使用 insert() 和 append() 方法修改列表。
>
>  方法二：重新创建一个同名字的列表覆盖。 

```python
# 方法一
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
index = 1


member.insert(1, 88)
member.insert(3, 90)
member.insert(5, 85)
member.insert(7, 90)
member.append(88)

print(member)
```

```python
# 方法二：
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
number = [88, 90,  85, 90,  88]
new = []

index = 0

while index < len(member):
    new.extend([member[index], number[index]])
    index += 1

member = new
print(member)
```



2. 利用 for 循环打印上边 member 列表中的每个内容，如图：

![member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]](https://img-blog.csdnimg.cn/20200330223209818.png)



```python
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

for i in member:
    print(i)
```





3. 上一题打印的样式不是很好，能不能修改一下代码打印成下图的样式呢？【请至少使用两种方法实现】 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200330223316122.png)

```python
# 上一题打印的样式不是很好，能不能修改一下代码打印成下图的样式呢？【请至少使用两种方法实现】

# 方法一
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

lenth = len(member)

for i in range(0, lenth, 2):
    print(member[i], member[i+1])
```



```python
# 方法二
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

for each in range(len(member)):
    if each % 2 == 0:
        print(member[each], member[each+1])
```



# 011. 列表：一个打了激素的数组-2

## 知识点

### 从列表中获取元素

通过索引值index 获取单个元素，从0开始

```python
>>> member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88] 
>>> member[0]
'小甲鱼'
>>> 
>>> member[1]
88
>>> 

# 交换数组元素
>>> temp = member[0]
>>> 
>>> member[0] = member[1]
>>> 
>>> member[1] = temp
>>> 
>>> member
[88, '小甲鱼', '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
```



### 从列表中删除元素

- remove() ; 参数是具体的存在于列表中的元素值，不需要知道位置

  ```python
  >>> member.remove('小甲鱼')
  >>> 
  >>> member
  [88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
  >>> 
  >>> member.remove('小甲鱼')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: list.remove(x): x not in list
  ```

  

- del

  - del <列表名字>；del member ， 会删除整个列表
  - del <列表元素>； del member[0]， 删除某个特定的列表元素

  ```python
  >>> member
  [88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
  >>> 
  >>> 
  >>> del member[0]
  >>> 
  >>> member
  ['黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
  >>> 
  >>> 
  >>> del member
  >>> 
  >>> member
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'member' is not defined
  ```

  

- pop()

  - 列表是通过栈存储数据的，可以通过pop 来弹栈数据
  - 不加任何参数，默认从列表中取出最后一个元素，并且弹出来
  - 可以加上参数index，弹出具体某个元素

  ```python
  >>> member = ['黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
  >>> member
  ['黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
  >>> member.pop()
  88
  >>> 
  >>> member
  ['黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳']
  >>> name = member.pop()
  >>> 
  >>> name
  '秋舞斜阳'
  >>> 
  >>> member
  ['黑夜', 90, '迷途', 85, '怡静', 90]
  >>> member.pop(1)
  90
  >>> 
  >>> member
  ['黑夜', '迷途', 85, '怡静', 90]
  ```



### 列表分片（slice）

- 利用索引可以每次获取一个元素；但是如果需要每次获取多个元素，需要采用列表分片

- 利用列表分片，得到一个列表的拷贝，返回值是列表

- 列表分片操作，原列表不会有任何改变

  ```pyth
  >>> member
  ['黑夜', '迷途', 85, '怡静', 90]
  >>> member[1:3]
  ['迷途', 85]
  >>> 
  >>> member
  ['黑夜', '迷途', 85, '怡静', 90]
  >>> member[:3]
  ['黑夜', '迷途', 85]
  >>> 
  >>> member[1:]
  ['迷途', 85, '怡静', 90]
  >>> 
  >>> member[:]
  ['黑夜', '迷途', 85, '怡静', 90]
  ```



## 课后作业

### Quiz

1. 下边的列表分片操作会打印什么内容？
   list1 = [1, 3, 2, 9, 7, 8]
   list1[2:5]

   [2, 9, 7]

2. 请问 list1[0] 和 list1[0:1] 一样吗？

   不一样，list1[0] 是一个元素：1， list[0:1] 是一个列表：[1]

3. 如果你每次想从列表的末尾取出一个元素，并将这个元素插入到列表的最前边，你会怎么做？

   list.insert(0, list.pop())

4. 有些鱼油比较调皮，他说我想试试 list1[-3:-1] 会不会报错，怎么知道一试居然显示 [9, 7]，这是怎么回事呢？

   Python 列表逆向切片，从右至左

5. 在进行分片的时候，我们知道分片的开始和结束位置需要进行指定，但其实还有另外一个隐藏的设置：步长。
   list1[0:6:2]

   - 简洁分片操作：
     list1[::2]

   - 步长不能为0，会报错
     list1 = [1, 3, 2, 9, 7, 8]
     list1 = [ : : 0 ]

   - 步长可以是负数，改变方向（从尾部开始向左走）
     list1[::-2]

     ```python
     >>> list1[0:6:2]
     [1, 2, 7]
     >>> 
     >>> list1[::2]
     [1, 2, 7]
     >>> 
     >>> list=[::0]
       File "<stdin>", line 1
         list=[::0]
               ^
     SyntaxError: invalid syntax
     >>> 
     >>> list1[::-2]
     [8, 9, 3]
     ```

     

6. 课堂上小甲鱼说可以利用分片完成列表的拷贝 list2 = list1[:]，那事实上可不可以直接写成 list2 = list1 更加简洁呢？

   不能，list2 = list1 并没有拷贝数据存储在内存中，而是给同一份内存数据加上了一个新的标签：list2

```python
 list1 = [1, 3, 2, 9, 7, 8]
 list2 = list1[:]
 list2 
[1, 3, 2, 9, 7, 8]
 list3 = list1
 list3
[1, 3, 2, 9, 7, 8]
 list1.sort()
 list1
[1, 2, 3, 7, 8, 9] 
 list2
[1, 3, 2, 9, 7, 8]
 list3
[1, 2, 3, 7, 8, 9] 
```

6.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式



# 012. 列表：一个打了激素的数组-3

## 知识点

### 列表操作符

- 比较操作符

  列表比较，当有多个元素的时候，默认从第0个元素开始比较

  ```python
  >>> list1 = [123]
  >>> list2 = [234]
  >>> list1 > list2
  False 
  >>> 
  >>> list1 = [123, 456]
  >>> list2 = [234, 123]
  >>> 
  >>> list1 > list2
  False
  ```

- 逻辑操作符

  ```
  >>> list3 = [123, 456]
  >>> 
  >>> (list1 < list2) and (list1 == list3)
  True
  ```

- 连接操作符

  类似于extend（），但是不建议使用 + 来扩展或添加列表元素，建议使用insert，append，extend

  ```
  >>> list4 = list1 + list2
  >>> list4
  [123, 456, 234, 123]
  ```

- 重复操作符

  ```
  >>> list3 * 3
  [123, 456, 123, 456, 123, 456]
  >>> 
  >>> list3 *= 3
  >>> list3
  [123, 456, 123, 456, 123, 456]
  >>> 
  >>> 
  >>> 
  >>> list3 *= 5
  >>> list3
  [123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456]
  ```

- 成员关系操作符

  - 列表中的列表的操作

  ```
  >>> 123 in list3
  True
  >>> 'xiaojiayu' not in list3
  True
  >>> 123 not in list3
  False
  >>> 
  >>> list5 = [123, ['xiaojiayu', 'mudan'], 456]
  >>> 'xiaojiayu'  in list5
  False 
  >>> 'xiaojiayu' in list5[1]
  True
  >>> 
  >>> list5[1][1]
  'mudan'
  ```



### 列表的小伙伴们

 ```python
 >>> dir(list)
 ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
 ```

- reverse(): 将整个列表反转

  ```
  >>> list3.reverse()
  >>> list3
  [456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123]
  ```

- sort(): 用指定的方式，对成员排序，默认是从小到大

  ```
  >>> list6 = [4, 2, 3, 5, 9, 8, 10]
  >>> list6.sort()
  >>> 
  >>> list6
  [2, 3, 4, 5, 8, 9, 10]
  >>>  
  >>> list6.sort(reverse=True)
  >>> list6
  [10, 9, 8, 5, 4, 3, 2]
  ```

- count(): 计算一个元素在列表中出现的次数

  ```
  >>> list3.count(123)
  15
  ```

- index(): 返回参数在列表中的位置

  ```
  >>> list3.index(123)
  0
  >>> 
  >>> list3.index(123, 3, 7)
  4
  ```

  

## 课后作业

### Quiz

1. 请问如何将下边这个列表的'小甲鱼'修改为'小鱿鱼'？ 

> list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18] 



```
list1[1][2][0] = '小鱿鱼'
```



2. 要对一个列表进行顺序排序，请问使用什么方法？

   ```python
   list.sort()
   ```

    

   

3. 要对一个列表进行逆序排序，请问使用什么方法？ 

   ```
   list.sort(reverse=true)
   
   或者：
   list.sort()
   list.reverse()
   ```

   

4. 列表还有两个内置方法没给大家介绍，不过聪明的你应该可以自己摸索使用的门道吧：copy() 和 clear() 

```
>>> list7 = list6.copy()
>>> 
>>> 
>>> 
>>> list7
[4, 2, 3, 5, 9, 8, 10]
>>> 
>>> 
>>> list6.sort()
>>> list6
[2, 3, 4, 5, 8, 9, 10]
>>> list7
[4, 2, 3, 5, 9, 8, 10]

>>> list7.clear()
>>> 
>>> list7
[]
```



5. 你有听说过列表推导式或列表解析吗？ 没听过？！没关系，我们现场来学习一下吧，看表达式： 

```
>>> [ i*i for i in range(10) ] 

>>> [i*i for i in range(10)] 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```



你觉得会打印什么内容？ 



居然分别打印了0到9各个数的平方，然后还放在列表里边了有木有？！

 列表推导式（List comprehensions）也叫列表解析，灵感取自函数式编程语言 Haskell。Ta 是一个非常有用和灵活的工具，可以用来动态的创建列表，语法如： [有关A的表达式 for A in B] 



例如 

```
>>> list1 = [x**2 for x in range(10)] 

>>> list1 

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
```

相当于 

```
list1 = [] 
for x in range(10): 
		list1.append(x**2) 
```



问题：请先在 IDLE 中获得下边列表的结果，并按照上方例子把列表推导式还原出来。 

```
list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0] 
```



```python
>>> for x in range(10):
...     for y in range(10):
...             if x%2==0 and y%2!=0:
...                     list1.append((x, y))
... 
>>> list1
[(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9), (6, 1), (6, 3), (6, 5), (6, 7), (6, 9), (8, 1), (8, 3), (8, 5), (8, 7), (8, 9)]
```



6. 活学活用：请使用列表推导式补充被小甲鱼不小心涂掉的部分 

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200225183701856.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L01hbWluZ3p1bw==,size_16,color_FFFFFF,t_70)

```python
list3=[y + ":" + x[2:] for x in list1 for y in list2 if x[0] == y[0]]
```





# 013. 元组：戴上了枷锁的列表

## 知识点

- 由于和列表是近亲关系，所以元组和列表在实际使用上是非常相似的。

- 元组可以切片，但是元组是不可改变的，不能随意插入修改元素

  ```
  >>> tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
  >>> type(tuple1)
  <class 'tuple'>
  >>> 
  >>> 
  >>> tuple1
  (1, 2, 3, 4, 5, 6, 7, 8)
  >>> 
  >>> tuple1[1]
  2
  >>> 
  >>> tuple1[5:]
  (6, 7, 8)
  >>> 
  >>> tuple2 = tuple1[:]
  >>> 
  >>> tuple2
  (1, 2, 3, 4, 5, 6, 7, 8)
  >>> 
  >>> tuple1[1] = 3
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
  >>> 
  ```

  

- 主要讨论以下知识点：

  - 创建和访问一个元组； 逗号是定义一个元组的关键，而不是小括号

    ```
    >>> temp = (1)
    >>> temp
    1
    >>> 
    >>> type(temp)
    <class 'int'>
    >>> 
    >>> temp2 = 2, 3, 4
    >>> 
    >>> temp2
    (2, 3, 4)
    >>> 
    >>> type(temp2)
    <class 'tuple'>
    >>> 
    >>> temp = ()
    >>> type(temp)
    <class 'tuple'>
    >>> temp
    ()
    >>> 
    >>> temp = (1, )
    >>> type(temp)
    <class 'tuple'>
    >>> 
    >>> temp
    (1,)
    >>> 
    >>> temp = 1, 
    >>> temp
    (1,)
    >>> type(temp)
    <class 'tuple'> 
    ```

  - 更新和删除一个元组

    通过连接符来修改一个元组，注意修改完之后，原来的元组还在内存中，过一会python 会检查是否还有标签（变量名）指向它，如果没有，会从内存中回收它

    ```
    >>> temp = ('小甲鱼', '小布丁', '迷途', '黑夜')
    >>> temp
    ('小甲鱼', '小布丁', '迷途', '黑夜')
    >>> 
    >>> temp = temp[:2] + ('怡静', ) + temp[2:]
    >>> 
    >>> temp
    ('小甲鱼', '小布丁', '怡静', '迷途', '黑夜')
    ```

    如果要强行回收资源，可以使用del 语法 

    ```
    >>> del temp
    >>> 
    >>> temp
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'temp' is not defined
    ```



- 列表的操作符和元组一样



## 课后作业

### Quiz

1. 请用一句话描述什么是列表？再用一句话描述什么是元组？ 

   列表：一个大仓库，你可以随时往里边添加和删除任何东西。 

   元组：封闭的列表，一旦定义，就不可改变（不能添加、删除或修改）

2. 什么情况下你需要使用元组而不是列表？

   当我们希望内容不被轻易改写的时候，我们使用元组（把权力关进牢笼）。 当我们需要频繁修改数据，我们使用列表。 

3. 当元组和列表掉下水，你会救谁？ 

   如果是我，我会救列表，因为列表提供了比元组更丰富的内置方法，这相当大的提高了编程的灵活性。 

   回头来看下元组，元组固然安全，但元组一定创建就无法修改（除非通过新建一个元组来间接修改，但这就带来了消耗），而我们人是经常摇摆不定的，所以元组只有在特殊的情况才用到，平时还是列表用的多。 综上所述，小甲鱼会救列表（列表是美眉）

4. 请将下图左边列表的内置方法与右边的注释连线，并圈出元组可以使用的方法。 

   ![img](https://images2018.cnblogs.com/blog/1274778/201805/1274778-20180510092732778-991558013.png)

   元组只能使用2个方法：count（）和index（）

5. 创建一个元组，什么情况下逗号和小括号必须同时存在，缺一不可？ 

   在通过拼接符创建元组的时候

6. x, y, z = 1, 2, 3 请问x, y, z是元组吗？ 

   所有的多对象的、逗号分隔的、没有明确用符号定义的这些集合默认的类型都是元组

   ```
   >>> x, y, z = 1, 2, 3
   >>> 
   >>> type(x)
   <class 'int'>
   >>> 
   >>> h = x, y, z
   >>> type(h)
   <class 'tuple'>
   ```

   

7. 请写出以下情景中应该使用列表还是元组来保存数据： 

   1. 游戏中角色的属性： 列表
   2. 你的身份证信息： 元组
   3. 论坛的会员： 列表
   4. 团队合作开发程序，传递给一个你并不了解具体实现的函数的参数：元组 
   5. 航天火箭各个组件的具体配置参数： 元组
   6. NASA系统中记录已经发现的行星数据： 列表

8. 上节课我们通过课后作业的形式学习到了“列表推导式”，那请问如果我把中括号改为小括号，会不会得到“元组推导式”呢？ 

   不能，因为元组不能向列表一样迭代更新



# 014. 字符串：各种奇葩的内置方法

## 知识点

### 字符串，列表，元组

- 字符串， 列表，元组 都属于序列类型，很多用法非常类似
- 字符串更像元组，一旦被定义，就不能修改。非要“修改”的话，可以参考元组的方式，采用拼接符“+” 的方式，注意旧的字符串还在，并没有改变
- 字符串和列表，元组一样可以索引，切片操作
- 字符串和列表，元组一样，使用比较操作符，逻辑操作符，成员关系操作符，连接操作符，重复操作符

{filename: }

### 字符串方法及注释

> 字符串的方法不会改变原来的字符串，一般都是返回一个新的字符串

| capitalize()                              | 把字符串的第一个字符改为大写                                 |
| ----------------------------------------- | ------------------------------------------------------------ |
| casefold()                                | 把整个字符串的所有字符改为小写                               |
| center(width)                             | 将字符串居中，并使用空格填充至长度 width 的新字符串          |
| count(sub[, start[, end]])                | 返回 sub 在字符串里边出现的次数，start 和 end 参数表示范围，可选。 |
| encode(encoding=‘utf-8’, errors=‘strict’) | 以 encoding 指定的编码格式对字符串进行编码。                 |
| endswith(sub[, start[, end]])             | 检查字符串是否以 sub 子字符串结束，如果是返回 True，否则返回 False。start 和 end 参数表示范围，可选。 |
| expandtabs([tabsize=8])                   | 把字符串中的 tab 符号（\t）转换为空格，如不指定参数，默认的空格数是 tabsize=8。 |
| find(sub[, start[, end]])                 | 检测 sub 是否包含在字符串中，如果有则返回索引值，否则返回 -1，start 和 end 参数表示范围，可选。 |
| index(sub[, start[, end]])                | 跟 find 方法一样，不过如果 sub 不在 string 中会产生一个异常。 |
| isalnum()                                 | 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False。 |
| isalpha()                                 | 如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False。 |
| isdecimal()                               | 如果字符串只包含十进制数字则返回 True，否则返回 False。      |
| isdigit()                                 | 如果字符串只包含数字则返回 True，否则返回 False。            |
| islower()                                 | 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回 True，否则返回 False。 |
| isnumeric()                               | 如果字符串中只包含数字字符，则返回 True，否则返回 False。    |
| isspace()                                 | 如果字符串中只包含空格，则返回 True，否则返回 False。        |
| istitle()                                 | 如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回 True，否则返回 False。 |
| isupper()                                 | 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回 True，否则返回 False。 |
| join(sub)                                 | 以字符串作为分隔符，插入到 sub 中所有的字符之间。            |
| ljust(width)                              | 返回一个左对齐的字符串，并使用空格填充至长度为 width 的新字符串。 |
| lower()                                   | 转换字符串中所有大写字符为小写。                             |
| lstrip()                                  | 去掉字符串左边的所有空格                                     |
| partition(sub)                            | 找到子字符串 sub，把字符串分成一个 3 元组 (pre_sub, sub, fol_sub)，如果字符串中不包含 sub 则返回 (‘原字符串’, ‘’, ‘’) |
| replace(old, new[, count])                | 把字符串中的 old 子字符串替换成 new 子字符串，如果 count 指定，则替换不超过 count 次。 |
| rfind(sub[, start[, end]])                | 类似于 find() 方法，不过是从右边开始查找。                   |
| rindex(sub[, start[, end]])               | 类似于 index() 方法，不过是从右边开始。                      |
| rjust(width)                              | 返回一个右对齐的字符串，并使用空格填充至长度为 width 的新字符串。 |
| rpartition(sub)                           | 类似于 partition() 方法，不过是从右边开始查找。              |
| rstrip()                                  | 删除字符串末尾的空格。                                       |
| split(sep=None, maxsplit=-1)              | 不带参数默认是以空格为分隔符切片字符串，如果 maxsplit 参数有设置，则仅分隔 maxsplit 个子字符串，返回切片后的子字符串拼接的列表。 |
| splitlines(([keepends]))                  | 在输出结果里是否去掉换行符，默认为 False，不包含换行符；如果为 True，则保留换行符。。 |
| startswith(prefix[, start[, end]])        | 检查字符串是否以 prefix 开头，是则返回 True，否则返回 False。start 和 end 参数可以指定范围检查，可选。 |
| strip([chars])                            | 删除字符串前边和后边所有的空格，chars 参数可以定制删除的字符，可选。 |
| swapcase()                                | 翻转字符串中的大小写。                                       |
| title()                                   | 返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串。 |
| translate(table)                          | 根据 table 的规则（可以由 str.maketrans(‘a’, ‘b’) 定制）转换字符串中的字符。 |
| upper()                                   | 转换字符串中的所有小写字符为大写。                           |
| zfill(width)                              | 返回长度为 width 的字符串，原字符串右对齐，前边用 0 填充。   |



```
>>> str1.capitalize()
'Abdc'
>>> str1
'abdc'
>>> str1.center(2)
'abdc'
>>> str1
'abdc'
>>> str1.center(12)
'    abdc    '
>>> str1.casefold()
'abdc'
>>> str2 = 'DAXDIExiaoyang'
>>> 
>>> str2.count('xi')
1
>>> str2.endswith('ng')
True
>>> 
>>> str3 = 'I\tlove\tFishC.com!'
>>> str3.expandtabs()
'I       love    FishC.com!'
>>> str3
'I\tlove\tFishC.com!'
>>> print(str3)
I	love	FishC.com!
>>> str3 = 'I\tlove\tFishC.com!'
>>> 
>>> print(str3)
I	love	FishC.com!
>>> str3.expandtabs(tabsize=18)
'I                 love              FishC.com!'
>>> str3.find('efc')
-1
>>> 
>>> str3.find('com')
13
>>> str3.index('efc')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> str4 = 'FishC'
>>> 
>>> str4.join('12345')
'1FishC2FishC3FishC4FishC5'
>>> str5 = '    i love you   '
>>> str5.lstrip()
'i love you   '
>>> str5
'    i love you   '
>>> str5.rstrip()
'    i love you'
>>> 
>>> str6 = 'l love fish'
>>> str6.partition('ov')
('l l', 'ov', 'e fish')
>>> 
>>> str6
'l love fish'
>>> str6.replace('fish', 'felix')
'l love felix' 
>>> str6
'l love fish'
>>> str6.split()
['l', 'love', 'fish']
>>> str6.split('i')
['l love f', 'sh']
>>> str6.startswith('I')
False
>>> str6.startswith('i')
False
>>> str6.startswith('1')
False
>>> str6
'l love fish'
>>> str6.startswith('l')
True
>>> str7 = '     aaaasssss    '
>>> str7.strip()
'aaaasssss'
>>> str7 = str7.strip()
>>> str7
'aaaasssss'
>>> str7.strip('s')
'aaaa'
>>> str7.swapcase()
'AAAASSSSS'
>>> 
>>> str7.title()
'Aaaasssss'
```



## 课后作业

### Quiz

1. 还记得如何定义一个跨越多行的字符串吗（请至少写出两种实现的方法）？

   ```
   方法一： 
   >>> str1 = '''待我长发及腰，将军归来可好？ 
   此身君子意逍遥，怎料山河萧萧。 
   天光乍破遇，暮雪白头老。 
   寒剑默听奔雷，长枪独守空壕。 
   醉卧沙场君莫笑，一夜吹彻画角。 
   江南晚来客，红绳结发梢。''' 
   
   方法二： 
   >>> str2 = '待卿长发及腰，我必凯旋回朝。\ 
   昔日纵马任逍遥，俱是少年英豪。\ 
   东都霞色好，西湖烟波渺。\ 
   执枪血战八方，誓守山河多娇。\ 
   应有得胜归来日，与卿共度良宵。\ 
   盼携手终老，愿与子同袍。' 
   
   方法三： 
   >>> str3 = ('待卿长发及腰，我必凯旋回朝。' 
   '昔日纵马任逍遥，俱是少年英豪。' 
   '东都霞色好，西湖烟波渺。' 
   '执枪血战八方，誓守山河多娇。' 
   '应有得胜归来日，与卿共度良宵。' 
   '盼携手终老，愿与子同袍。')
   ```

    

2. 三引号字符串通常我们用于做什么使用？ 

   注释

3. file1 = open('C:\windows\temp\readme.txt', 'r') 表示以只读方式打开“C:\windows\temp\readme.txt”这个文本文件，但事实上这个语句会报错，知道为什么吗？你会如何修改？ 

   文件名中包含默认的制表符：\t, \r... 需要指定用原始字符读取文件名，'r' 置于整个字符串的前面

   ```
   >>> file1 = open(r'C:\windows\temp\readme.txt', 'r')
   ```

4. 有字符串：

   ```
   str1 = '<a href="http://www.fishc.com/dvd" target="_blank">鱼C资源打包</a>'
   ```

   请问如何提取出子字符串：'www.fishc.com' 

   ```
   # 使用split() 方法可以以‘/’ 切片字符串，返回一个列表
   str1.split('/')[2]
   
   或者
   
   # 使用partition() 方法可以直接截取，返回一个元组
   str1.partition('www.fishc.com')[1]
   ```

   

5. 如果使用负数作为索引值进行分片操作，按照第三题的要求你能够正确目测出结果吗？ 

   ```
    str1.split('/')[-3]
   ```

   

6. 还是第三题那个字符串，请问下边语句会显示什么内容？ 	

```
>> str1[20:-36] 
'fishc'
```



7. 据说只有智商高于150的鱼油才能解开这个字符串（还原为有意义的字符串）：

   str1 = 'i2sl54ovvvb4e3bferi32s56h;$c43.sfc67o0cm99' 

   ```
   >>> str1[::3]
   'ilovefishc.com'
   ```

   

### Practice

1. 请写一个密码安全性检查的脚本代码：check.py 

> 密码安全性检查代码 
>
> 低级密码要求： 
>
> 1. 密码由单纯的数字或字母组成 
> 2. 密码长度小于等于8位 
>
> 中级密码要求： 
>
> 1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合 *
> 2. 密码长度不能低于8位 
>
> 高级密码要求： 
>
> 1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合 
>
> 2. 密码只能由字母开头
>
> 3. 密码长度不能低于16位 

程序演示： 

```python
specialchar = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"

while True:
    alphaflag, digitflag, specharflag = 0, 0, 0
    passstr = input('Please input your password: ')
    
		# 设置标记位
    for each in passstr:
        if each.isalpha():
            alphaflag = 1
        elif each.isdigit():
            digitflag = 1
        elif each in specialchar:
            specharflag = 1
        else:
            continue

    if passstr[0].isalpha() and len(passstr) >= 16 and alphaflag+digitflag+specharflag == 3:
        print('The password is strong!')
        break
    elif len(passstr) >= 8 and alphaflag+digitflag+specharflag >= 2:
        print('The password is medium!')
        break
    elif len(passstr) < 8 and (passstr.isdigit() or passstr.isalpha()):
        print('The password is weak!')
        break
    else:
        print('The password does not meet requirement, please input again!')
```



# 015. 字符串：格式化

## 知识点

### format()  方法

- 位置参数格式化

- 关键字参数格式化

- 混合位置和关键字参数格式化

  - 位置参数必须在关键字参数之前

  ```
  >>> "{0} love {1}.{2}".format("I", "flish", "com")
  'I love flish.com'
  >>> 
  >>> "{a} love {b}.{c}".format(a="I", b="flish", c="com")
  'I love flish.com'
  >>> 
  >>> "{0} love {b}.{c}".format("I", b="flish", c="com")
  'I love flish.com'
  >>> 
  >>> 
  >>> "{a} love {b}.{0}".format(a="I", b="flish", "com")
    File "<stdin>", line 1
      "{a} love {b}.{0}".format(a="I", b="flish", "com")
                                                       ^
  SyntaxError: positional argument follows keyword argument
  ```

- 两个特殊的例子

  - 如果要想打印格式化符号：花括号，该怎么办呢？ 其实类似于加一个反斜杠避免转义字符，可以用花括号把花括号括起来

    ```python
    >>> print('\\')
    \
    >>> 
    >>> print('{{0}}'.format('不打印'))
    {0}
    >>> '{{0}}'.format('不打印')
    '{0}'
    ```

    

  - 为什么下面的这个output 是27.7GB，而不是27.658GB呢？

    位置参数0 后面的冒号：表示格式化符号的开始，后面接的‘.1f’ 就是格式化符号，‘.1’ 表示四舍五入，‘f’ 表示定点数

    ```python
    >>> '{0:.1f}{1}'.format(27.658,'GB')
    '27.7GB'
    ```

### Python3 字符串格式化符号含义及转义字符含义

- 字符串格式化符号含义

  | 符  号 | 说   明                                |
  | ------ | -------------------------------------- |
  | %c     | 格式化字符及其ASCII码                  |
  | %s     | 格式化字符串                           |
  | %d     | 格式化整数                             |
  | %b     | 格式化无符号二进制数                   |
  | %o     | 格式化无符号八进制数                   |
  | %x     | 格式化无符号十六进制数                 |
  | %X     | 格式化无符号十六进制数（大写）         |
  | %f     | 格式化定点数，可指定小数点后的精度     |
  | %e     | 用科学计数法格式化定点数               |
  | %E     | 作用同%e，用科学计数法格式化定点数     |
  | %g     | 根据值的大小决定使用%f活%e             |
  | %G     | 作用同%g，根据值的大小决定使用%f或者%E |

  ```python
  >>> '%c' % 97
  'a'
  >>> '%c %c %c' % (97, 98, 99)
  'a b c'
  >>> 
  >>> 
  >>> '%s' % 'I love fishC'
  'I love fishC'
  
  >>> 
  >>> '%d + %d = %d' %(4, 5 , 4+5)
  '4 + 5 = 9'
  >>> 
  >>> '%o' %10
  '12'
  >>> 
  >>> '%x' %10
  'a'
  >>> '%X' %10
  'A'
  >>> 
  >>> 
  >>> '%X' %160
  'A0'
  >>> 
  >>> '%f' % 27.658
  '27.658000'
  >>> 
  >>> 
  >>> '%e' % 27.658
  '2.765800e+01'
  >>> '%E' % 27.658
  '2.765800E+01'
  >>> 
  >>> '%g' % 27.658
  '27.658'
  >>> '%g' % 27.65843824837284738274832784732
  '27.6584'
  >>> '%g' % 2765843824837284738274832784732
  '2.76584e+30'
  ```

  

- 格式化操作符辅助指令

  | 符  号 | 说   明                                                    |
  | ------ | ---------------------------------------------------------- |
  | m.n    | m是显示的最小总宽度，n是小数点后的位数                     |
  | -      | 用于左对齐                                                 |
  | +      | 在正数前面显示加号（+）                                    |
  | #      | 在八进制数前面显示 '0o'，在十六进制数前面显示 '0x' 或 '0X' |
  | 0      | 显示的数字前面填充 '0' 取代空格                            |

  ```python
  >>> '%5.1f' %27.658
  ' 27.7'
  >>> 
  >>> '%.2e' %27.658
  '2.77e+01'
  >>> 
  >>> 
  >>> '%10d' %5
  '         5'
  >>> '%-10d' %5
  '5         '
  >>> '%+10d' %5
  '        +5'
  >>> '%+10d' %-5
  '        -5'
  >>> 
  >>> '%+-10d' %5
  '+5        '
  >>> 
  >>> 
  >>> '%#o' % 10
  '0o12'
  >>> 
  >>> '%#x' % 10
  '0xa'
  >>> '%#X' % 10
  '0XA'
  >>> 
  >>> 
  >>> 
  >>> '%#d' % 10
  '10'
  >>> '%010d' % 10
  '0000000010'
  >>> '%-010d' % 10
  '10        '
  ```

  

- 字符串转义字符含义

  | 符  号 | 说   明              |
  | ------ | -------------------- |
  | \'     | 单引号               |
  | \"     | 双引号               |
  | \a     | 发出系统响铃声       |
  | \b     | 退格符               |
  | \n     | 换行符               |
  | \t     | 横向制表符（TAB）    |
  | \v     | 纵向制表符           |
  | \r     | 回车符               |
  | \f     | 换页符               |
  | \o     | 八进制数代表的字符   |
  | \x     | 十六进制数代表的字符 |
  | \0     | 表示一个空字符       |
  | \\     | 反斜杠               |

## 课后作业

### Quiz

1. 根据说明填写相应的字符串格式化符号

   | 符 号 | 说 明                              |
   | ----- | ---------------------------------- |
   | %c    | 格式化字符及其ASCII码              |
   | %s    | 格式化字符串                       |
   | %d    | 格式化整数                         |
   | %o    | 格式化无符号八进制数               |
   | %x    | 格式化无符号十六进制数             |
   | %X    | 格式化无符号十六进制数（大写）     |
   | %f    | 格式化定点数，可指定小数点后的精度 |
   | %e    | 用科学计数法格式化定点数           |
   | %E    | 根据值的大小决定使用%f或者%e       |
   | %g    | 根据值的大小决定使用%F或者%E       |

2. 请问以下这行代码会打印什么内容？ 

   > \>>>"{{1}}".format("不打印", "打印") 

   '{1}'

3. 以下代码中，a, b, c是什么参数？ 

> \>>> "{a} love {b}.{c}".format(a="I", b="FishC", c="com") '
>
> 'I love FishC.com' 

关键字参数

4. 以下代码中，{0}, {1}, {2}是什么参数？ 

> \>>> "{0} love {1}.{2}".format("I", "FishC", "com") 
>
> 'I love FishC.com' 

位置参数

5. 如果想要显示Pi = 3.14，format前边的字符串应该怎么填写呢？ 

> ''.format('Pi = ', 3.1415) 

'{0}{1:.2f}'.format('Pi = ', 3.1415) 

### Practice 

1. 编写一个进制转换程序，程序演示如下（提示，十进制转换二进制可以用bin()这个BIF）： 

   ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly91cGxvYWQtaW1hZ2VzLmppYW5zaHUuaW8vdXBsb2FkX2ltYWdlcy8yMzA4NjI4Mi02NThjNjVjZWNiNzgxZTA2LnBuZw?x-oss-process=image/format,png)

```python
number = input('请输入一个整数（输入Q结束程序）：')

while True:
    if number == 'Q':
        print('程序结束')
        break
    elif number.isdigit():
        intnumber = int(number)
        print('{0}{1:#x}'.format('十进制 -> 十六进制：', intnumber))
        print('{0}{1:#o}'.format('十进制 -> 八进制：', intnumber))
        print('{0}{1:#b}'.format('十进制 -> 二进制：', intnumber))
        break
    else:
        number = input('输入错误，请重新输入一个整数（输入Q结束程序）：')
        continue
```





# 016. 序列！序列！

## 知识点

- 列表，元组和字符串的共同点

  - 都可以通过索引得到每一个元素
  - 默认索引值总是从0开始
  - 可以通过分片的方法得到一个范围内的元素的集合
  - 有很多共同的操作符（重复操作符，拼接操作符，成员关系操作符）

- 常用BIF

  - list(),  把一个可迭代器转换成列表

  - tuple(), 把一个可迭代器转换成元组

  - str(), 把obj对象转换成字符串

  - len(), 返回长度

  - max(), 返回序列或者参数集合中的最大值

  -  min(), 返回序列或者参数集合中的最小值

  - sum(iterable[, start=0]), 返回序列iterable 和可选参数start的总和

  - sorted(), 从小到大排序; list.sort()

  - reversed(), 返回迭代器对象；可以用list(迭代器对象)转换成列表

  - enumerate(), 生成由每个元素的index 值和元素值组成的元组； 返回迭代器对象；可以用list(迭代器对象)转换成列表

  - zip(a, b)， 成双成对打包

    ```python
    >>> a = list()
    >>> a
    []
    >>> 
    >>> b = 'I love fishC.com'
    >>> b = list(b)
    >>> 
    >>> b
    ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'f', 'i', 's', 'h', 'C', '.', 'c', 'o', 'm']
    >>> 
    >>> 
    >>> c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
    >>> 
    >>> c = list(c)
    >>> 
    >>> c
    [1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    >>> len(a)
    0
    >>> len(b)
    16
    >>> max(1, 2, 3, 4, 5)
    5
    >>> 
    >>> max(b)
    'v'
    >>> 
    >>> b
    ['I', ' ', 'l', 'o', 'v', 'e', ' ', 'f', 'i', 's', 'h', 'C', '.', 'c', 'o', 'm']
    >>> 
    >>> numbers = [1, 18, 13, 0, -98, 34, 54, 76, 32]
    >>> max(numbers)
    76
    >>> min(numbers)
    -98
    >>> chars = '123456789'
    >>> min(chars)
    '1'
    >>> 
    >>> tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    >>> 
    >>> max(tuple1)
    9
    >>> tuple2 = (3.1, 2.3, 3.4)
    >>> sum(tuple2)
    8.8
    >>> 
    >>> sum(numbers)
    130
    >>> sum(numbers, 8)
    138
    >>> chars
    '123456789'
    >>> sum(chars)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> sorted(numbers)
    [-98, 0, 1, 13, 18, 32, 34, 54, 76]
    
    >>> reversed(numbers)
    <list_reverseiterator object at 0x10495e2b0>
     
    >>> list(reversed(numbers))
    [32, 76, 54, 34, -98, 0, 13, 18, 1]
    >>> 
    >>> 
    >>> enumerate(numbers)
    <enumerate object at 0x104a0e4c0>
    >>> 
    >>> list(enumerate(numbers))
    [(0, 1), (1, 18), (2, 13), (3, 0), (4, -98), (5, 34), (6, 54), (7, 76), (8, 32)]
    >>> 
    >>> a = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> b = [4, 5, 6, 7]
    >>> zip(a, b)
    <zip object at 0x104a0e400>
    >>> 
    >>> list(zip(a, b))
    [(1, 4), (2, 5), (3, 6), (4, 7)]
    ```

    

## 课后作业

### Quiz

1. 我们根据列表、元祖和字符串的共同特点，把它们三统称为什么？

   序列 

2. 请问分别使用什么BIF，可以把一个可迭代对象转换为列表、元祖和字符串？ 

   list([iterable])

   tuple([iterable])

   str(obj)

3. 你还能复述出“迭代”的概念吗？

   所谓迭代，是重复反馈过程的活动，其目的通常是为了接近并到达所需的目标或结果。每一次对过程的重复被称为一次“迭代”，而每一次迭代得到的结果会被用来作为下一次迭代的初始值。

4. 你认为调用 max('I love FishC.com') 会返回什么值？为什么？ 

   'v', 因为字符串在计算机中是以ASCII码的形式存储（ASCII对照表：http://bbs.fishc.com/thread-41199-1-1.html），参数中ASCII码值最大的是'v'对应的118

5. 哎呀呀，现在的小屁孩太调皮了，邻居家的孩子淘气，把小甲鱼刚写好的代码画了个图案，麻烦各位鱼油恢复下啊，另外这家伙画的是神马吗？怎么那么眼熟啊！？？ 

   ![Alt](https://img-blog.csdnimg.cn/img_convert/b8487addfb00c4a6b7cad9c4b5f328f9.gif)



​		

```python
name = input("请输入待查找的用户名：")
score = [ ['迷途',  85], ['黑夜',  80], ['小布丁', 65], ['福禄娃娃', 95], ['怡静', 90]]
IsFind = False

for each in score:
    if name == each[0]:
        print(name + '的得分是：',  each[1])
        IsFind = True
        break
if not IsFind:
    print("查找的数据不存在！")
```



### Practice

1. 猜想一下 min() 这个BIF的实现过程 

   ```
   list1 = [3, 2, 332, 41, 532, 6]
   minvalue = list1[0]
   
   for each in list1:
       if each < minvalue:
           minvalue = each
   
   print(minvalue)
   ```

   

2. 视频中我们说 sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，请写出一个新的实现过程，自动“无视”参数里的字符串并返回正确的计算结果 

   ```python
   for each in list1:
       if isinstance(each, str):
           list1.remove(each)
   
   print(list1, '\n', sum(list1))
   ```

   

# 017. 函数：Python的乐高积木

## 知识点

```
>>> def MyFirstFunction():
...     print('这是我创建的第一个函数')
...     print('我表示很激动')
... 
>>> MyFirstFunction()
这是我创建的第一个函数
我表示很激动
```



- 先定义函数
- 执行函数时候，就是调用函数，向上面回找，依次执行函数体的内容
- 如果Python 向上找函数的时候，没有找到相应的函数名的定义过程，会报错



### 函数的参数

- Python 函数支持多个参数，但是尽量不用太多
- 函数要写好注释

```python
>>> def MySecondFunction(name):
...     print(name + 'I love You!' )
... 
>>>
>>> MySecondFunction()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: MySecondFunction() missing 1 required positional argument: 'name'
>>> 
>>> 
>>> MySecondFunction('小甲鱼')
小甲鱼I love You!

>>> def add(num1, num2):
...     result = num1 + num2
...     print(result)
... 
>>> 
>>> add(1, 2)
3

```

### 函数的返回值

- 采用关键字return

```
>>> def add(num1, num2):
...     return (num1 + num2)
... 
>>> 
>>> add(1, 2)
3
```



## 课后作业

### Quiz

1. 你有听说过DRY吗？ 

   DRY是程序员们公认的指导原则：Don't Repeat Yourself.

2. 都是重复一段代码，为什么我要使用函数（而不使用简单的拷贝黏贴）呢？ 

   - 维护效率高
   - 提高代码效率
   - 降低代码量
   - 易于阅读

3. 函数可以有多个参数吗？ 

   可以有多个参数

4. 创建函数使用什么关键字，要注意什么？ 

   使用“def”关键字，要注意函数名后边要加上小括号“()”，然后小括号后边是冒号“:”，然后缩进部分均属于函数体的内容

   

5. 请问这个函数有多少个参数？ 

   ```python
   def MyFun((x, y), (a, b)):
     return x * y - a * b
   ```

   0，因为类似于这样的写法是错误的！我们分析下，函数的参数需要的是变量，而这里你试图用“元祖”的形式来传递是不可行的。

6. 请问调用以下这个函数会打印什么内容？ 

   ```python
   def hello():
     print('Hello World!') 
     return
   	print('Welcome To FishC.com!')
   ```

   会打印‘Hello World!’。因为return会结束函数的执行。

### Practice

1. 编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。 

   ```python
   def power(x, y):
       if y == 0:
           return 1
       elif y > 0:
           if y == 1:
               return x
           else:
               result = x
               for i in range(y-1):
                   result *= x
               return result
       else:
           if y == -1:
               return 1/x
           else:
               result = x
               for i in range((-y-1)):
                   result *= x
               return 1/result
   
   print(power(2, -2))
   ```

   

2. 编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。 

   ```python
   def gcder(a, b):
       flag = a % b
       result = b
       while flag != 0:
           flag = a % b
           result = b
           a = b
           b = flag
       return result
   
   print(gcder(121, 11))
   ```

   

3. 编写一个将十进制转换为二进制的函数，要求采用“除2取余”（脑补链接）的方式，结果与调用bin()一样返回字符串形式。 

   ```python
   def biner(x):
       binarylist = []
       while x != 0:
           flag = str(x % 2)
           binarylist.insert(0, flag)
           x = x // 2
       # 将列表或元组转换成字符串的方法：''.join(object)
       return ''.join(binarylist)
   
   print(biner(4))
   ```

   

# 018. 函数：灵活即强大

## 知识点

### 形参和实参

- `\>>> def MySecondFunction(name):` 函数定义过程中的name是叫形参， # 因为它只是一个形式，表示占据一个位置
- `\>>> MySecondFunction('小甲鱼')` ：传递进来的小甲鱼叫做实参，因为它是具体的参数值

### 函数文档

- 系统默认特殊属性： `.__doc__`

- 利用函数文档，对函数的内容，参数，意义以及返回值有一个介绍，让别人可以理解使用

  ```python
  >>> def MyFirstFunction(name):
  ...     '函数定义过程中的name是叫形参'
  ...     #因为它只是一个形式，表示占据一个参数位置
  ...     print('传递进来的' + name + '叫做实参，因为它是具体的参数值！')
  ... 
  >>> 
  >>> MyFirstFunction('小甲鱼')
  传递进来的小甲鱼叫做实参，因为它是具体的参数值！
  >>> 
  >>> MyFirstFunction.__doc__
  '函数定义过程中的name是叫形参'
  >>> 
  >>> 
  >>> print.__doc__
  "print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
  >>> 
  ```

### 关键字参数

- 利用关键字匹配参数，可以避免搞不清楚顺序按照位置匹配引起的问题

  ```python
  >>> def SaySome(name, words):
  ...     print(name + '->' + words)
  ... 
  >>> SaySome('小甲鱼', '让编程改变世界')
  小甲鱼->让编程改变世界
  >>> 
  >>> SaySome('让编程改变世界', '小甲')
  让编程改变世界->小甲
  >>> SaySome(words='让编程改变世界', name='小甲鱼')
  小甲鱼->让编程改变世界
  ```

  

### 默认参数

- 在参数定义的过程中，为形参赋初始值

  ```python
  >>> def SaySome(name='小甲鱼', words='让编程改变世界'):
  ...     print(name + '->' + words)
  ... 
  >>> 
  >>> 
  >>> SaySome()
  小甲鱼->让编程改变世界
  >>> 
  >>> 
  >>> SaySome('默默')
  默默->让编程改变世界
  >>> 
  >>> SaySome('默默', '你好')
  默默->你
  ```

### 收集参数

- 可变参数，原因是函数的作者有时候也搞不清楚到底需要多少个参数

- 在参数前面加上*号即可

- Python 把标识为收集参数的参数用一个元组打包起来

  ```python
  >>> def test(*params):
  ...     print('参数的长度是', len(params))
  ...     print('第二个参数是', params[1])
  ... 
  >>> 
  >>> 
  >>> test(1, '小鲫鱼', 3, 5, 7)
  参数的长度是 5
  第二个参数是 小鲫鱼
  ```

- 如果除了收集参数，还有其他定制参数，需要使用关键字参数来定制，不然会报错

  ```python
  >>> def test(*params, exp):
  ...     print('参数的长度是', len(params), exp)
  ...     print('第二个参数是', params[1])
  ... 
  >>> 
  >>> 
  >>> test(1, '小鲫鱼', 3, 5, 7)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: test() missing 1 required keyword-only argument: 'exp'
  >>> 
  >>> 
  >>> test(1, '小鲫鱼', 3, 5, 7, exp=8)
  参数的长度是 5 8
  第二个参数是 小鲫鱼
  ```

  

## 课后作业

### Quiz

1. 请问以下哪个是形参哪个是实参？

   ```python
   def MyFun(x):
   	return x ** 3
   y = 3
   print(MyFun(y))
   ```

   x 是形参，y 是实参；形参指的是函数定义过程中，小括号里面的参数；实参指的是函数调用过程中传递进去的参数

2. 函数文档和直接用“#”为函数写注释有什么不同

   函数文档会保存在内置函数：`__doc__` ，可以通过 `help()` 或者 `.__doc__`  来查看

3. 使用关键字参数，可以有效避免什么问题的出现呢？

   可以避免忘记参数位置导致传入的实参不匹配的问题

4. 使用help(print)查看print()这个BIF有哪些默认参数？分别起到什么作用？

   `print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)`

   

5. 默认参数和关键字参数表面最大的区别是什么

   默认参数会默认指定一个值，如果没有传入任何实参的时候，会使用默认值

### Practice

1. 编写一个符合以下要求的函数：

   a. 计算打印所有参数的和乘以基数（base=3）的结果

   b. 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算

   ```python
   # 编写一个符合以下要求的函数：
   # a. 计算打印所有参数的和乘以基数（base=3）的结果
   # b. 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算
   
   def practice1(*pram, base=3):
       return sum(pram)*base
   
   
   print(practice1(1, 3, 4))
   print(practice1(1, 3, 4,  base=5))
   ```

   

2. 寻找水仙花数

   题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。

   ```python
   # 寻找水仙花数
   # 题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。
   
   def narcissistic():
       for i in range(100, 1000):
           x = i // 100
           y = (i // 10) % 10
           z = i % 10
           if i == pow(x, 3) + pow(y, 3) + pow(z, 3):
               print('narcissistic number: %d' % i)
   
   
   narcissistic()
   ```

   

3. 编写一个函数 findstr()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。例如：假定输入的字符串为“You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.”，子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。

   ```python
   # 编写一个函数 findstr()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
   # 例如：假定输入的字符串为
   # “You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.”，
   # 子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。
   
   def findstr(x, y):
       a = y[0]
       b = y[1]
       count = 0
       xlen = len(x)
       for i in range(xlen):
           if x[i] == a and x[i+1] == b:
               count += 1
       print(count)
   
   
   findstr('You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.', 'im')
   ```

   

# 019. 函数：我的地盘听我的

## 知识点

### 函数和过程

- 函数是有返回值的

- 过程是简单的，特殊的，没有返回值的

- Python 只有函数，没有过程。Python的所有函数都是有返回的，有返回值就返回值，没有返回值就返回None

  ```python
  >>> def hello():
  ...     print('hello, fishC!')
  ... 
  >>> temp = hello()
  hello, fishC!
  >>> 
  >>> temp
  >>> 
  >>> type(temp)
  <class 'NoneType'>
  ```

### 再谈谈返回值

- Python 动态确定类型，不需要提前定义

- Python是没有变量的，只有名字

- Python 是可以返回多个返回值的

  ```python
  >>> def back():
  ...     return[1, '小甲鱼', 3.14]
  ... 
  >>> back()
  [1, '小甲鱼', 3.14]
  >>> 
  >>> 
  >>> 
  >>> def back():
  ...     return 1, '小甲鱼', 3.14
  ... 
  >>> back()
  (1, '小甲鱼', 3.14)
  ```



### 我的地盘听我的 - 局部和全局变量

- **局部变量**： 作用域范围在函数内，在外面调用会出错；Python 在调用函数时，利用栈来存储函数所需要的代码和局部变量，当执行完函数，函数的栈会自动清空，所以函数执行完之后再试图访问函数体内的变量会出错

  ```python
  def discounts(price, rate):
      final_price = price * rate
      return final_price
  
  
  old_price = float(input('请输入原价：'))
  rate = float(input('请输入折扣率：'))
  new_price = discounts(old_price, rate)
  print('打折扣价格是：', new_price)
  
  # 试图打印局部变量：final_price 会报错
  print('试图打印局部变量final_price', final_price)
  ```

  ```python
  请输入原价：12
  请输入折扣率：0.3
  打折扣价格是： 3.5999999999999996
  Traceback (most recent call last):
    File "/Users/felix_yang/PycharmProjects/learningpython/19/test01.py", line 15, in <module>
      print('试图打印局部变量final_price', final_price)
  NameError: name 'final_price' is not defined
  ```

- **全局变量**：拥有更大的作用域，他们的作用域是整个代码段。那如果在函数体内部访问全局变量是不是可以呢？

  ```python
  def discounts(price, rate):
      final_price = price * rate
    
      # 试图打印全局变量: old_price 不会报错
      print('试图打印全局变量old_price', old_price)
      
      return final_price
  
  
  old_price = float(input('请输入原价：'))
  rate = float(input('请输入折扣率：'))
  new_price = discounts(old_price, rate)
  
  print('打折扣价格是：', new_price)
  ```

  ```python
  请输入原价：12
  请输入折扣率：0.4
  试图打印全局变量old_price 12.0
  打折扣价格是： 4.800000000000001
  ```

  ***不要试图在函数内不修改全局变量，因为那样的话，python 会试图在函数内部创建一个名字一样的局部变量存储在函数的栈当中***

  

## 课后作业

### Quiz

1. 下边程序会输出什么？

   ```python
   def next():  
       print('我在next()函数里...')  
       pre()  
     
   def pre():  
       print('我在pre()函数里...')  
     
   next()
   ```

   我在next()函数里...

   我在pre()函数里...

2. 请问以下这个函数有返回值吗？

   ```python
   def hello():  
       print('Hello FishC!') 
   ```

   有，返回值是none



3. 请问Python的return语句可以返回多个不同类型的值吗？

   可以，可以return 列表，或者元组，把不同类型的值放到列表/元组中返回

   

4. 请目测以下程序会打印什么内容？

   ```python
   def fun(var):  
       var = 1314  
       print(var, end = '')  
     
   var = 520  
   fun(var)  
   print(var) 
   ```

   *1314520*

   第一个打印出来的是函数体内的局部变量（名字也叫var），第二个打印出来的是定义在函数之外的全局变量var

5. 目测以下程序会打印什么内容？

   ```
   var = 'Hi'  
     
   def fun1():  
       global var  
       var = ' Baby '  
       return fun2(var)  
     
   def fun2(var):  
       var += 'I love you'  
       fun3(var)  
       return var  
     
   def fun3(var):  
       var = ' 小甲鱼 '  
     
   print(fun1())
   ```

   Baby I love you





### Practice

1. 编写一个函数，判断传入的字符串参数是否为“回文联”

   ```python
   # 编写一个函数，判断传入的字符串参数是否为“回文联”
   
   # list的reverse()方法是返回None的，只会对列表内的元素逆序排序。而string的reserved()方法是会返回逆序后的字符串的
   
   def check(var):
       list1 = list(var)
       list2 = list1[:]
       list2.reverse()
   
       if list1 == list2:
           print('传入的参数 %s 是：回文联' % var)
       else:
           print('传入的参数 %s 不是：回文联' % var)
   
   
   check('1234321')
   ```

   

2. 编写一个函数，分别统计传入字符串参数（可能不止一个参数）的英文字母、空格、数字和其它字符的个数。

   ```python
   # 编写一个函数，分别统计传入字符串参数（可能不止一个参数）的英文字母、空格、数字和其它字符的个数。
   
   # 单个参数的情况
   def count_str(var):
       str_count = 0
       space_count = 0
       number_count = 0
       other_count = 0
   
       for i in var:
           if i.isdigit():
               number_count += 1
           elif i.isalpha():
               str_count += 1
           elif i.isspace():
               space_count += 1
           else:
               other_count += 1
   
       print('英文字母个数是：%d' % str_count)
       print('数字个数是：%d' % number_count)
       print('空格个数是：%d' % space_count)
       print('其他字符个数是：%d' % other_count)
   
   
   count_str('12d99  safe')
   ```

   ```python
   # 编写一个函数，分别统计传入字符串参数（可能不止一个参数）的英文字母、空格、数字和其它字符的个数。
   
   # 多个参数的情况
   
   def count_str(*param):
       var_number = len(param)
       for i in range(var_number):
           str_count = 0
           space_count = 0
           number_count = 0
           other_count = 0
           for each in param[i]:
               if each.isdigit():
                   number_count += 1
               elif each.isalpha():
                   str_count += 1
               elif each.isspace():
                   space_count += 1
               else:
                   other_count += 1
           print('第 %d 个参数有 %d 英文字母，%d 数字， %d 空格， %d 其他字符' % (i, str_count, number_count, space_count, other_count))
   
   
   count_str('1fe', '1ssssf sfe')
   ```

   

# 020. 函数：内嵌函数和闭包

## 知识点

### 全局Global 关键字

- 上节课提到不要试图去修改全局变量，python 会使用shadowing 的机制防止全局变量被修改

  ```python
  >>> count = 5
  >>> def MyFun():
  ...     count = 10
  ...     print(count)
  ... 
  >>> MyFun()
  10
  >>> print(count)
  5
  ```

- 如果非要修改，可以使用global 关键字，把想要变成全局变量的局部变量变成全局变量

  ```python
  >>> def MyFun():
  ...     global count
  ...     count = 10
  ...     print(count)
  ... 
  >>> MyFun()
  10
  >>> 
  >>> print(count)
  10
  ```



### 内嵌函数

- python 是支持函数嵌套的，先看一个例子。注意嵌套里面的函数无法在外面调用。

  ```python
  >>> def fun1():
  ...     print('fun1 is being called')
  ...     def fun2():
  ...             print('fun2 is being called')
  ...     fun2()
  ... 
  >>> fun1()
  fun1 is being called
  fun2 is being called
  ```

### 闭包

- 闭包是一种编程范式；其他的编程范式有：面向对象编程，面向过程编程，这些都是对代码的抽象和概括，使得代码的可用性和重用性变高

- 如果在一个内部函数里，对在外部作用域的变量（不是全局作用域的变量）进行引用，那么这个内部函数就是一个闭包

  ```python
  >>> def FunX(x):
  ...     def FunY(y):
  ...             return x * y
  ...     return FunY
  ... 
  >>> i = FunX(8)
  >>> i
  <function FunX.<locals>.FunY at 0x103343040>
  >>> 
  >>> 
  >>> type(i)
  <class 'function'>
  >>> 
  >>> i(5)
  40
  >>> 
  >>> FunX(8)(5)
  40
  >>> 
  >>> FunY(5)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'FunY' is not defined
  ```

- 因为闭包的概念是由内嵌函数演变而来， 所以也不能从外部函数的外面调用内部函数

- 在内部函数中只能对外部作用域的变量进行引用，不能修改，如果修改的话，这个变量同样会被shadowing，python 会在内部函数创建一个同名的内部作用域变量。以下例子显示了新建的内部作用域变量由于未被事先定义而报错

  ```python
  >>> def Fun1():
  ...     x = 5
  ...     def Fun2():
  ...             x *= x
  ...             return x
  ...     return Fun2()
  ... 
  >>> 
  >>> Fun1()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 6, in Fun1
    File "<stdin>", line 4, in Fun2
  UnboundLocalError: local variable 'x' referenced before assignment
  ```

  - 有没有解决的办法呢？Python3 之前没有解决办法，只有通过容器类型来解决，比如列表，因为不会存储在栈里面，不会报错

    ```python
    >>> def Fun1():
    ...     x = [5]
    ...     def Fun2():
    ...             x[0] *= x[0]
    ...             return x[0]
    ...     return Fun2()
    ... 
    >>> 
    >>> Fun1()
    25
    ```

  

  - Python3 开始，可以通过***nonlocal*** 关键字来解决，类似于***global*** 关键字

    ```python
    >>> def Fun1():
    ...     x = 5
    ...     def Fun2():
    ...             nonlocal x
    ...             x *= x
    ...             return x
    ...     return Fun2()
    ... 
    >>> 
    >>> Fun1()
    25
    ```




### 闭包在实际开发中的作用

- 闭包的实际应用，主要是用来封装变量。即把变量隐藏起来，不让外面拿到和修改。

  ```
  闭包就是能够读取其他函数内部变量的函数，说白了闭包就是个函数，只不过是处于其他函数内部而已。
  
  由于在python中，只有函数内部的子函数才能读取局部变量，所以说，闭包可以简单理解成“定义在一个函数内部的函数“。
  
  所以，在本质上，闭包是将函数内部和函数外部连接起来的桥梁。
  
  知乎大神说：闭包是指在 JavaScript 中，内部函数总是可以访问其所在的外部函数中声明的参数和变量，即使在其外部函数被返回（寿命终结）了之后。
  
  二：用途是什么?
  
  1.访问函数内部的变量
  
  2.防止函数内部的变量执行完城后，被销毁，使其一直保存在内存中。
  ```

## 课后作业

### Quiz

1. 如果希望在函数中修改全局变量的值，应该使用什么关键字？

   global

2. 在嵌套函数中，如果希望在内部函数修改外部函数的局部变量，应该是用什么关键字？

   nonlocal

3. Python的函数可以嵌套，但是要注意访问的作用域问题，请问以下代码存在什么问题呢？

   ```python
      def outside():
            print('I am outside!')
            def inside():
                  print('I am inside!')
   
      inside()
   ```

   不能直接访问嵌套内函数，只能访问outside()

4. 请问为什么代码A没有报错，但是代码B却报错了？应该如何修改？

   代码A：

   ```python
   1 def outside():
   2     var = 5
   3     def inside():
   4         var = 3
   5         print(var )
   6     inside()
   7 outside()
   ```

    

   代码B：

   ```python
   1 def outside():
   2     var = 5
   3     def inside():
   4         print(var )
   5         var = 3
   6     inside()
   7 outside()
   ```

   在内部函数中只能对外部作用域的变量进行引用，不能修改，如果修改的话，这个变量同样会被shadowing，python 会在内部函数创建一个同名的内部作用域变量。代码B 新建的内部作用域变量var 由于未被事先定义而被打印：print(var) 而报错。而代码A 已经事先定义： var=3，所以不会报错

5. 请问如何访问FunIn()呢？

   ```python
   1 def funOut():
   2     def funIn():
   3         print("宾果！恭喜成功访问到啦~")
   4     return funIn()
   ```

   funOut()

6. 请问如何访问FunIn()呢？

   ```python
   1 def funOut():
   2     def funIn():
   3         print("宾果！恭喜成功访问到啦~")
   4     return funIn
   ```

​		funOut()() 

​		或者

​		a = funOut()

​		a()

7. 以下是“闭包”的一个例子，请你目测下会打印什么内容？

   ```
    1 def funX():
    2     x=5
    3     def funY():
    4         nonlocal  x
    5         x+=1
    6         return x
    7     return funY
    8 a=funX()
    9 print(a())
   10 print(a())
   11 print(a())
   ```
   
   6
   
   7
   
   8
   
   大家可能会迷惑，这。。。怎么跟全局变量一样了？局部变量x不是应该再每次调用的时候都重新初始化了吗？！
   
   其实大家自己看看就明白了，当a = funX()，只要a变量没有被重新赋值，funX()就没有被释放，也就是说局部变量x就没有被重新初始化。
   
   所以当全局变量不适用的时候，可以考虑使用闭包更稳定和安全

​		



### Practice

1. 统计下边这个长字符串中各个字符出现的次数并找到小甲鱼送给大家的一句话

   [string1.txt](https://github.com/felixyh/learningpython/blob/main/20/string1.txt)

   ```python
   def count_str(x):
       temp_list = []
       temp_number = []
       lenth = len(x)
   
       def show():
           for i in range(lenth):
               current_char = x[i]
               if current_char not in temp_list:
                   temp_list.append(current_char)
                   temp_number.append(x.count(current_char))
           final_list = list(zip(temp_list, temp_number))
           print(final_list)
           # print('字符 %s 的数量是：%d' % (current, number))
       return show()
   
   
   count_str(string1)
   ```

   `[('%', 6104), ('$', 6046), ('@', 6157), ('_', 6112), ('^', 6030), ('#', 6115), (')', 6186), ('&', 6043), ('!', 6079), ('+', 6066), (']', 6152), ('*', 6034), ('}', 6105), ('[', 6108), ('(', 6154), ('{', 6046), ('\n', 1219), ('G', 1), ('O', 2), ('D', 1), ('L', 1), ('U', 1), ('C', 1), ('K', 1)]`

   GOODLUCK

2. 请用已经学过的知识编写程序，找出小甲鱼藏在下边这个长字符串中的密码，密码的埋藏点符合以下规律：

   [string2.txt](https://github.com/felixyh/learningpython/blob/main/20/string2.txt)

   - 每位密码为单个小写字母
   - 每位密码的左右两边均有且只有三个大写字母
   
   ```python
   def find_pass(x):
       str_length = len(x) - 9
       pass_list = ''
   
       def show_pass():
           # 指定pass_list 为nonlocal，因为需要从闭包函数里面调用修改
           nonlocal pass_list
   
           # 判断第一个password 字符，其实是从第4个字符开始： xxx[]xxxx，前后3个字符都是大写字母，第8个字符是小写
           if x[:3].isupper() and x[4:7].isupper() and (x[3]+x[7]).islower() and x[:7].isalpha():
               pass_list += x[3]
   
           # 每次截取9个字符放到temp_string，判断中间的一个字符和两头的字符是小写，前后3个字符为大写
           for i in range(str_length):
               temp_string = x[i:i+9]
               temp_low = temp_string[0] + temp_string[4] + temp_string[-1]
               temp_up = temp_string[1:4] + temp_string[-4:-1]
               if temp_low.islower() and temp_up.isupper() and (temp_up + temp_string[4]).isalpha():
                   pass_list += temp_string[4]
   
           # 判断最后一个password 字符，其实是从倒数第4个字符开始： xxxx[]xxx，前后3个字符都是大写字母，倒数第8个字符是小写
           if x[-7:-4].isupper() and x[-3:].isupper() and (x[-4]+x[-7]).islower() and x[-7:].isalpha():
               pass_list += x[-4]
   
           print(pass_list)
   
       return show_pass()
   
   
   find_pass(string2)
   ```
   
   

# 021. 函数：Lambda表达式

## 知识点

### 匿名函数Lambda

- Lambda 表达式用冒号分隔，冒号前面是参数，后面是函数体内容

- 先举一个例子 - 1 个参数

  ```python
  >>> def ds(x):
  ...     return 2 * x + 1
  ... 
  >>> ds(5)
  11
  >>> 
  >>> 
  >>> 
  >>> lambda x : 2 * x + 1
  <function <lambda> at 0x1033431f0>
  >>> g = lambda x : 2 * x + 1
  >>> 
  >>> g(5)
  11
  ```

- 再举一个例子 - 2个参数

  ```python
  >>> def add(x, y):
  ...     return x + y
  ... 
  >>> add(3, 4)
  7
  >>> 
  >>> lambda x, y : x + y
  <function <lambda> at 0x103343310>
  >>> 
  >>> g = lambda x, y : x + y
  >>> g(3, 4)
  7
  ```

### Lambda 表达式的作用

- Python写一些执行脚本的时候，使用lambda就可以省下定义函数的过程，比如说我们只是需要写个简单的脚本来管理服务器时间，我们就不需要专门定义一个函数然后再写调用，使用lambda可以使得代码更加精简。
- 对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，有时候给函数起个名字是比较头疼的问题，使用lambda就不需要考虑命名的问题了。
- 简化代码的可读性，由于普通屌丝函数阅读经常要跳到开头def 定义部分，使用lambda函数可以省去这样的步骤

### 两个比较牛逼的BIF

- filter() : 

  - filter(function or None, iterable)

  - Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true. (如果第一个参数是函数，返回一个迭代器，返回iterable中function(item)为true的元素;   如果第一个参数是none，返回值为true的item)

    举例：如果第一个参数为函数：

    ```python
    >>> def odd(x):
    ...     return x % 2
    ... 
    >>> temp = range(10)
    >>> show = filter(odd, temp)
    >>> list(show)
    [1, 3, 5, 7, 9]
    ```

    用lambda 实现

    ```python
    >>> show = filter(lambda x : x % 2, range(10))
    >>> list(show)
    [1, 3, 5, 7, 9]
    ```

    举例：如果第一个参数为None：

    ```python
    >>> filter(None, [1, 0, False, True])
    <filter object at 0x103325730>
    >>> 
    >>> list(filter(None, [1, 0, False, True]))
    [1, True]
    ```

    

- map()

  - map(func, *iterables)  第一个参数是函数，后面的参数是一个或者多个序列

  - Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted. (使用每个可迭代对象的参数计算函数，来创建一个迭代器，当最短的可迭代对象耗尽时停止。)

    举例：一个序列

    ```python
    >>> list(map(lambda x : x * 2, range(10)))
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    ```

    举例：多个序列

    ```python
    >>> list(map(lambda x, y : x * y, range(10), range(5)))
    [0, 1, 4, 9, 16]
    ```

    

## 课后作业

### Quiz

1. 请使用lambda表达式将下边函数转变为匿名函数？

   ```
   def fun_A(x,y=3):
       return x*y
   ```

   ```python
   lambda x, y=3 : x * y
   ```

   

2. 请将下边的匿名函数转变为普通的屌丝函数？

   ```python
   lambda x: x if x % 2 else None
   ```

   ```python
   def ds(x):
   		if x % 2:
   				return x
   		else:
   				return None
   ```

   

3. 感受一下使用匿名函数后给你的编程生活带来的变化？

   不用为起函数名而烦恼了

4. 你可以利用filter()和lambda表达式快速求出100以内所有3的倍数吗？

   ```python
   >>> list(filter(lambda x : not( x % 3 ), range(100)))
   [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
   ```

5. 还记得列表推导式吗？完全可以使用列表推导式代替filter()和lambda组合，你可以做到吗？

   ```python
   >>> [ x for x in range(100) if x % 3 == 0 ]
   [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
   ```

   

6. 还记得zip吗？使用zip会将两数以元祖的形式绑定在一块，例如：

   ```
   >>> list(zip([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
   [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
   ```

   但如果我希望打包的形式是灵活多变的列表而不是元祖（希望是[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]这种形式），你能做到吗？（采用map和lambda表达式）

   ```python
   >>> list(map(lambda x, y :  [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10] ))
   [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
   ```

   

7. 请目测以下表达式会打印什么？

   ```python
   def make_repeat(n):
       return lambda s: s * n
   double = make_repeat(2)
   print(double(8))
   print(double('FishC'))
   ```

   ```undefined
   16
   FishCFishC
   ```

### Practice





# 022. 函数：递归是神马？

## 知识点

递归其实就是函数调用自己

- 汉诺塔游戏： 使用递归会比迭代更好
- 树结构的定义： 使用递归定义结构体会比其他方法容易很多
- 谢尔宾斯基三角形：递归组成的图案
- 女神自拍

### 一个递归的例子

- 写一个求阶乘的函数

  - 正整数阶乘指从1乘以2乘以3乘以4一直乘到所要求的数
  - 例如所给的数是5，则阶乘式是1x2x3x4x5，得到的积是120，所以120就是5的阶乘

  1. 非递归版本范例：

     ```python
     def factorial(x):
         result = x
         for n in range(1, x):
             result *= n
         return result
     
     
     number = int(input('please input a number:'))
     final_result = factorial(number)
     print(final_result)
     ```

     

  2. 递归版本范例

     ```python
     def factorial(n):
         if n == 1:
             return 1
         else:
             return n * factorial(n-1)
     
     
     number = int(input('please input a number:'))
     final_result = factorial(number)
     print(final_result)
     ```

     ![image-20220509110226777](/Users/felix_yang/Library/Application Support/typora-user-images/image-20220509110226777.png)



## 课后作业

### Quiz

1. 递归在编程上的形式是如何表现的呢？

   函数自己调用自己

   ```python
   def fun():
   	return fun()
   ```

   不过这样是不行的，因为没有停止条件，IDLE会一直报错，直到你按下Ctlr + C。python3默认递归的深度是100层，可以通过以下代码修改：

   ```python
   >>> import sys
   >>> sys.setrecursionlimit(1000)
   ```

2. 递归必须满足哪两个基本条件？

   递和归，调用自身，有停止条件。

3. 思考一下，按照递归的特性，在编程中有没有不得不使用递归的情况？

   例如汉诺塔，目录索引（因为你不知道目录里是否还有目录），树结构的定义等

4. 用递归去计算阶乘问题或斐波那契数列是很糟糕的算法，你知道为什么吗？

   因为递归是函数调用自身，每一次调用都要进行压栈和出栈，需要很多时间和内存资源。

5. 请聊一聊递归的优缺点（无需官方陈词，想到什么写什么就可以）

   优点：可以使代码简洁；在解决一些问题，如汉诺塔问题时比较方便
   缺点：使用上需要谨慎，因为会占用大量时间和资源；还有可能因为停止条件设置不合适而导致内存爆满。

6. 拿手机拍一张“递归自拍照片”

   拍这个的话需要两面镜子，那会是一个没有停止条件的递归，无限循环反射下去。



### Practice

1. 使用递归编写一个power()函数内建函数pow()，即power(x,y)为计算并返回x的y次幂的值。

   ```python
   # 使用递归编写一个power()函数内建函数pow()，即power(x,y)为计算并返回x的y次幂的值。
   
   
   def power(x, y):
       if y == 1:
           return x
       elif y == 0:
           return 1
       else:
           return x * power(x, y-1)
   
   
   print(power(2, 10))
   ```

2. 使用递归编写一个函数，利用欧几里得算法求最大公约数，例如gcd(x,y)返回值为参数x和参数y的最大公约数。

   ```python
   # 使用递归编写一个函数，利用欧几里得算法求最大公约数，例如gcd(x,y)返回值为参数x和参数y的最大公约数。
   
   def gcder(x, y):
       if x % y == 0:
           return y
       else:
           return gcder(y, x % y)
   
   
   print(gcder(9, 6))
   ```





# 023. 递归：这帮小兔崽子

## 知识点

### 斐波那契数列

![image-20220513210700654](/Users/felix_yang/Library/Application Support/typora-user-images/image-20220513210700654.png)



- 递归算法 - 思路清晰，但是耗费资源

  ```python
  def fibonacci(n):
      if n == 1 or n == 2:
          return 1
      elif n < 1:
          return -1
      else:
          return fibonacci(n-1) + fibonacci(n-2)
  
  
  n = input('please input a number:')
  result = fibonacci(int(n))
  if result != -1:
      print(result)
  ```

  

- 迭代算法

  ```python
  def fibonacci(n):
      n1 = 1
      n2 = 1
  
      if n < 1:
          print('The number is incorrect')
  
      elif n == 1 or n == 2:
          return 1
      else:
          while (n-2) > 0:
              n3 = n1 + n2
              n1 = n2
              n2 = n3
              n -= 1
          return n3
  
  
  n = int(input('please input a number:'))
  result = fibonacci(n)
  print(result)
  ```

  



# 024. 递归：汉诺塔

## 知识点

<img src="/Users/felix_yang/Library/Application Support/typora-user-images/image-20220515204116145.png" alt="image-20220515204116145" style="zoom:50%;" />

<img src="/Users/felix_yang/Library/Application Support/typora-user-images/image-20220516082730879.png" alt="image-20220516082730879" style="zoom:50%;" />

<img src="/Users/felix_yang/Library/Application Support/typora-user-images/image-20220516082806121.png" alt="image-20220516082806121" style="zoom:50%;" />



```
In [1]: def hanoi(n, x, y, z):
   ...:     if n == 1:
   ...:         print(x, '--->', z)
   ...:     else:
   ...:         hanoi(n-1, x, z, y)
   ...:         print(x, '--->', z)
   ...:         hanoi(n-1, y, x, z)
   ...: 


In [2]: n = int(input('please input the hanoi levels:'))
please input the hanoi levels:3

In [3]: hanoi(n, 'x', 'y', 'z')
x ---> z
x ---> y
z ---> y
x ---> z
y ---> x
y ---> z
x ---> z
```



## 课后作业

### Quiz



### Practice

1. 使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）
   $$
   b = f(x) = \left\{
     \begin{array}{lr}
       1 & : x = 1\\
       f( x // 2) \Join x \% 2 & : x > 1
     \end{array}
   \right.
   $$

   $$
   \Join 表示拼接；
   公式的意思是：如果十进制正整数 x 等于 1，那它对应的二进制 b 就是 1；
   否则 x 大于 1，那它的二进制就是 d 整除 2 的商对应的二进制，拼接 x 整除 2 的余数。
   $$

   

   ```python
   # 使用递归编写一个十进制转换为二进制的函数（要求采用“取2取余”的方式，结果与调用bin()一样返回字符串形式）
   
   
   def bin_recursion(n):
       if n == 1:
           return 1
       else:
           return str(bin_recursion(n // 2)) + str(n % 2)
   
   
   print(bin_recursion(8))
   ```

   

2. 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==> [1, 2, 3, 4, 5] 

   
   $$
   b = f(x) = \left\{  \begin{array}{lr}
   [ ] & : x = 0 \\    
   [f( x // 10) , x \% 10 ]& : x > 0  
   \end{array}\right.
   $$

   ```python
   # 写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==> [1, 2, 3, 4, 5]
   
   
   def get_digits(n):
       result = []
       if n == 0:
           return []
       else:
           result.extend(get_digits(n // 10))
           result.append(n % 10)
           return result
   
   
   print(get_digits(12342321421321))
   ```

   

3. 还记得求回文字符串那道题吗？现在让你使用递归的方式来求解，亲还能骄傲的说我可以吗   

4. 使用递归编程求解以下问题： 

   有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？ 
   
   ```python
   # 使用递归编程求解以下问题：
   #
   # 有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
   
   
   def age(n):
       if n == 1:
           return 10
       else:
           return age(n-1) + 2
   
   
   print(age(5))
   ```
   
   

# 025. 字典：当索引不好用时

## 知识点

### 字典概念

- Python的字典，key-value，也称为HASH，关系数组

- 映射类型区别于序列类型，通过数组的形式进行存储的，通过索引进行存取

  ```python
  In [9]: brand = ['李宁', '耐克', '阿迪达斯', '鱼C 工作室']
  
  In [10]: slogan = ['一切皆有可能', 'Just Do It', 'Impossible is nothing', '让编程改变世界']
  
  In [11]: print('鱼C 工作室的口号是：', slogan[brand.index('鱼C 工作室')])
  鱼C 工作室的口号是： 让编程改变世界
  ```

- 创建和访问字典

  ```python
  In [12]: dict1 = {'李宁':'一切皆有可能', '耐克':'Just Do It', '阿迪达斯':'Impossible is nothing', '鱼C 工作室':'让编程改变世界'}
  
  In [13]: print('鱼C 工作室的口号是：', dict1['鱼C 工作室'])
  鱼C 工作室的口号是： 让编程改变世界
  
  In [14]: dict2 = {1:'one', 2:'two', 3:'three'}
  
  In [15]: dict2
  Out[15]: {1: 'one', 2: 'two', 3: 'three'}
  
  In [16]: dict2[2]
  Out[16]: 'two'
  
  In [17]: dict3 = {}
  
  In [18]: dict3
  Out[18]: {}
  ```

  

  - dict() 工厂函数 创建字典

    > 工厂函数看上去有点像函数，实质上他们是类，当你调用他们时，实际上是生成了该类型的一个实例，就像工厂生产货物一样，常见的工厂函数有：list(), tuple(), dict(), int(), float()

    ```python
    In [19]: dict3 = dict((('F', 70), ('i', 105), ('h', 104), ('c', 67)))
    
    In [20]: dict3
    Out[20]: {'F': 70, 'i': 105, 'h': 104, 'c': 67}
    ```

  - 关键字参数创建字典

    ```python
    In [25]: dict4 = dict(李宁='一切皆有可能', 耐克='Just Do It')
    
    In [26]: dict4
    Out[26]: {'李宁': '一切皆有可能', '耐克': 'Just Do It'}
    ```

  - 直接给字典的键赋值，如果这个键不存在，会直接创建这个键

    ```python
    In [29]: dict4['阿迪达斯'] = 'Impossible is nothing'
    
    In [30]: dict4
    Out[30]: {'李宁': '一切皆有可能', '耐克': 'Just Do It', '阿迪达斯': 'Impossible is nothing'}
    ```

  

### 字典常用内建方法

> clear()   fromkeys()  items()   pop()    setdefault() values()   
>
> ​        copy()    get()    keys()    popitem()  update()





## 课后作业

### Quiz

1. 当你听到小伙伴们在谈论“映射”、“哈希”、“散列”或者“关系数组”的时候，事实上他们就是在讨论什么呢

   字典

2. 尝试一下将数据（‘F’: 70, ‘C’: 67, ‘h’: 104, ‘i’: 105, ‘s’: 115）创建为一个字典并访问键 ‘C’ 对应的值？

   ```python
   >>> dict1 = dict(F=70, C=67, h=104, i=105, s=115)
   >>> dict1
   {'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115}
   >>> dict1['C']
   67
   ```

   

3. 用方括号（“[]”）括起来的数据我们叫列表，那么使用大括号（“{}”）括起来的数据我们就叫字典，对吗？

   不对，用大括号括起来的数据还要形成有对应对象的映射关系（即 键 与 值 ）才能构成字典。

4. 你如何理解有些东西字典做得到，但“万能的”列表却难以实现（臣妾做不到T_T）？

   列表本身的元素是只有与其所在位置的索引值有对应关系的，而元素与元素之间是无法产生相互映射关系的，并且列表与列表之间要表达映射关系只能通过索引值进行索引之后再提取进行对应，这样会变麻烦很多。所以字典的存在就弥补了这种繁琐过程的缺陷，字典本身内在的元素就通过键(key)与值(value)之间进行了映射关系，所以在调用的时候能很快通过键取得值，省去了列表与列表先索引再对应的过程。

5. 下边这些代码，他们都在执行一样的操作吗？你看得出差别吗？

   ```python
   >>> a = dict(one=1,two=2,three=3)
   >>> b = {'one':1,'two':2,'three':3}
   >>> c = dict(zip(['one','two','three'],[1,2,3]))
   >>> d = dict([('two',2),('one',1),('three',3)])
   >>> e = dict({'three':3,'one':1,'two':2})
   ```

   A: 通过关键字定义，关键字不能加引号

   B: 直接定义

   C: 先用zip 生成一个具有映射关系的对象，每个元素就是一个元祖，包含键和值，然后用工厂函数dict 转换成字典

   D: 把一个具有映射关系的列表，用工厂函数dict 转换成字典

   E: 把一个具有映射关系的字典，用工厂函数dict 转换成字典

   

7. 如图，你可以推测出打了马赛克部分的代码吗？

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20190427184131580.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0ODk1OTI3,size_16,color_FFFFFF,t_70)

   ​	`data.split(',')`

### Practice

1. 尝试利用字典的特性编写一个通讯录程序吧，功能如图：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2019042718425940.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0ODk1OTI3,size_16,color_FFFFFF,t_70)

​	**Version-1**:

```python
# 尝试利用字典的特性编写一个通讯录程序吧


address_book = {'小甲鱼': '020-88974563', 'Felix': '025-52680000'}
welcome_msg = '''
|--- 欢迎进入通讯录程序---|
|--- 1： 查询联系人资料---|
|--- 2： 插入新的联系人---|
|--- 3： 删除已有联系人---|
|--- 4： 退出通讯录程序---|
'''
bye_msg = '''
|--- 感谢使用通讯录程序---|
'''


def ad_search():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        print(address_book[name])
    else:
        print('输入的联系人不存在！')


def ad_insert():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        print('您输入的姓名在通讯录中已存在 --->> %s : %s' %(name, address_book[name]))
        edit_check = input('是否修改用户资料（YES/NO）')
        if edit_check == 'YES':
            address_book[name] = input('请输入用户联系电话：')
    else:
        phone = input('请输入用户联系电话：')
        address_book[name] = phone


def ad_delete():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        del_check = input('是否删除已有联系人: %s（YES/NO）' % name)
        if del_check == 'YES':
            del address_book[name]
    else:
        print('输入的联系人不存在！')


def address():
    while True:
        print(welcome_msg)
        code = int(input('请输入相关的指令代码：'))
        if code == 2:
            ad_insert()
        elif code == 1:
            ad_search()
        elif code == 3:
            ad_delete()
        elif code == 4:
            print(bye_msg)
            break
        else:
            print('输入有误，请重新输入代码')


if __name__ == '__main__':
    address()

```



**Version-2**:  dict.pop() 删除字典键值, dict.setdefault() 修改字典：插入字典键值

```python
# 尝试利用字典的特性编写一个通讯录程序吧


address_book = {'小甲鱼': '020-88974563', 'Felix': '025-52680000'}
welcome_msg = '''
|--- 欢迎进入通讯录程序---|
|--- 1： 查询联系人资料---|
|--- 2： 插入新的联系人---|
|--- 3： 删除已有联系人---|
|--- 4： 退出通讯录程序---|
'''
bye_msg = '''
|--- 感谢使用通讯录程序---|
'''


def ad_search():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        print(address_book[name])
    else:
        print('输入的联系人不存在！')


def ad_insert():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        print('您输入的姓名在通讯录中已存在 --->> %s : %s' %(name, address_book[name]))
        edit_check = input('是否修改用户资料（YES/NO）')
        if edit_check == 'YES':
            address_book[name] = input('请输入用户联系电话：')
    else:
        # phone = input('请输入用户联系电话：')
        # address_book[name] = phone
        address_book.setdefault(name, input('请输入用户联系电话：'))


def ad_delete():
    name = input('请输入联系人姓名：')
    if name in address_book.keys():
        del_check = input('是否删除已有联系人: %s（YES/NO）' % name)
        if del_check == 'YES':
            address_book.pop(name)
    else:
        print('输入的联系人不存在！')


def address():
    while True:
        print(welcome_msg)
        code = int(input('请输入相关的指令代码：'))
        if code == 2:
            ad_insert()
        elif code == 1:
            ad_search()
        elif code == 3:
            ad_delete()
        elif code == 4:
            print(bye_msg)
            break
        else:
            print('输入有误，请重新输入代码')


if __name__ == '__main__':
    address()
```



# 026. 字典：当索引不好用时2

## 知识点

### 字典的常用内建方法

- 创建字典：fromkeys(): 

  > **fromkeys**(iterable, value=None, /) method of builtins.type instance;  Create a new dictionary with keys from iterable and values set to value.

  ```python
  >>> dict1 = {}
  >>> dict1.fromkeys((1, 2, 3))
  {1: None, 2: None, 3: None}
  >>> 
  >>> 
  >>> dict1.fromkeys((1, 2, 3), 'number')
  {1: 'number', 2: 'number', 3: 'number'}
  ```

  注意这个内置函数不能修改已有的字典，它每次都会生成一个新的字典；比如尝试修改1和3 的键值，但是只会生成一个新的字典

  ```python
  >>> dict1.fromkeys((1, 3), '数字')
  {1: '数字', 3: '数字'}
  ```

  

- 访问字典：keys(), values(), items()

- 查找字典：判断键的成员资格：get(),  in/not in 判断

  - get() : 

    > **get**(self, key, default=None, /)  Return the value for key if key is in the dictionary, else default.

- 清空字典：clear(),  或者del dict(key=)不推荐直接赋值空字典{} 的方式来清空，因为有数据泄漏风险

- 浅拷贝字典：copy(), 拷贝意味着生成一个新字典，与赋值是不同的。

- 删除/弹出对应的键值：pop()

- 删除/弹出字典键值 - 默认最后一个：popitem()

- 修改字典：追加：setdefault() ：和get() 类似，但是setdefault 找不到对应的值的时候，会自动添加，随机添加到某个位置，因为字典不存在顺序

- 修改字典：用字典去更新另外一个字典：update(), 类似于列表的extend()





## 课后作业

### Quiz

1. Python的字典是否支持一键（Key）多值（Value）？

   不支持，除非这个值是元祖和列表括起来的

2. 在字典中，如果试图为一个不存在的键（Key）赋值会怎样？

   会创建这个key and value

3. 成员资格操作符（in和not in）可以检查一个元素是否存在序列中，当然也可以用来检查一个键（Key）是否存在字典中，那么请问哪种的检查效率更高些？为什么？

   字典效率更高，因为是直接查找到相应的Key； 而序列是从第一个元素开始遍历

4. Python对键（Key）和值（Value）有没有类型限制？

   没有

5. 请目测下边代码执行后，字典dict1的内容是什么？

   ```
   >>> dict1.fromkeys((1, 2, 3), ('one', 'two', 'three'))
    
   >>> dict1.fromkeys((1, 3), '数字')
   ```

   ```
   （1:('one', 'two', 'three')， 2:('one', 'two', 'three')， 3:('one', 'two', 'three') ）
   (1:'数字', 3:'数字' )
   ```

6. 如果你需要将字典dict1 = {1: 'one', 2: 'two', 3: 'three'}拷贝到dict2，你应该怎么做？

   ```
   dict2 = dict1.copy()
   ```

   

### Practice

1. 尝试编写一个用户登录程序（这次尝试将功能封装成函数），程序实现如图

   <img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly94eHguaWxvdmVmaXNoYy5jb20vZm9ydW0vMjAxNDAzLzI0LzE5MDIwMjdrZDcyNTZoNnh5Nzc1ZGQucG5n?x-oss-process=image/format,png" alt="img" style="zoom:100%;" />

```python
# 尝试编写一个用户登录程序（这次尝试将功能封装成函数），程序实现如图

log_user = {}

welcome_msg = '''
|---新建用户：N/n---|
|---登陆账号：E/e---|
|---退出程序：Q/q---|
'''

register_msg = '''
注册成功，赶紧试试登陆吧！
'''

logon_msg = '''
欢迎进入xxoo系统，请点击右上方的x结束程序！
'''

quit_msg = '''
已成功退出系统！
'''


def logon():
    name = input('请输入用户名：')
    while name not in log_user.keys():
        name = input('您输入的用户名不存在，请重新输入：')
    passwd = input('请输入密码：')
    count = 3
    while log_user[name] != passwd:
        count -= 1
        if count > 0:
            passwd = input('密码错误，请重新输入')
        else:
            print('密码输入错误3次，退出程序')
            break
    print(logon_msg)


def create():
    name = input('请输入用户名：')
    while name in log_user.keys():
        name = input('此用户已经被使用，请重新输入：')
    log_user.setdefault(name, input('请输入密码：'))
    print(register_msg)


def logon_main():
    while True:
        print(welcome_msg, end='')
        code = input('|---请输入指令代码：')

        if code == 'N' or code == 'n':
            create()
        elif code == 'E' or code == 'e':
            logon()
        elif code == 'Q' or code == 'q':
            print(quit_msg)
            break


if __name__ == '__main__':
    logon_main()


```





# 027. 集合：在我的世界里，你就是唯一

## 知识点

### 集合的概念

- 集合是字典的“表亲”,  type = set, 用花括号括起一堆没有映射关系的元素

  ```
  >>> num = {}
  >>> type(num)
  <class 'dict'>
  >>> 
  >>> 
  >>> num2 = {1, 2, 3, 4}
  >>> type(num2)
  <class 'set'>
  ```

  

- 集合的元素是唯一，会自动过滤掉重复的元素

  ```
  >>> num2 = {1, 2, 3, 4, 5, 4, 3, 2, 1}
  >>> 
  >>> num2
  {1, 2, 3, 4, 5}
  ```

- 集合的元素是无序的，无法通过索引操作元素

  ```
  >>> num2[2]
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'set' object is not subscriptable
  ```

  

- 创建集合

  - 直接把一堆元素用花括号括起来

  - 使用set() 工厂函数,  可以传入序列参数

    ```
    >>> set1 = set([1, 2, 3, 4, 5, 5])
    >>> set1
    {1, 2, 3, 4, 5}
    ```

- 一个例子

  要求：去掉列表中重复的元素  [0, 1, 2, 3, 4, 5, 5, 3, 1]

  ```
  >>> list1 = [0, 1, 2, 3, 4, 5, 5, 3, 1]
  >>> 
  >>> list2 = list(set(list1))
  >>> list2
  [0, 1, 2, 3, 4, 5]
  ```

  注意：set 函数得到的集合是无序的！！！

  

### 集合的常用内建方法

- add()
- remove()

### Frozenset

- 不可变集合： 通过frozenset()

  ```
  >>> num3 = frozenset([1, 23, 4, 4])
  >>> num3
  frozenset({1, 4, 23})
  >>> 
  >>> num3.add(0)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  AttributeError: 'frozenset' object has no attribute 'add'
  ```

  

## 课后作业

### Quiz

1. 请问集合的唯一作用是什么呢？

   确保集合中的元素具有唯一性

2. 如果你希望创建的集合是不变的，应该怎么做？

   frozenset()

3. 请问如何确定一个集合里边有多少个元素？

   len() 函数

4. 请目测一下代码会打印什么内容？

   ```
   >>> num_set = set([1,2,3,4,5])
   
   >>> num_set[0]
   ```

   报错，集合是无序的，没有索引

5. 请问set1 = {[1,2]}和set1 = set([1,2])执行的结果一样吗？

   不一样，第一个会报错，第二个会生成一个集合

6. 打开你的IDLE，输入set1 ={1,1.0},你发现了什么？

   过滤掉相同的元素，得到{1}

7. 请问如何给集合添加和删除元素？

   add(), remove()

### Practice

1. 自学扩展：自己花点时间看下这个表格

   ![image.png](https://www.pianshen.com/images/918/769b9a085dba5f8b204a3f5abb4b2976.png)



# 028. 文件：因为懂你，所以永恒

## 知识点

- 文件的处理流程： 输入，处理， 输出

- 什么是文件：.exe, .txt, .ppt, .jpg, .mp4, .avi

- 打开文件：

  | 打开模式 | 执行操作                                       |
  | -------- | ---------------------------------------------- |
  | 'r'      | 以只读方式打开文件（默认）                     |
  | 'w'      | 以写入的方式打开文件，会覆盖已存在的文件       |
  | 'x'      | 如果文件已存在，使用此模式打开将引发异常       |
  | 'a'      | 以写入模式打开，如果文件存在，则在末尾追加写入 |
  | 'b'      | 以二进制模式打开文件                           |
  | 't'      | 以文本模式打开（默认）                         |
  | '+'      | 可读写模式（可添加到其他模式中使用）           |
  | 'U'      | 通用换行符支持                                 |

- 文件对象方法：

  | 文件对象方法                   | 执行操作                                                     |
  | ------------------------------ | ------------------------------------------------------------ |
  | f.close()                      | 关闭文件                                                     |
  | f.read([size=-1])              | 从文件读取size个字符，当未给定size或给定负值的时候，读取剩余的所有字符，然后作为字符串返回 |
  | f.readline([size=-1])          | 从文件中读取并返回一行（包括行结束符），返回字符串，如果有size有定义则返回size个字符 |
  | f.write(str)                   | 将字符串str写入文件                                          |
  | f.writelines(seq)              | 向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象 |
  | f.seek(offset, from)           | 在文件中移动文件指针，从from（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节 |
  | f.tell()                       | 返回当前在文件中的位置                                       |
  | f.truncate([size=file.tell()]) | 截取文件到size个字节，默认是截取到文件指针当前位置           |
  | f.readlines()                  | readlines()方法读取整个文件所有行，保存在一个列表(list)变量中，每行作为一个元素，但读取大文件会比较占内存。 |

  

  - f.read() 读一次，文件指针移动（类似于书签）一次；如果未指定size，会读取所有字符，指针移动到文件末尾；再次运行f.read()，就什么都读不出来了

    ```python
    >>> f = open('record.txt')
    >>> f.read()
    '小客服:小甲鱼?,今天有?客户问你有没有女朋友?\n小甲鱼:咦???\n小客服:我跟她说你有女朋友了!\n小甲鱼:。。。。。\n小客服:"她让你分手后考虑下她!然后我说您要买个优盘，我就帮您留意~\n小甲鱼:下次有人想调戏你我不阻止~\n小客服:滚!!!\n==========================================================\n小客服:小甲鱼,有个好评很好笑哈。\n小甲鱼:哦?\n小客服:"有了小甲小客服:嗯嗯,我看了你的微博丫~小甲鱼哟西~\n小客服:那个有条回复"左手拿著小甲魚,右手拿著打火機,哪裡不會點哪裡,?soeasy^...^"\n小甲鱼:T_T\n======================================鱼?,今天一?一个会员想找你\n小甲鱼:哦?什么事?\n小客服:他说你一个学生月薪已经超过12k了!?!\n小甲鱼:哪里的?\n小客服:上海的\n小甲鱼:那正常,哪家公司?\n小客服:他没说呀。\n小甲鱼:哦:滚!!!\n'
    
    >>> f.read()
    ''
    
    ```

  - f.tell() 可以查看当前文件指针位置

    ```python
    >>> f = open('record.txt')
    >>> f.read(5)
    '小客服:小'
    >>> 
    >>> f.tell()
    13
    
    ```

    注意： 由于我实验里面的record.txt 是utf-8 编码，所以一个中文字符是3个字节；如果是gbk编码的话，一个中文字符是2个字节

  - f.seek(offset, from) 可以用来修改文件指针位置; f.readline() 打印一行

    ```python
    >>> f.seek(46,0)
    46
    >>> f.readline()
    '没有女朋友?\n'
    
    ```

  - 可以直接迭代文件对象，来打印出文件的每一行

    ```
    f = open('record.txt')
    for each_line in f:
        print(each_line, end='')
    f.close()
    ```

  - f.write(str), f.writelines(seq, 比如list对象), 写入的类型都是字符串类型

    ```
    >>> f = open('test.txt', 'w')
    >>> f.write('I love fishc')
    12
    >>> f.close()
    
    >>> f = open('test.txt', 'w')
    >>> list1 = ['I', 'live', 'fishc']
    >>> list1
    ['I', 'live', 'fishc']
    >>> f.writelines(list1)
    >>> 
    >>> f.close()
    
    ```

    

## 课后作业

### Quiz

1. 下边只有一种方式不能打开文件，请问是哪一种，为什么？

   ```
   f = open('E:/test.txt','w')  #A
   f = open('E:\test.txt','w')  #B
   f = open('E://test.txt','w') #C
   f = open('E:\\test.txt','w') #D
   ```

​		***B，没有对反斜杠进行转义***， Windows在路径名中既可以接受斜线（/）也可以接受反斜线（\），不过如果使用反斜线作为路径名的[分隔符](https://so.csdn.net/so/search?q=分隔符&spm=1001.2101.3001.7020)的话，要注意使用双反斜线（\）进行转义，否则Python会将反斜线进行转义，例如（\n）看成一个换行符，（\t）看作一个制表符等

2. 打开一个文件我们使用open()函数，通过设置文件的打开模式，决定打开的文件具有哪些性质，请问默认的打开模式是什么呢？

   ‘rt’，即可读，文本的模式打开

3. 请问>>>open(‘E:\Test.bin’,‘xb’)是以什么样的模式打开文件的？

   以“可写入以及二进制模式”打开文件“E:\Test.bin”。
   这里要注意的是’x’和’w’均是以“可写入”的模式打开文件，但以’x’模式打开的时候，如果路径下已经存在相同的文件名，会抛出异常，而’w’模式的话会直接覆盖同名文件。
   因此，'w’模式打开文件会比较危险，容易导致此前的内容遗失，因此使用’w’模式打开文件前先检查该文件名是否已经存在显得非常重要！

4. 尽管python有所谓的“垃圾回收机制”，但对于打开了的文件，在不需要用到的时候我们仍然需要使用f.close()将文件对象“关闭”，这是为什么呢？

   Python拥有垃圾收集机制，会在文件对象的引用计数降至零的时候自动关闭文件，所以在Python编程里，如果忘记关闭文件并不会造成内存泄漏那么危险。
   但并不是说就可以不要关闭文件，如果你对文件进行了写入操作，那么你应该在完成写入之后进行关闭文件。因为Python可能会缓存你写入的数据，如果这中间断电了神马的，那些缓存的数据根本就不会写入到文件中。所以，为了安全起见，要养成使用完文件后立刻关闭的优雅习惯。

5. 如何将一个文件对象(f)中的数据存放进列表中？

   list(f)

6. 如何迭代打印出文件对象(f)中的每一行数据？

   ```python
   for each_line in f:
     print(each_line)
   ```

   

7. 文件对象的内置方法f.read([size=-1])作用是读取文件对象内容，size参数是可选的，那如果设置了size=10，例如f.read(10),将返回什么内容呢？

   读取文件指针当前位置往后读10个字符

   

8. 如何获得文件对象(f)当前文件指针的位置？

   `f.tell()`

9. 还是视频中的那个演示文件(record.txt),请问为何f.seek(45,0)不会出错，但f.seek(46)就出错了呢？

   ```
   
   >>> f.seek(46)
   46
   >>> f.readline()
   >Traceback (most recent call last):
   >File "<pyshell#18>", line 1, in <module>
   >f.readline()
   
   ```

   因为使用f.seek()定位的文件指针是按字节为单位进行计算的，演示文件（record.txt）是以GBK进行编码的，按照规则，一个汉字需要占用两个字节，f.seek(45)的位置位于字符“小”的开始位置，因此可以正常打印，而f.seek(46)的位置刚好位于字符“小”的中间位置，因此按照GBK编码的形式无法将其解码
   

### Practice

1. 尝试将某个文件(OpenMe.mp3)打印到屏幕上

   ```python
   f = open('OpenMe.mp3')
   for each_line in f:
       print(each_line, end='')
   f.close()
   ```

   

2. 编写代码，将上一题中的文件（OpenMe.mp3）保存为新文件（OpenMe.txt）

   ```python
   f1 = open('OpenMe.mp3')
   f2 = open('OpenMe.txt', 'x') # 使用'x'打开更安全，避免使用‘w’打开覆盖已有的文件
   
   f2.write(f1.read())
   
   f1.close()
   f2.close()
   ```

   

# 029. 文件：一个任务

## 知识点

> 任务：将文件(record.txt)中的数据进行分割，并按照以下规则保存起来。
>  1.小甲鱼的对话单独保存为boy_*.txt的文件(去掉"小甲鱼:")
>  2.小客服的对话单独保存为girl_*.txt的文件(去掉"小客服:")
>  3.文件中总共有三段对话，分别保存为boy_1.txt、boy_2.txt、boy_3.txt、gilr_1.txt、gilr_2.txt、gilr_3.txt
>    共6个文件。(提示：不同的对话已经使用"===="进行分割)



我的代码：

```python
# 任务：将文件(record.txt)中的数据进行分割，并按照以下规则保存起来。
#  1.小甲鱼的对话单独保存为boy_*.txt的文件(去掉"小甲鱼:")
#  2.小客服的对话单独保存为girl_*.txt的文件(去掉"小客服:")
#  3.文件中总共有三段对话，分别保存为boy_1.txt、boy_2.txt、boy_3.txt、gilr_1.txt、gilr_2.txt、gilr_3.txt
#    共6个文件。(提示：不同的对话已经使用"===="进行分割)


f1 = open('../28/record.txt', 'rt')
count = 1

boy_list = []
girl_list = []


def generate_file(file_name, file_list):
    f_file_name = open(file_name, 'x')
    f_file_name.writelines(file_list)
    f_file_name.close()


for each_line in f1:
    temp_list = each_line.split(':')
    if temp_list[0] == '小甲鱼':
        boy_list.append(temp_list[1])
    elif temp_list[0] == '小客服':
        girl_list.append(temp_list[1])

    if "====" in each_line:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        generate_file(file_name_boy, boy_list)
        generate_file(file_name_girl, girl_list)

        boy_list = []
        girl_list = []
        count += 1

# 循环结束，写入最后一段内容
file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'

generate_file(file_name_boy, boy_list)
generate_file(file_name_girl, girl_list)


# 关闭原始文件
f1.close()
```



## 课后作业

### Quiz



### Practice

1. 编写一个程序，接受用户的输入并保存为新的文件，程序实现如图：

   ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly94eHguaWxvdmVmaXNoYy5jb20vZm9ydW0vMjAxNDA0LzAyLzIxNDAwMmw4bXd3Y2I1MmY5ZjVxOWYucG5n?x-oss-process=image/format,png)

   ```python
   # 编写一个程序，接受用户的输入并保存为新的文件，程序实现如图
   
   
   name = input('请输入文件名：')
   # lines = []
   f = open(name, 'x')
   print('请输入内容【单独输入\':w\' 保存退出】:')
   
   
   while True:
       # 其实是循环等待每行输入，但是让input的输入提示符为空，效果是看起来一直没有打断的输入
       content = input()
       if content != ':w':
           content += '\n'
           f.write(content)
       else:
           break
           f.close()
   ```

   另一种实现：

   ```python
   # 编写一个程序，接受用户的输入并保存为新的文件，程序实现如图
   
   name = input('请输入文件名：')
   f = open(name, 'x')
   print('请输入内容【单独输入\':w\' 保存退出】:')
   
   # 用内置函数iter实现等待输入， 让input()遇到回车键也能持续输入
   txt = ''
   for line in iter(input, ':w'):
       txt += line + '\n'
   
   
   f.write(txt)
   f.close()
   ```

   

2. 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置，程序实现如图：

   ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly94eHguaWxvdmVmaXNoYy5jb20vZm9ydW0vMjAxNDA0LzA2LzIyMjYxNWlrM2J5cnB4NmpyampiNGIucG5n?x-oss-process=image/format,png)
   
   ```python
   # 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置，程序实现如图：
   
   name1 = input('请输入需要比较的头一个文件名：')
   name2 = input('请输入需要比较的另一个文件名：')
   
   name1_f = open(name1, 'rt')
   name2_f = open(name2, 'rt')
   
   name1_list = name1_f.readlines()
   name2_list = name2_f.readlines()
   
   name1_f.close()
   name2_f.close()
   
   
   diff_count = []
   name1_len = len(name1_list)
   name2_len = len(name2_list)
   
   
   if name1_len >= name2_len:
       file_min_len = name2_len
   else:
       file_min_len = name1_len
   
   
   for i in range(file_min_len):
       if name1_list[i] != name2_list[i]:
           diff_count.append(i)
   
   
   print('两个文件共有【 %d 】处不同：' % len(diff_count))
   
   for each in diff_count:
       print('第 %d 行不一样' % each)
   ```
   
   另一种写法：
   
   ```python
   def cp_file(fname1, fname2):
       name1_f = open(fname1, 'rt')
       name2_f = open(fname2, 'rt')
   
       diff_row = []
       count = 0
       row_number = 1
       for each_line in name1_f:
           if each_line != name2_f.readline():
               count += 1
               diff_row.append(row_number)
           row_number += 1
       name2_f.close()
       name2_f.close()
       if count == 0:
           print('两个文件相同')
       else:
           print('两个文件共有【 %d 】处不同：' % count)
           for each in diff_row:
               print('第 %d 行不一样' % each)
   
   
   def cp_main():
       name1 = input('请输入需要比较的头一个文件名：')
       name2 = input('请输入需要比较的另一个文件名：')
   
       cp_file(name1, name2)
   
   
   if __name__ == '__main__':
       cp_main()
   ```
   
   



3. 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上，程序实现如图：

   ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly94eHguaWxvdmVmaXNoYy5jb20vZm9ydW0vMjAxNDA0LzAyLzIxNTEzM3FzMml0dHRnMTFidnQwMTAucG5n?x-oss-process=image/format,png)
   
   ```python
   # 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上，程序实现如图：
   
   def show_file(name, rows):
       f_open = open(name, 'rt')
       for i in range(int(rows)):
           print(f_open.readline(), end='')
       f_open.close()
   
   
   f_name = input('请输入要打开的文件：')
   f_rows = input('请输入需要显示该文件前几行：')
   print('文件 %s 的前 %s 的内容如下：' % (f_name, f_rows))
   
   if __name__ == '__main__':
       show_file(f_name, f_rows)
   ```
   
   



4. 呃，不得不说我们的用户变得越来越刁钻了。要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。（如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容）

   ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly94eHguaWxvdmVmaXNoYy5jb20vZm9ydW0vMjAxNDA0LzAyLzIxNTMzMXhmMTg2amYzd21qcjVyeHoucG5n?x-oss-process=image/format,png)

​		

```python
# 呃，不得不说我们的用户变得越来越刁钻了。
# 要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。
# （如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容）


def show_file(name, rows):
    f_open = open(name, 'rt')
    f_lines = f_open.readlines()

    start_s, end_s = rows.split(':')
    if start_s == '':
        row_start = 0
        row_start_msg = '开始'
    else:
        row_start = int(start_s)-1
        row_start_msg = '第' + start_s + '行'
    if end_s == '':
        row_end = len(f_lines)
        row_end_msg = '末尾'
    else:
        row_end = int(end_s)
        row_end_msg = '第' + end_s + '行'

    print('文件 %s 从 %s 到 %s 行的内容如下：' % (f_name, row_start_msg, row_end_msg))
    for each_line in range(row_start, row_end):
        print(f_lines[each_line], end='')
    f_open.close()


f_name = input('请输入要打开的文件：')
f_rows = input('请输入需要显示的行数【格式如 13：21 或 ：21 或 21：】：')


if __name__ == '__main__':
    show_file(f_name, f_rows)
```



5. 编写一个程序，实现“全部替换”功能，程序实现如图：

   ![img](https://imgconvert.csdnimg.cn/aHR0cHM6Ly94eHguaWxvdmVmaXNoYy5jb20vZm9ydW0vMjAxNDA0LzAyLzIxNTM1NHZzNms4Nmw4bGZnMGw5cXEucG5n?x-oss-process=image/format,png)

   ​	
   
   ```python
   # 编写一个程序，实现“全部替换”功能，程序实现如图：
   
   def file_replace(name, o_str, n_str):
       f_read = open(name, 'rt')
       f_content = f_read.read()
       f_read.close()
       count = f_content.count(o_str)
       if count == 0:
           print('没有找到需要替换的字符')
       else:
           print('文件 %s 中共有 %d 个 【%s】' %(name, count, o_str))
           print('你确定要把所有【%s】的替换为【%s】吗' %(o_str, n_str))
           answer = input('[YES/NO]:')
           if answer == 'YES':
               f_content = f_content.replace(o_str, n_str)
               f_write = open(name, 'w')
               f_write.write(f_content)
               f_write.close()
   
   
   f_name = input('请输入文件名：')
   old_str = input('请输入需要替换的单词或字符：')
   new_str = input('请输入新的单词或字符：')
   
   
   if __name__ == '__main__':
       file_replace(f_name, old_str, new_str)
   ```
   
   

# 030. 文件系统：介绍一个高大上的东西

## 知识点

- 模块：它是包含所有你定义的函数和变量的文件，后缀是py；模块可以被别的程序引入，以使用该模块的函数等功能

  使用模块之前，需要先导入模块：import *module*

  ```python
  >>> secret = random.randint(1, 10)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'random' is not defined
  >>> 
  >>> import random
  >>> secret = random.randint(1, 10)
  >>> secret
  4
  ```

  

- OS 模块：

  > 我们所知道常用的操作系统有：windows，Mac OS， Linux， Unix等等，这些操作系统底层对于文件系统的访问工作原理是不一样的，因此你可能要针对不同的系统来考虑使用哪些文件系统模块。这样的做法是非常不友好且麻烦的，因为这样就意味着当你的程序运行环境一旦改变，你就要相应的去修改大量的代码来应付

  > 有了OS 模块，我们不需要关心什么操作系统下使用什么模块，OS模块会帮你选择正确的模块并调用

  

  - **os模块中关于文件/目录常用的函数使用方法**

  | **函数名**                                           | **使用方法**                                                 |
  | ---------------------------------------------------- | ------------------------------------------------------------ |
  | getcwd()                                             | 返回当前工作目录                                             |
  | chdir(path)                                          | 改变工作目录                                                 |
  | listdir(path='.')                                    | 列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录） |
  | mkdir(path)                                          | 创建单层目录，如该目录已存在抛出异常                         |
  | makedirs(path)                                       | 递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突 |
  | remove(path)                                         | 删除文件                                                     |
  | rmdir(path)                                          | 删除单层目录，如该目录非空则抛出异常                         |
  | removedirs(path)                                     | 递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常 |
  | rename(old, new)                                     | 将文件old重命名为new                                         |
  | system(command)                                      | 运行系统的shell命令                                          |
  | walk(top)                                            | 遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])【具体实现方案请看：第30讲课后作业^_^】 |
  | *以下是支持路径操作中常用到的一些定义，支持所有平台* |                                                              |
  | os.curdir                                            | 指代当前目录（'.'）                                          |
  | os.pardir                                            | 指代上一级目录（'..'）                                       |
  | os.sep                                               | 输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）    |
  | os.linesep                                           | 当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）       |
  | os.name                                              | 指代当前使用的操作系统（包括：'posix', 'nt', 'mac', 'os2', 'ce', 'java'） |

  

  

  ```python
  >>> import os
  >>> os.getcwd()
  '/Users/felix'
  
  >>> os.chdir('/Users/felix/PycharmProjects/learningpython/30')
  >>> 
  >>> 
  >>> 
  >>> os.listdir('.')
  []
  >>> 
  >>> 
  >>> os.mkdir('A')
  >>> os.mkdir('B')
  >>> os.mkdir('./C/D')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  FileNotFoundError: [Errno 2] No such file or directory: './C/D'
  >>> 
  >>> os.listdir('.')
  ['A', 'B']
  >>> 
  >>> os.makedirs('./C/D')
  >>> os.listdir()
  ['A', 'C', 'B']
  >>> os.remove
  os.remove(      os.removedirs(  
  >>> os.removedirs('C')
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/usr/local/Cellar/python@3.9/3.9.12_1/Frameworks/Python.framework/Versions/3.9/lib/python3.9/os.py", line 243, in removedirs
      rmdir(name)
  OSError: [Errno 66] Directory not empty: 'C'
  
  >>> 
  >>> 
  >>> os.removedirs('./C/D')
  >>> 
  >>> os.listdir()
  ['A', 'B']
  >>> os.rename('B', 'D')
  >>> os.listdir()
  ['A', 'D']
  
  >>> os.system('ls -l')
  total 0
  drwxr-xr-x  2 felix  staff  64 May 24 08:57 A
  drwxr-xr-x  2 felix  staff  64 May 24 08:58 D
  0
    
    
  >>> os.listdir(os.curdir)
  ['A', 'D']
  >>> 
  >>> os.listdir(os.pardir)
  ['03', '04', '05', '02', '20', '18', '29', '16', '28', '17', '10', '19', '26', 'test.py', 'README.md', '09', '30', '01', '06', '.git', '24', '23', '15', '14', '22', '.idea', '25']
  >>> os.listdir(os.pardir+ '/29')
  ['05.py', 'task.py', 'example-2.py', '01-1.py', '04.py', 'boy_1.txt', 'boy_2.txt', 'boy_3.txt', '03.py', 'girl_1.txt', '02-1.py', 'girl_2.txt', '02.py', 'input_nonstop.py', 'girl_3.txt']
  
  >>> os.name
  'posix'
  ```

  

- OS.PATH 模块

  - **os.path模块中关于路径常用的函数使用方法**

  | **函数名**                     | **使用方法**                                                 |
  | ------------------------------ | ------------------------------------------------------------ |
  | basename(path)                 | 去掉目录路径，单独返回文件名                                 |
  | dirname(path)                  | 去掉文件名，单独返回目录路径                                 |
  | join(path1[, path2[, ...]])    | 将path1, path2各部分组合成一个路径名                         |
  | split(path)                    | 分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在 |
  | splitext(path)                 | 分离文件名与扩展名，返回(f_name, f_extension)元组            |
  | getsize(file)                  | 返回指定文件的尺寸，单位是字节                               |
  | getatime(file)                 | 返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算） |
  | getctime(file)                 | 返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算） |
  | getmtime(file)                 | 返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算） |
  | *以下为函数返回 True 或 False* |                                                              |
  | exists(path)                   | 判断指定路径（目录或文件）是否存在                           |
  | isabs(path)                    | 判断指定路径是否为绝对路径                                   |
  | isdir(path)                    | 判断指定路径是否存在且是一个目录                             |
  | isfile(path)                   | 判断指定路径是否存在且是一个文件                             |
  | islink(path)                   | 判断指定路径是否存在且是一个符号链接                         |
  | ismount(path)                  | 判断指定路径是否存在且是一个挂载点                           |
  | samefile(path1, paht2)         | 判断path1和path2两个路径是否指向同一个文件                   |

  ```python
  >>> import os.path
  >>> 
  >>> os.path.basename(os.curdir + 'A/sexy.txt')
  'sexy.txt'
  >>> 
  >>> 
  >>> os.path.dirname(os.curdir + 'A/sexy.txt')
  '.A'
  >>> 
  >>> 
  >>> 
  >>> os.path.join('A', 'B', 'C')
  'A/B/C'
  >>> os.path.join('.', 'A', 'B', 'C')
  './A/B/C'
  >>> os.path.split(os.curdir + 'A/sexy.txt')
  ('.A', 'sexy.txt')
  >>> os.path.getsize(os.pardir+ '/29/05.py')
  926
  >>> 
  >>> os.path.getatime(os.pardir+ '/29/05.py')
  1653282351.295187
  >>> 
  >>> os.path.getmtime(os.pardir+ '/29/05.py')
  1653279681.7378166
  
  >>> import time
  >>> time.gmtime(os.path.getmtime(os.pardir+ '/29/05.py'))
  time.struct_time(tm_year=2022, tm_mon=5, tm_mday=23, tm_hour=4, tm_min=21, tm_sec=21, tm_wday=0, tm_yday=143, tm_isdst=0)
  >>> time.localtime(os.path.getmtime(os.pardir+ '/29/05.py'))
  time.struct_time(tm_year=2022, tm_mon=5, tm_mday=23, tm_hour=12, tm_min=21, tm_sec=21, tm_wday=0, tm_yday=143, tm_isdst=0)
  
  >>> os.path.exists(os.curdir + '/A/sexy.txt')
  False
  >>> 
  
  >>> os.path.exists(os.curdir + '/A')
  True
  
  >>> os.path.isabs(os.curdir + '/A')
  False
  >>> 
  >>> os.path.isdir(os.curdir + '/A')
  True
  ```

  

## 课后作业

### Quiz



### Practice

1. 编写一个程序，统计当前目录下每个文件类型的文件数，程序实现如图：

   ![img](https://img-blog.csdn.net/20180829233232993?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI0NTQ2MTM3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

   ```python
   # 编写一个程序，统计当前目录下每个文件类型的文件数，程序实现如图：
   import os
   import os.path
   
   
   def count_ext(file_path):
       ext_dic = {}
       count = 0
       dir_elements = os.listdir(file_path)
       for each in dir_elements:
           ext = os.path.splitext(each)[1]
           if ext not in ext_dic.keys():
               ext_dic.setdefault(ext, 1)
           else:
               ext_dic[ext] += 1
       for each_ext in ext_dic.keys():
           if each_ext =='':
               print('文件夹：【 %s 】下共有类型为文件夹的文件 %d 个' % (file_path, ext_dic[each_ext]))
           else:
               print('文件夹：【 %s 】下共有类型为 [ %s ] 的文件 %d 个' % (file_path, each_ext, ext_dic[each_ext]))
   
   
   count_ext(os.path.curdir)
   ```

   

2. 编写一个程序，计算当前文件夹下所有文件的大小，程序实现如图：

   ![img](https://img-blog.csdn.net/20180829233243506?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI0NTQ2MTM3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

   ```python
   # 编写一个程序，计算当前文件夹下所有文件的大小，程序实现如图：
   
   import os
   import os.path
   
   
   def file_size(f_path):
       os.chdir(f_path)
       file_list = list(filter(lambda x: os.path.isfile(x), os.listdir(f_path)))
       for each_file in file_list:
           print(each_file + '  【%d Bytes】 ' % os.path.getsize(each_file))
   
   
   if __name__ == '__main__':
       file_size(input('please input the path:'))
   ```

   

3. 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图：

   ![img](https://img-blog.csdn.net/20180829233256964?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI0NTQ2MTM3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

   ```python
   # 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图
   
   import os
   import os.path
   
   
   def search_file(path, file_name):
       os.chdir(path)
       temp_folder_name = list(filter(lambda x: os.path.isdir(x), os.listdir(path)))
       temp_file_name = list(filter(lambda x: os.path.isfile(x), os.listdir(path)))
       if file_name in temp_file_name:
           print(os.path.join(path, file_name))
       if temp_folder_name:
           for sub_folder_name in temp_folder_name:
               search_file(os.path.join(path, sub_folder_name), file_name)
   
   
   if __name__ == '__main__':
       search_file(input('请输入待查找的初始目录：'), input('请输入需要查找的目标文件：'))
   ```

   还可以通过os.walk() 来实现：

   ```python
   # 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图
   
   import os
   import os.path
   
    
   def search_file(path, file_name):
       # os.walk() 返回的是一个三元组迭代器，有三元组参数，通过for 循环使用
       for folder, sub_folders, sub_files in os.walk(path): 
           if file_name in sub_files:
               print(os.path.join(folder, file_name))
   
   
   if __name__ == '__main__':
       search_file(input('请输入待查找的初始目录：'), input('请输入需要查找的目标文件：'))
   ```

   

4. 编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹）所有的视频格式文件（要求查找mp4，rmvb，avi的格式即可），并创建一个文件（vedioList.txt）存放找到的文件的路径，程序实现如图：

   ![img](https://img-blog.csdn.net/20180829233514332?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI0NTQ2MTM3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

   ![img](https://img-blog.csdn.net/20180829233329338?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI0NTQ2MTM3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

   ```python
   # 编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹）所有的视频格式文件（要求查找mp4，rmvb，avi的格式即可），
   # 并创建一个文件（vedioList.txt）存放找到的文件的路径，程序实现如图：
   
   import os
   import os.path
   
   file_list = []
   
   def search_video(path, format_list=['.mp4', '.rmvb', '.avi']):
       os.chdir(path)
       temp_folder = list(filter(lambda x: os.path.isdir(x), os.listdir(path)))
       temp_file = list(filter(lambda x: (os.path.isfile(x) and os.path.splitext(x)[1] in format_list), os.listdir(path)))
       file_list.extend(os.path.join(path, each_file) for each_file in temp_file)
       if temp_folder:
           for sub_folder in temp_folder:
               search_video(os.path.join(path, sub_folder))
   
       f_video_list = open('/Users/felix/PycharmProjects/learningpython/vedioList.txt', 'w')
       
       # 如果直接使f_video_list.writelines(file_list) 写入的文件内容没有换行
       # f_video_list.writelines(file_list)
       for each_file_path in file_list:
           f_video_list.write(each_file_path)
           f_video_list.write('\n')
       f_video_list.close()
   
   
   if __name__ == '__main__':
       search_video(input('请输入待查找的初始目录：'))
   ```

   

5. 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符），程序实现如图：

   ![img](https://img-blog.csdn.net/20180829233344730?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI0NTQ2MTM3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
   
   ​	
   
   ```python
   # 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），
   # 要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符），程序实现如图
   
   import os
   import os.path
   
   
   # 存放所有目录和子目录下的txt 文件，并且是绝对路径
   sub_full_txt = []
   file_row_keyword = {}
   
   
   def search_keyword(path, keyword):
       for folder, sub_folders, sub_files in os.walk(path):
           # 过滤出txt 文件
           sub_files_txt = list(filter(lambda x: os.path.splitext(x)[1] == '.txt', sub_files))
           # 转换成绝对路径的txt 文件
           sub_full_txt.extend(os.path.join(folder, each_file) for each_file in sub_files_txt)
   
       for file_name in sub_full_txt:
           f_open = open(file_name, 'r', encoding='utf-8')
           f_lines = f_open.readlines()
           f_open.close()
   
           # 预先定义一个子字典存储行数和关键字位置关系信息
           row_keyword = {}
   
           for row_number in range(len(f_lines)):
               f_keyword_index = []
               start_flag = 0
               f_keyword_number = f_lines[row_number].find(keyword, start_flag)
   
               while f_keyword_number >= 0:
                   f_keyword_index.append(f_keyword_number)
                   start_flag = f_keyword_number + 1
                   f_keyword_number = f_lines[row_number].find(keyword, start_flag)
                   if f_keyword_number == -1:
                       row_keyword.setdefault(row_number+1, f_keyword_index)
                       if file_name in file_row_keyword.keys():
                           file_row_keyword[file_name] = row_keyword
                       else:
                           file_row_keyword.setdefault(file_name, row_keyword)
   
       # 函数返回一个字典，key=文件路径，value=（以行数为key，以位置信息列表为value 的字典），如下
       # {
       #   'C:/Users/felix_yang/PycharmProjects/learningpython\\28\\record.txt': {5: [16], 6: [4]},
       #  'C:/Users/felix_yang/PycharmProjects/learningpython\\29\\boy_1.txt': {3: [0]},
       #  'C:/Users/felix_yang/PycharmProjects/learningpython\\29\\boy_2.txt': {3: [0]},
       #  'C:/Users/felix_yang/PycharmProjects/learningpython\\29\\girl_1.txt': {3: [12, 23], 7: [12, 23]}
       # }
   
       return file_row_keyword
   
   
   if __name__ == '__main__':
       filename = input('请输入待查找的初始目录：')
       keyword = input('请输入需要查找的关键字：')
       search_keyword(filename, keyword)
       for file_key in file_row_keyword.keys():
           print('============================================')
           print('在文件【%s】中找到关键字【%s】' % (file_key, keyword))
           for rows in file_row_keyword[file_key].keys():
               # 将字典存储的位置信息转换成字符串打印
               key_str = [str(i) for i in file_row_keyword[file_key][rows]]
               print('关键字出现在第 %d 行，第 【 %s 】 位置' % (rows, ','.join(key_str)))
   
   ```
   
   ```
   
   请输入待查找的初始目录：C:/Users/felix_yang/PycharmProjects/learningpython
   请输入需要查找的关键字：小甲鱼
   ============================================
   在文件【C:/Users/felix_yang/PycharmProjects/learningpython\28\record.txt】中找到关键字【小甲鱼】
   关键字出现在第 1 行，第 【 4 】 位置
   关键字出现在第 2 行，第 【 0 】 位置
   关键字出现在第 4 行，第 【 0 】 位置
   关键字出现在第 6 行，第 【 0 】 位置
   关键字出现在第 8 行，第 【 0 】 位置
   关键字出现在第 10 行，第 【 0 】 位置
   关键字出现在第 13 行，第 【 4 】 位置
   关键字出现在第 14 行，第 【 0 】 位置
   关键字出现在第 15 行，第 【 7 】 位置
   关键字出现在第 16 行，第 【 0 】 位置
   关键字出现在第 17 行，第 【 16 】 位置
   关键字出现在第 19 行，第 【 0 】 位置
   关键字出现在第 21 行，第 【 4 】 位置
   关键字出现在第 22 行，第 【 0 】 位置
   关键字出现在第 24 行，第 【 0 】 位置
   关键字出现在第 26 行，第 【 0 】 位置
   关键字出现在第 28 行，第 【 0 】 位置
   关键字出现在第 30 行，第 【 0 】 位置
   ============================================
   在文件【C:/Users/felix_yang/PycharmProjects/learningpython\29\girl_1.txt】中找到关键字【小甲鱼】
   关键字出现在第 1 行，第 【 0 】 位置
   ============================================
   在文件【C:/Users/felix_yang/PycharmProjects/learningpython\29\girl_2.txt】中找到关键字【小甲鱼】
   关键字出现在第 1 行，第 【 0 】 位置
   关键字出现在第 2 行，第 【 3 】 位置
   关键字出现在第 3 行，第 【 12 】 位置
   ============================================
   在文件【C:/Users/felix_yang/PycharmProjects/learningpython\29\girl_3.txt】中找到关键字【小甲鱼】
   关键字出现在第 1 行，第 【 0 】 位置
   
   Process finished with exit code 0
   
   ```
   
   

# 031. 永久存储：腌制一缸美味的泡菜

## 知识点

### pickle 模块

> 我们之前学习了文件和文件系统，我们知道从一个文件里面去读取字符串是非常简单的，但是你如果要试图读取出数值的话，那么就要多费点周折了，因为无论你是使用read()方法还是readline()方法，都是返回一个字符串，如果我们希望从字符串中取出数值的话，我们会使用int()或float()函数，把类似于1,2,3或者3.14的字符串强制转换为整型或者浮点型数值，我们一直在讲保存文件，然而当你要保存的数据像列表，字典，集合甚至是类的实例这些更加复杂的数据类型的时候，你就会举手无措了，兴许你可能会把这些都转化为字符串，然后再写入到一个文本文件中保存起来，但是很快你就会发现，把这个过程反过来的时候，也就是从文本文件中恢复数据对象，即把一个字符串恢复成列表，字典，集合，类的实例的时候，你会发现这异常的困难，所幸的是，Python提供了一个标准的模块（pickle）使用这个模块，我们就可以轻松地将列表，字典，集合，类的实例这类复杂的类型转换为二进制文件了。这个模块就是我们要学习的pickle模块了。

- 令人惊叹的模块，几乎可以把所有的python 对象 转换成二进制的形式存储. `import pickle`

- 存取数据：pickling - pickle.dump(src_object, pickle_file_object)

- 读取数据：unpickling - pickle.load(pickle_file_object)

  ```
  >>> import pickle
  >>> 
  >>> my_list = [123, 1232, '小甲鱼']
  >>> 
  >>> pickle_file = open('my_list.pkl', 'wb')
  >>> pickle.dump(my_list, pickle_file)
  >>> pickle_file.close()
  
  >>> pickle_file = open('my_list.pkl', 'rb')
  >>> my_list2 = pickle.load(pickle_file)
  >>> my_list2
  [123, 1232, '小甲鱼']
  >>> pickle_file.close()
  ```

- 可以把一些大数据“腌制成泡菜“ ，即保存成一个pkl 二进制文件，在代码中导入进行引用，使得代码更加简洁优雅



## 课后作业

### Quiz

1. pickle的实质是什么？

   pickle的实质就是利用一些算法将你的数据对象“腌制”成二进制文件，存储在磁盘上，当然也可以放在数据库或者通过网络传输到另一台计算机上。

2. 使用pickle的什么方法存储数据？

   pickle.dump(src_object, pickle_file_object); 第一个参数是待存储的数据对象，第二个参数是目标存储的文件对象，注意要先使用’wb’的模式open文件哦

3. 使用pickle的什么方法读取数据？

   pickle.load(pickle_file_object); 参数是目标存储的文件对象，注意要先使用’rb’的模式open文件哦

4. 使用pickle能不能保存为”*.txt”类型的文件？

   可以，不过打开后是乱码，因为是以二进制的模式写入的。

### Practice

1. 编写一个程序，这次要求使用pickle将文件（ record.txt (1.1 KB, 下载次数: 3561) ）里的对话按照以下要求腌制成不同文件（没错，是第29讲的内容小改，考考你自己能写出来吗？）：
               ※小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
               ※小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
               ※文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件（提示：文件中不同的对话间已经使用“==========”分割）

   ```python
   # 编写一个程序，这次要求使用pickle将文件（ record.txt (1.1 KB, 下载次数: 3561) ）里的对话按照以下要求腌制成不同文件（没错，是第29讲的内容小改，考考你自己能写出来吗？）：
   #             ※小甲鱼的对话单独保存为boy_*.txt的文件（去掉“小甲鱼:”）
   #             ※小客服的对话单独保存为girl_*.txt的文件（去掉“小客服:”）
   #             ※文件中总共有三段对话，分别保存为boy_1.txt, girl_1.txt，boy_2.txt, girl_2.txt, boy_3.txt, gril_3.txt共6个文件
   #             （提示：文件中不同的对话间已经使用“==========”分割）
   
   
   import pickle
   
   
   def extract(file_name):
       count = 0
       boy_list = []
       girl_list = []
       record_file = open(file_name, 'r')
       for each_line in record_file:
           temp_list = each_line.split(':')
           if temp_list[0] == '小甲鱼':
               boy_list.append(temp_list[1])
           elif temp_list[0] == '小客服':
               girl_list.append(temp_list[1])
   
           if '========' in each_line:
               count += 1
               pickle_file_boy = open('boy_%d.txt' % count, 'wb')
               pickle_file_girl = open('girl_%d.txt' % count, 'wb')
               pickle.dump(boy_list, pickle_file_boy)
               pickle.dump(girl_list, pickle_file_girl)
               pickle_file_boy.close()
               pickle_file_girl.close()
               boy_list = []
               girl_list = []
       count += 1
       pickle_file_boy = open('boy_%d.txt' % count, 'wb')
       pickle_file_girl = open('girl_%d.txt' % count, 'wb')
       pickle.dump(boy_list, pickle_file_boy)
       pickle.dump(girl_list, pickle_file_girl)
       pickle_file_boy.close()
       pickle_file_girl.close()
   
       record_file.close()
   
   
   extract('record.txt')
   ```

   

# 032. 异常处理：你不可能总是对的

## 知识点

### Python 标准异常总结

| 异常                  | 描述                                                         |
| --------------------- | ------------------------------------------------------------ |
| AssertionError        | 断言语句（assert）失败                                       |
| AttributeError        | 尝试访问未知的对象属性                                       |
| EOFError              | 用户输入文件末尾标志EOF（Ctrl+d）                            |
| FloatingPointError    | 浮点计算错误                                                 |
| GeneratorExit         | generator.close()方法被调用的时候                            |
| ImportError           | 导入模块失败的时候                                           |
| IndexError            | 索引超出序列的范围                                           |
| KeyError              | 字典中查找一个不存在的关键字                                 |
| KeyboardInterrupt     | 用户输入中断键（Ctrl+c）                                     |
| MemoryError           | 内存溢出（可通过删除对象释放内存）                           |
| NameError             | 尝试访问一个不存在的变量                                     |
| NotImplementedError   | 尚未实现的方法                                               |
| OSError               | 操作系统产生的异常（例如打开一个不存在的文件）               |
| OverflowError         | 数值运算超出最大限制                                         |
| ReferenceError        | 弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象 |
| RuntimeError          | 一般的运行时错误                                             |
| StopIteration         | 迭代器没有更多的值                                           |
| SyntaxError           | Python的语法错误                                             |
| IndentationError      | 缩进错误                                                     |
| TabError              | Tab和空格混合使用                                            |
| SystemError           | Python编译器系统错误                                         |
| SystemExit            | Python编译器进程被关闭                                       |
| TypeError             | 不同类型间的无效操作                                         |
| UnboundLocalError     | 访问一个未初始化的本地变量（NameError的子类）                |
| UnicodeError          | Unicode相关的错误（ValueError的子类）                        |
| UnicodeEncodeError    | Unicode编码时的错误（UnicodeError的子类）                    |
| UnicodeDecodeError    | Unicode解码时的错误（UnicodeError的子类）                    |
| UnicodeTranslateError | Unicode转换时的错误（UnicodeError的子类）                    |
| ValueError            | 传入无效的参数                                               |
| ZeroDivisionError     | 除数为零                                                     |



### 常见异常

- AssertionError
- AttributeError
- IndexError
- KeyError
- NameError
- SyntaxError
- TypeError
- ZeroDivisionError

```python
>>> mylist = ['小甲鱼是帅哥']
>>> assert len(mylist) > 0
>>> mylist.pop()
'小甲鱼是帅哥'
>>> mylist
[]
>>>
>>> assert len(mylist) > 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

>>> mylist.fishc
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'fishc'
    
>>> my_list = [1, 2, 3]
>>>
>>> my_list[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> my_dict = {'one':1, 'two':2}
>>>
>>> my_dict['one']
1
>>> my_dict['four']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'four'
>>>
>>>
>>> my_dict.get('four')

>>> mylist1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mylist1' is not defined
    
>>> print 'I love FishC'
  File "<stdin>", line 1
    print 'I love FishC'
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('I love FishC')?
    
>>> 1 + '1'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
        
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```



## 课后作业

### Quiz

1. 结合你自身的编程经验，总结下[异常处理机制](https://so.csdn.net/so/search?q=异常处理机制&spm=1001.2101.3001.7020)的重要性？

   由于环境的不确定性和用户操作的不可以预知性都可能导致程序出现各种问题，因此异常机制最重要的无非就是：增强程序的健壮性和用户体验，尽可能的捕获所有预知的异常并写好处理的代码，当异常出现的时候，程序自动消化并恢复正常（不至于崩溃）。|

2. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称

   ```python
   >>> my_list = [1, 2, 3, 4,,]
   ```

   SyntaxError

3. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称

   ```python
   >>> my_list = [1, 2, 3, 4, 5]
   >>> print(my_list[len(my_list)])
   ```

   IndexError

4. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称

   ```python
   >>> my_list = [3, 5, 1, 4, 2]
   >>> my_list.sorted()
   ```

   列表的排序方法叫 list.sort()，sorted() 是BIF。因此会引发 AttributeError: ‘list’ object has no attribute ‘sorted’ 异常。

5. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称

   ```python
   >>> my_dict = {'host': 'http://bbs.fishc.com', 'port': '80'}
   >>> print(my_dict['server'])
   ```

   KeyError

6. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称

   ```python
   def my_fun(x, y):
           print(x, y)
   
   my_fun(x=1, 2)
   ```

   SyntaxError 如果使用关键字参数的话，需要两个参数均使用关键字参数 my_fun(x=1, y=2)

7. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称

   ```python
   f = open('C:\\test.txt', wb)
   f.write('I love FishC.com!\n')
   f.close()
   ```

   NameError

   注意 open() 第二个参数是字符串，应该 f = open(‘C:\test.txt’, ‘wb’) 。wb不加双引号 Python 还以为是变量名呢，往上一找，艾玛没找着……引发 NameError 异常。由于打开文件失败，接着下边一连串与 f 相关的均会报同样异常。

8. 请问以下代码是否会产生异常，如果会的话，请写出异常的名称：

   ```python
   def my_fun1():
           x = 5
           def my_fun2():
                   x *= x
                   return x
           return my_fun2()
   
   my_fun1()
   ```

   

   

   闭包的知识大家还记得不？ Python 认为在内部函数的 x 是局部变量的时候，外部函数的 x 就被屏蔽了起来，所以执行 x *= x 的时候，在右边根本就找不到局部变量 x 的值，因此报错。
   在 Python3 之前没有直接的解决方案，只能间接地通过容器类型来存放，因为容器类型不是放在栈里，所以不会被“屏蔽”掉。容器类型这个词儿大家是不是似曾相识？我们之前介绍的字符串、列表、元祖，这些啥都可以往里的扔的就是容器类型啦。

   ```python
   def my_fun1():
           x = [5]
           def my_fun2():
                   x[0] *= x[0]
                   return x[0]
           return my_fun2()
   
   my_fun1()
   
   123456789
   ```

   但是到了 Python3 的世界里，又有了不少的改进，如果我们希望在内部函数里可以修改外部函数里的局部变量的值，那么也有一个关键字可以使用，就是 nonlocal：

   ```python
   def my_fun1():
           x = 5
           def my_fun2():
                   nonlocal x
                   x *= x
                   return x
           return my_fun2()
   
   my_fun1()
   ```



# 033. 异常处理：你不可能总是对的-2

## 知识点

- try-except 语句 ： Try 语句一旦检测到异常，剩下的语句不会被执行

  ```
  try:
  	检测范围
  except Exceptions[as reason]
  	出现异常（exception）后的处理代码
  ```

  **Example-1:**

  ```python
  try:
      # OSError，尝试打开一个不存在的文件
      f = open('我为什么是个文件.txt')
      print(f.read())
      f.close()
  except OSError:
      print('文件出错啦@')
  ```

  output:

  ```
  文件出错啦@ 
  ```

  **Example-2:**

  ```python
  try:
      # OSError，尝试打开一个不存在的文件
      f = open('我为什么是个文件.txt')
      print(f.read())
      f.close()
  except OSError as reason:
      print('文件出错啦@ \n错误的原因是：' + str(reason))
  ```

  output:

  ```
  文件出错啦@ 
  错误的原因是：[Errno 2] No such file or directory: '我为什么是个文件.txt'
  ```

  **Example-3:**

  ```python
  try:
      #TypeError
      sum_umber = 1 + '1'
      
      # OSError，尝试打开一个不存在的文件
      f = open('我为什么是个文件.txt')
      print(f.read())
      f.close()
  except OSError as reason:
      print('文件出错啦@ \n错误的原因是：' + str(reason))
  except TypeError as reason:
      print('类型出错啦@ \n错误的原因是：' + str(reason))
  ```

  output:

  ```
  类型出错啦@ 
  错误的原因是：unsupported operand type(s) for +: 'int' and 'str'
  ```

  **注意由于检测到`sum_umber = 1 + '1'` 异常，会直接跳到`except TypeError as reason`, 主程序的剩余代码不会被执行**

  

  **Example-4:** 直接用except，无论什么出错，都能cover到;  ***但是太笼统，实际中并不推荐*** ，比如如果用户用`ctrl+c`想中断关闭程序，会由于KeyboardInterrupt 异常被捕获而触发出错Error，反而导致程序不会中断关闭

  ```python
  try:
      int('abc')
      sum_umber = 1 + '1'
      f = open('我为什么是个文件.txt')
      print(f.read())
      f.close()
  except:
      print('出错啦@')
  ```

   output:

  ```
  出错啦@
  ```

  **Example-5:** 

  ```python
  try:
      sum_umber = 1 + '1'
      f = open('我为什么是个文件.txt')
      print(f.read())
      f.close()
  except (OSError, TypeError):
      print('文件出错啦@')
  ```

  output:

  ```
  出错啦@
  ```

  

- try-finally 语句:  做收尾工作

  ```
  try:
  	检测范围
  except Exceptions[as reason]:
  	出现异常（Exception）后的处理代码
  finally:
  	无论如何都会被执行的代码
  ```

  ```python
  try:
      f = open('我为什么是个文件.txt', 'w')
      f.write('我存在了！')
      sum_umber = 1 + '1'
  
  except (OSError, TypeError):
      print('文件出错啦@')
  finally:
      f.close()
  ```

  

- raise 语句触发异常

  ```python
  >>> 1/0
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ZeroDivisionError: division by zero
  >>> raise ZeroDivisionError
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ZeroDivisionError
  ```

  

## 课后作业

### Quiz

1. 我们使用什么方法来处理程序中出现的异常？

   try-except-finally

2. 一个 try 语句可以和多个 except 语句搭配吗？为什么？

   可以，针对不同的errortype 可以使用不同的except的语句

3. 你知道如何统一处理多类异常吗？

   使用元祖：`except (OSError, TypeError):`

4. except 后边如果不带任何异常类，Python 会捕获所有（try 语句块内）的异常并统一处理，但小甲鱼却不建议这么做，你知道为什么吗？

   **太笼统，实际中并不推荐*** ，比如如果用户用`ctrl+c`想中断关闭程序，会由于KeyboardInterrupt 异常被捕获而触发出错Error，反而导致程序不会中断关闭

5. 如果异常发生在成功打开文件后，Python 跳到 except 语句执行，并没有执行关闭文件的命令（用户写入文件的数据就可能没有保存起来），因此我们需要确保无论如何（就算出了异常退出）文件也要被关闭，我们应该怎么做呢？

   使用finally 保证代码块一定会被执行； 如果 try 语句块中没有出现任何运行时错误，会跳过 except 语句块执行 finally 语句块的内容。

6. 请恢复以下代码中马赛克挡住的内容，使得程序执行后可以按要求输出。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200728115630241.png)

   

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200728115633801.png)

   ```python
   try:
       for i in range(3):
           for j in range(3):
               if i == 2:
                   raise KeyboardInterrupt
               print(i, j)
   except KeyboardInterrupt:
       print('推出啦！')
   ```

   

### Practice

1. 还记得我们第一个小游戏吗？只要用户输入非整型数据，程序立刻就会蹦出不和谐的异常信息然后崩溃。请使用刚学的[异常处理](https://so.csdn.net/so/search?q=异常处理&spm=1001.2101.3001.7020)方法修改以下程序，提高用户体验。

   ```python
   import random
   
   secret = random.randint(1, 10)
   print('------------------我爱鱼C工作室------------------')
   temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
   try:
       guess = int(temp)
   except ValueError as reason:
       print('输入类型出错啦@ \n出错类型： %s' % str(reason))
       guess = secret
   while guess != secret:
       temp = input("哎呀，猜错了，请重新输入吧：")
       guess = int(temp)
       if guess == secret:
           print("我草，你是小甲鱼心里的蛔虫吗？！")
           print("哼，猜中了也没有奖励！")
       else:
           if guess > secret:
               print("哥，大了大了~~~")
           else:
               print("嘿，小了，小了~~~")
   print("游戏结束，不玩啦^_^")
   ```

   

2. input() 函数有可能产生两类异常：EOFError（文件末尾endoffile，当用户按下组合键 Ctrl+d 产生）和 KeyboardInterrupt（取消输入，当用户按下组合键 Ctrl+c 产生），再次修改上边代码，捕获处理 input() 的两类异常，提高用户体验

   ```python
   import random
   
   secret = random.randint(1, 10)
   print('------------------我爱鱼C工作室------------------')
   try:
       temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
       guess = int(temp)
   except (KeyboardInterrupt, EOFError) as reason:
       print('用户中断 \n原因： %s' % str(reason))
       guess = secret
   except ValueError as reason:
       print('输入类型出错啦@ \n出错类型： %s' % str(reason))
       guess = secret
   
   while guess != secret:
       temp = input("哎呀，猜错了，请重新输入吧：")
       guess = int(temp)
       if guess == secret:
           print("我草，你是小甲鱼心里的蛔虫吗？！")
           print("哼，猜中了也没有奖励！")
       else:
           if guess > secret:
               print("哥，大了大了~~~")
           else:
               print("嘿，小了，小了~~~")
   print("游戏结束，不玩啦^_^")
   ```

   

3. 尝试一个新的函数 int_input()，当用户输入整数的时候正常返回，否则提示出错并要求重新输入

   ```python
   # 尝试一个新的函数 int_input()，当用户输入整数的时候正常返回，否则提示出错并要求重新输入
   
   def int_input(msg=''):
       flag = True
       try:
           number = input(msg)
           temp = int(number)
       except ValueError as reason:
           print('输入类型出错啦@ \n出错类型： %s' % str(reason))
           flag = False
       while flag:
           if isinstance(temp, int):
               return temp
               break
           else:
               temp = input('error captured, please input again\n')
   
   
   print(int_input())
   ```

   优化的程序：

   ```python
   def int_input(prompt=''):
       while True:
           try:
               int(input(prompt))
               break
           except ValueError:
               print('出错，您输入的不是整数！')
   
   
   int_input('请输入一个整数：')
   ```

   

4. 把文件关闭放在 finally 语句块中执行还是会出现问题，像下边这个代码，当前文件夹中并不存在"My_File.txt"这个文件，那么程序执行起来会发生什么事情呢？你有办法解决这个问题吗？

   ```python
   try:
       f = open('My_File.txt') # 当前文件夹中并不存在"My_File.txt"这个文件T_T
       print(f.read())
   except OSError as reason:
       print('出错啦：' + str(reason))
   finally:
   		f.close()
   
   ```

   ```python
   try:
       f = open('My_File.txt')  # 当前文件夹中并不存在"My_File.txt"这个文件T_T
       print(f.read())
   except OSError as reason:
       print('出错啦：' + str(reason))
   finally:
       if 'f' in locals():  # 如果文件对象变量存在当前局部变量符号表的话，说明打开成功
           f.close()
   ```
   
   

# 034. 丰富的else语句及简洁的with语句

## 知识点

### 丰富的else语句

- 要么怎样，要么不怎样

  - if-else

- 干完了能怎样，干不完就别想怎样 ；

  - 和for 语句或者while 语句搭配

    ```python
    def showMaxFactor(number):
        count = number // 2
        while count > 1:
            if number % count == 0:
                print('%d 的最大约数是 %d' %(number, count))
                break
            count -= 1
        else:
            print('%d 是一个素数' % number)
    
    
    num = int(input('please input a number:'))
    showMaxFactor(num)
    ```

    

- 没有问题，那就干吧

  - 和异常处理搭配

    ```python
    try:
        a = int(input('input a number:'))
    except ValueError:
        print('出错啦！')
    else:
        print(a)
    ```

    

### 间接的with语句

- 一个例子

  ```python
  try:
      f = open('test.txt', 'w')
      for each_line in f:
          print(each_line)
  except OSError as reason:
      print('出错啦！' + str(reason))
  finally:
      f.close()
  ```

  使用with 改进之后：

  ```python
  try:
      with open('test.txt', 'w') as f:
          for each_line in f:
              print(each_line)
  except OSError as reason:
      print('出错啦！' + str(reason))
  ```

- with 语句会monitor 打开的文件，会自动关闭，不需要再用`f.close()` 



## 课后作业

### Quiz

1. 在 Python 中，else 语句能跟哪些语句进行搭配？

   if, while, for 和 try-except

2. 请问以下例子中，循环中的 break 语句会跳过 else 语句吗？

   ```python
   def showMaxFactor(num):
       count = num // 2
       while count > 1:
           if num % count == 0:
               print('%d最大的约数是%d' % (num, count))
               break
           count -= 1
       else:
           print('%d是素数！' % num)
   
   num = int(input('请输入一个数：'))
   showMaxFactor(num)
   ```

   会，因为如果将 else 语句与循环语句（while 和 for 语句）进行搭配，那么只有在循环正常执行完成后才会执行 else 语句块的内容。

3. 请目测以下代码会打印什么内容？

   ```python
   try:
           print('ABC')
   except:
           print('DEF')
   else:
           print('GHI')
   finally:
           print('JKL')
   
   ```

   ABC

   GHI

   JKL

4. 使用什么语句可以使你不必再担心文件打开后却忘了关闭的尴尬？

   ```python
   try:
       with open('data.txt', 'w') as f:
           for each_line in f:
               print(each_line)
   except OSError as reason:
       print('出错啦：' + str(reason))
   ```

   使用with语句

5. 使用 with 语句固然方便，但如果出现异常的话，文件还会自动正常关闭吗？

   with 语句会自动处理文件的打开和关闭，如果中途出现异常，会执行清理代码，然后确保文件自动关闭。g

6. 你可以换一种形式写出下边的伪代码吗？

   ```python
   with A() as a:
       with B() as b:
           suite
   ```

   ```python
   with A() as a, B() as b:
       suite
   ```
   
   

### Practice

1. 使用 with 语句改写以下代码，让 Python 去关心文件的打开与关闭吧。

   ```python
   def file_compare(file1, file2):
       f1 = open(file1)
       f2 = open(file2)
       count = 0 # 统计行数
       differ = [] # 统计不一样的数量
   
       for line1 in f1:
           line2 = f2.readline()
           count += 1
           if line1 != line2:
               differ.append(count)
   
       f1.close()
       f2.close()
       return differ
   
   file1 = input('请输入需要比较的头一个文件名：')
   file2 = input('请输入需要比较的另一个文件名：')
   
   differ = file_compare(file1, file2)
   
   if len(differ) == 0:
       print('两个文件完全一样！')
   else:
       print('两个文件共有【%d】处不同：' % len(differ))
       for each in differ:
           print('第 %d 行不一样' % each)
   ```

   使用with 之后的代码：

   ```python
   def file_compare(file1, file2):
       # f1 = open(file1)
       # f2 = open(file2)
       with open(file1) as f1, open(file2) as f2:
           count = 0  # 统计行数
           differ = []  # 统计不一样的数量
       
           for line1 in f1:
               line2 = f2.readline()
               count += 1
               if line1 != line2:
                   differ.append(count)
                   
           return differ
   
   
   file1 = input('请输入需要比较的头一个文件名：')
   file2 = input('请输入需要比较的另一个文件名：')
   
   differ = file_compare(file1, file2)
   
   if len(differ) == 0:
       print('两个文件完全一样！')
   else:
       print('两个文件共有【%d】处不同：' % len(differ))
       for each in differ:
           print('第 %d 行不一样' % each)
   ```

   

2. 你可以利用异常的原理，修改下面的代码使得更高效率的实现吗？

   ```python
   print('|--- 欢迎进入通讯录程序 ---|')
   print('|--- 1：查询联系人资料  ---|')
   print('|--- 2：插入新的联系人  ---|')
   print('|--- 3：删除已有联系人  ---|')
   print('|--- 4：退出通讯录程序  ---|')
   
   contacts = dict()
   
   while 1:
       instr = int(input('\n请输入相关的指令代码：'))
       
       if instr == 1:
           name = input('请输入联系人姓名：')
           if name in contacts:
               print(name + ' : ' + contacts[name])
           else:
               print('您输入的姓名不再通讯录中！')
   
       if instr == 2:
           name = input('请输入联系人姓名：')
           if name in contacts:
               print('您输入的姓名在通讯录中已存在 -->> ', end='')
               print(name + ' : ' + contacts[name])
               if input('是否修改用户资料（YES/NO）：') == 'YES':
                   contacts[name] = input('请输入用户联系电话：')
           else:
               contacts[name] = input('请输入用户联系电话：')
   
       if instr == 3:
           name = input('请输入联系人姓名：')
           if name in contacts:
               del(contacts[name])         # 也可以使用dict.pop()
           else:
               print('您输入的联系人不存在。')
               
       if instr == 4:
           break
   
   print('|--- 感谢使用通讯录程序 ---|')
   ```

   使用条件语句的代码非常直观明了，但是效率不高。因为程序会两次访问字典的键，一次判断是否存在（例如 `if name in contacts）`，一次获得值（例如 `print(name + ' : ' + contacts[name])`）

   如果利用异常解决方案，我们可以简单避开每次需要使用 in 判断是否键存在字典中的操作。因为只要当键不存在字典中时，会触发 KeyError 异常，利用此特性我们可以修改代码如下：
   
   ```python
   print('|--- 欢迎进入通讯录程序 ---|')
   print('|--- 1：查询联系人资料  ---|')
   print('|--- 2：插入新的联系人  ---|')
   print('|--- 3：删除已有联系人  ---|')
   print('|--- 4：退出通讯录程序  ---|')
   
   contacts = dict()
   
   while 1:
       instr = int(input('\n请输入相关的指令代码：'))
   
       if instr == 1:
           name = input('请输入联系人姓名：')
           try:
               print(name + ' : ' + contacts[name])
           except KeyError:
               print('您输入的姓名不再通讯录中！')
   
       if instr == 2:
           name = input('请输入联系人姓名：')
           try:
               print('您输入的姓名在通讯录中已存在 -->> ', end='')
               print(name + ' : ' + contacts[name])
               if input('是否修改用户资料（YES/NO）：') == 'YES':
                   contacts[name] = input('请输入用户联系电话：')
           except KeyError:
               contacts[name] = input('请输入用户联系电话：')
   
       if instr == 3:
           name = input('请输入联系人姓名：')
           try:
               del (contacts[name])  # 也可以使用dict.pop()
           except KeyError:
               print('您输入的联系人不存在。')
   
       if instr == 4:
           break
   
   print('|--- 感谢使用通讯录程序 ---|')
   ```
   
   

# 035. 图形用户界面入门：EasyGui

## 知识点

- [官方文档](http://easygui.sourceforge.net/)

- 导入easygui模块 - 3种方法； 推荐使用`import easygui as g`

  ```python
  >>> import easygui
  >>> 
  >>> easygui.msgbox('hi')
  'OK'
  >>> from easygui import *
  >>> 
  >>> msgbox('hi')
  'OK'
  >>> 
  >>> import easygui as g
  >>> g.msgbox('hi')
  'OK'
  ```

  

- 使用easygui

  - 建议不要在IDLE上运行Easygui

  - 一个简单的例子

    ```python
    import easygui as g
    import sys
    
    while 1:
        g.msgbox("嗨，欢迎进入第一个界面小游戏")
        msg = "请问你但愿在鱼C工做室学习到什么知识呢"
        title="小游戏互动"
        choices=["谈恋爱","编程","OOXX","琴棋书画"]
        choice=g.choicebox(msg,title,choices)
    
        #note that we convert choice to string,in case
        #the user cancelled the choice,and we got None
        g.msgbox("你的选择是:"+str(choice),"结果")
        msg="你但愿从新开始小游戏吗?"
        title=" 请选择"
        if g.ccbox(msg,title):  #show a Contiue/Cancel dialog
            pass #user chose Contonue
        else:
            sys.exit(0)  #user chose Cancel
    ```

    

## 知识点 - 补充

0. 安装 EasyGUI

   官网：https://github.com/robertlugg/easygui

   使用 pip 进行安装：

   [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714172112548-1358634293.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714172112548-1358634293.png)

 

1. 什么是 EasyGUI？

   EasyGUI 是 Python 中一个非常简单的 GUI 编程模块，不同于其他的 GUI 生成器，它不是事件驱动的。相反，所有的 GUI 交互都是通过简单函数调用就可以实现。

   EasyGUI 为用户提供了简单的 GUI 交互接口，不需要程序员知道任何有关 tkinter，框架，部件，回调或 lambda 的任何细节。

   EasyGUI 可以很好地兼容 Python 2 和 3，并且不存在任何依赖关系。

   EasyGUI 是运行在 Tkinter 上并拥有自身的事件循环，而 IDLE 也是 Tkinter 写的一个应用程序并也拥有自身的事件循环。因此当两者同时运行的时候，有可能会发生冲突，且带来不可预测的结果。因此如果你发现你的 EasyGUI 程序有这样的问题，请尝试在 IDLE 外去运行你的程序。

 

2. 一个简单的例子

   在 EasyGui 中，所有的 GUI 互动均是通过简单的函数调用，下边一个简单的例子告诉你 EasyGui 确实很 Easy！

   ```python
    1 import easygui as g
    2 import sys
    3 
    4 while 1:
    5         g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
    6 
    7         msg ="请问你希望在鱼C工作室学习到什么知识呢？"
    8         title = "小游戏互动"
    9         choices = ["谈恋爱", "编程", "OOXX", "琴棋书画"]
   10         
   11         choice = g.choicebox(msg, title, choices)
   12 
   13         # 注意，msgbox的参数是一个字符串
   14         # 如果用户选择Cancel，该函数返回None
   15         g.msgbox("你的选择是: " + str(choice), "结果")
   16 
   17         msg = "你希望重新开始小游戏吗？"
   18         title = "请选择"
   19 
   20         # 弹出一个Continue/Cancel对话框
   21         if g.ccbox(msg, title):
   22                 pass            # 如果用户选择Continue
   23         else:
   24                 sys.exit(0)     # 如果用户选择Cancel
   ```

   

3. EasyGUI 的各种功能演示

   要运行 EasyGUI 的演示程序，在命令行调用 EasyGUI 是这样的：

   `python easygui.py`

   或者可以从 IDE（例如 IDLE, PythonWin, Wing, 等等）上调用：

   ```python
   >>> import easygui
   >>> easygui.egdemo()
   ```

   成功调用后将可以尝试 EasyGUI 拥有的各种功能，并将结果打印至控制台。

   [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714192216412-982535486.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714192216412-982535486.png)

 

4. 导入 EasyGUI

   为了使用 EasyGUI 这个模块，你应该先导入它。

   最简单的导入语句是：

   ```
   import easygui
   ```

   如果使用上面这种形式导入的话，那么你使用 EasyGUI 的函数的时候，必须在函数的前面加上前缀 easygui，像这样：

   ```
   easygui.msgbox(...)
   ```

   另一种选择是导入整个 EasyGUI 包：

   ```
   from easygui import *
   ```

   这使得我们更容易调用 EasyGUI 的函数，可以直接这样编写代码：

   ```
   msgbox(...)
   ```

   第三种方案是使用类似下边的 import 语句：

   ```
   import easygui as g
   ```

   这种方法还可以让你保持 EasyGUI 的命名空间，同时减少你的打字数量。

   导入之后就可以这么调用 EasyGUI 的函数：

   ```
   g.msgbox(...)
   ```

   

5. 使用 EasyGUI

   一旦你的模块导入 EasyGUI，GUI 操作就是一个简单的调用 EasyGUI 函数的几个参数的问题了。

   例如，使用 EasyGUI 来实现世界上最著名的打招呼：

   ```python
   import easygui as g
   
   g.msgbox("Hello, world!")
   ```

   [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714192630885-1374238834.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714192630885-1374238834.png)

 

6. EasyGUI 函数的默认参数

   对于所有对话框而言，前两个参数都是消息主体和对话框标题。

   按照这个规律，在某种情况下，这可能不是理想的布局设计（比如当对话框在获取目录或文件名的时候会选择忽略消息参数），但保持这种一致性且贯穿于所有的窗口部件是更为得体的考虑！
   绝大部分的 EasyGUI 函数都有默认参数，几乎所有的组件都会显示消息主体和对话框标题。

   标题默认是空字符串，消息主体通常有一个简单的默认值。

   这使得你可以尽可能少的去设置参数，比如 msgbox() 函数标题部分的参数是可选的，因此你调用 msgbox() 的时候只需要指定一个消息参数即可，例如：

   ```
   >>> msgbox('我爱hale^_^')
   ```

   当然你也可以指定标题参数和消息参数，例如：

   ```
   >>> msgbox('我爱hale^_^', 'AG自述')
   ```

   [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714193213861-730996074.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714193213861-730996074.png)

    

   在各类按钮组件里，默认的消息是 “Shall I continue?”，所以你可以不带任何参数地去调用它们。

   这里我们演示不带任何参数地去调用 ccbox()，当选择 “cancel” 或关闭窗口的时候返回一个布尔类型的值：

   ```
   if ccbox(): 
           pass         # 用户选择继续
   else: 
           return      # 用户选择取消
   ```

   **这里return会报错SyntaxError: 'return' outside function**

   **`return`关键字只能在`def`自定义函数里面使用，（在`while`循环中只能使用`break`关键字来结束循环！这里没有自定义函数，所以不能出现`return`这样的关键字！）**

 

7. 使用关键字参数调用 EasyGUI 的函数

   调用 EasyGUI 函数还可以使用关键字参数哦。

   现在假设你需要使用一个按钮组件，但你不想指定标题参数（第二个参数），你仍可以使用关键字参数的方法指定 choices 参数（第三个参数），像这样：

    

   ```
   >>> choices = ['愿意', '不愿意', '有钱的时候就愿意']
   >>> reply = choicebox('你愿意购买资源打包支持小甲鱼吗？', choices = choices)
   ```

    

   [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714194606615-944741941.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714194606615-944741941.png)

    

   

8. 使用按钮组件

   根据需求，EasyGUI 在 buttonbox() 上建立了一系列的函数供调用。

   

   8.1.	msgbox()

   msgbox(msg='(Your message goes here)', title=' ', ok_button='OK', image=None, root=None)

   msgbox() 显示一个消息和提供一个 “OK” 按钮，你可以指定任意的消息和标题，你甚至可以重写 “OK” 按钮的内容。

   重写 “OK” 按钮最简单的方法是使用关键字参数：

    

   ```
   >>> msgbox("我一定要学会编程!", ok_button="加油!")
   ```

    

   [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714194911513-2109612713.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714194911513-2109612713.png)

    

    8.2.	ccbox()

   ccbox(msg='Shall I continue?', title=' ', choices=('C[o]ntinue', 'C[a]ncel'), image=None, default_choice='C[o]ntinue', cancel_choice='C[a]ncel')

   ccbox() 提供一个选择：“C[o]ntinue” 或者 “C[a]ncel”，并相应的返回 True 或者 False。

   注意：“C[o]ntinue” 中的 [o] 表示快捷键，也就是说当用户在键盘上敲一下 o 字符，就相当于点击了 “C[o]ntinue” 按键。

   

   8.3.	ynbox()

   ynbox(msg='Shall I continue?', title=' ', choices=('[<F1>]Yes', '[<F2>]No'), image=None, default_choice='[<F1>]Yes', cancel_choice='[<F2>]No')

   跟 ccbox() 一样，只不过这里默认的 choices 参数值不同而已，[<F1>] 表示将键盘上的 F1 功能按键作为 “Yes” 的快捷键使用。

   

   8.4.	buttonbox()

   buttonbox(msg='', title=' ', choices=('Button[1]', 'Button[2]', 'Button[3]'), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True)

   可以使用 buttonbox() 定义自己的一组按钮，buttonbox() 会显示一组由你自定义的按钮。

   当用户点击任意一个按钮的时候，buttonbox() 返回按钮的文本内容。

   如果用户点击取消或者关闭窗口，那么会返回默认选项（第一个选项）。

   请看例子：

   [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714200023069-1294875944.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714200023069-1294875944.png)

   

   8.5.	 indexbox()

   *indexbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None, default_choice='Yes', cancel_choice='No')*

   基本跟 buttonbox() 一样，区别就是当用户选择第一个按钮的时候返回序号 0， 选择第二个按钮的时候返回序号 1。

   

   8.6.	boolbox()

   *boolbox(msg='Shall I continue?', title=' ', choices=('[Y]es', '[N]o'), image=None, default_choice='Yes', cancel_choice='No')*

   如果第一个按钮被选中则返回 True，否则返回 False。

   

9. 如何在 buttonbox 里边显示图片

   当你调用一个 buttonbox 函数（例如 msgbox(), ynbox(), indexbox() 等等）的时候，你还可以为关键字参数 image 赋值，可以设置一个 .gif 格式的图像（PNG 格式的图像也是支持的哦^_^）：

   ```
   buttonbox('大家说我长得帅吗？', image='turtle.gif', choices=('帅', '不帅', '!@#$%'))
   ```

   这里Python3需要安装pillow库才可加载jpg等其他图像

   [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714201305682-1560100367.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714201305682-1560100367.png)

    

    

    

10. 为用户提供一系列选项

    

    10.1.	choicebox()

    *choicebox(msg='Pick an item', title='', choices=[], preselect=0, callback=None, run=True)*

    按钮组件方便提供用户一个简单的按钮选项，但如果有很多选项，或者选项的内容特别长的话，更好的策略是为它们提供一个可选择的列表。 
    choicebox() 为用户提供了一个可选择的列表，使用序列（元祖或列表）作为选项，这些选项会按照字母进行排序。

    另外还可以使用键盘来选择其中一个选项（比较纠结，但一点儿都不重要）：

    - 例如当按下键盘上的 “g” 键，将会选中的第一个以 “g” 开头的选项。再次按下 “g” 键，则会选中下一个以 “g” 开头的选项。在选中最后一个以 “g” 开头的选项的时候，再次按下 “g” 键将重新回到在列表的开头的第一个以 “g” 开头的选项。
    - 如果选项中没有以 “g” 开头的，则会选中字符排序在 “g” 之前（“f”）的那个字符开头的选项
    - 如果选项中没有字符的排序在 “g” 之前的，那么在列表中第一个元素将会被选中。 [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714201858460-688480039.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714201858460-688480039.png)

    10.2.	multchoicebox()

    *multchoicebox(msg='Pick an item', title='', choices=[], preselect=0, callback=None, run=True)*

    multchoicebox() 函数也是提供一个可选择的列表，与 choicebox() 不同的是，multchoicebox() 支持用户选择 0 个，1 个或者同时选择多个选项。

    multchoicebox() 函数也是使用序列（元祖或列表）作为选项，这些选项显示前会按照不区分大小写的方法排好序。

    [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714202023050-15996395.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714202023050-15996395.png)

    ​    

​	

11. 让用户输入消息

    

    11.1.	enterbox()

    *enterbox(msg='Enter something.', title=' ', default='', strip=True, image=None, root=None)*

    enterbox() 为用户提供一个最简单的输入框，返回值为用户输入的字符串。

    默认返回的值会自动去除首尾的空格，如果需要保留首尾空格的话请设置参数 strip=False。

    [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714202400343-1120620975.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714202400343-1120620975.png)

    

    11.2.	integerbox()

    *integerbox(msg='', title=' ', default=None, lowerbound=0, upperbound=99, image=None, root=None)*

    integerbox() 为用户提供一个简单的输入框，用户只能输入范围内（lowerbound 参数设置最小值，upperbound 参数设置最大值）的整型数值，否则会要求用户重新输入。

    

    11.3 multenterbox()

    *multenterbox(msg='Fill in values for the fields.', title=' ', fields=[], values=[], callback=None, run=True)*

    multenterbox() 为用户提供多个简单的输入框，要注意以下几点：

    - 如果用户输入的值比选项少的话，则返回列表中的值用空字符串填充用户未输入的选项。
    - 如果用户输入的值比选项多的话，则返回的列表中的值将截断为选项的数量。
    - 如果用户取消操作，则返回域中的列表的值或者 None 值。

    实现如下图（*源代码在第35讲的课后作业中^_^*）：

    [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714202836630-1172692665.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714202836630-1172692665.png)


​     

12. 让用户输入密码

    有时候可能需要让用户输入密码等敏感信息，那么界面看上去应该是这样的：******。

    12.1.	passwordbox()

    *passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None)*

    passwordbox() 跟 enterbox() 样式一样，不同的是用户输入的内容用星号（*）显示出来，该函数返回用户输入的字符串：

    [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714203118959-2140893646.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714203118959-2140893646.png)

     ***12.2 multpasswordbox()***

    *multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=(), callback=None, run=True)*

    multpasswordbox() 跟 multenterbox() 使用相同的接口，但当它显示的时候，最后一个输入框显示为密码的形式（*）：

    [![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714203407291-1287204336.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714203407291-1287204336.png)

 

**13. 显示文本**

EasyGUI 还提供函数用于显示文本。

***13.1 textbox()***

*textbox(msg='', title=' ', text='', codebox=False, callback=None, run=True)*

textbox() 函数默认会以比例字体（参数 codebox=True 设置为等宽字体）来显示文本内容（自动换行），这个函数适合用于显示一般的书面文字。

注：text 参数设置可编辑文本区域的内容，可以是字符串、列表或者元祖类型。

[![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714204601580-1727704146.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714204601580-1727704146.png)

 

 

 ***13.2 codebox()***

*codebox(msg='', title=' ', text='')*

codebox() 以等宽字体显示文本内容（不自动换行），相当于 textbox(codebox=True)

注：等宽字体很丑的，但适合代码编写，不信你试试看@_@


**14. 目录与文件**

GUI 编程中一个常见的场景是要求用户输入目录及文件名，EasyGUI 提供了一些基本函数让用户来浏览文件系统，选择一个目录或文件。

***14.1 diropenbox()***

*diropenbox(msg=None, title=None, default=None)*

diropenbox() 函数用于提供一个对话框，返回用户选择的目录名（带完整路径哦），如果用户选择 “Cancel” 则返回 None。

default 参数用于设置默认的打开目录（请确保设置的目录已存在）。

[![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714212045322-541743005.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714212045322-541743005.png)

 

 ***14.2 fileopenbox()***

*fileopenbox(msg=None, title=None, default='\*', filetypes=None, multiple=False)*

fileopenbox() 函数用于提供一个对话框，返回用户选择的文件名（带完整路径哦），如果用户选择 “Cancel” 则返回 None。

关于 default 参数的设置方法：

- default 参数指定一个默认路径，通常包含一个或多个通配符。
- 如果设置了 default 参数，fileopenbox() 显示默认的文件路径和格式。
- default 默认的参数是 '*'，即匹配所有格式的文件。


例如：

- default="c:/fishc/*.py" 即显示 C:\fishc 文件夹下所有的 Python 文件。
- default="c:/fishc/test*.py" 即显示 C:\fishc 文件夹下所有的名字以 test 开头的 Python 文件。


关于 filetypes 参数的设置方法：

- 可以是包含文件掩码的字符串列表，例如：filetypes = ["*.txt"]
- 可以是字符串列表，列表的最后一项字符串是文件类型的描述，例如：filetypes = ["*.css", ["*.htm", "*.html", "HTML files"]]


最后是 multiple 参数，如果为 True 则表示可以同时选择多个文件。

[![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714213405295-1488798206.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714213405295-1488798206.png)

 

 

***14.3 filesavebox()***

*filesavebox(msg=None, title=None, default='', filetypes=None)*

filesavebox() 函数提供一个对话框，让用于选择文件需要保存的路径（带完整路径哦），如果用户选择 “Cancel” 则返回 None。

default 参数应该包含一个文件名（例如当前需要保存的文件名），当然也可以设置为空的，或者包含一个文件格式掩码的通配符。

filetypes 参数的设置方法请参考 fileopenbox() 函数。

[![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714214027910-1110083280.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714214027910-1110083280.png)

 

 **15. 记住用户的设置**

***15.1 EgStore***

GUI 编程中一个常见的场景就是要求用户设置一下参数，然后保存下来，以便下次用户使用你的程序的时候可以记住他的设置。

为了实现对用户的设置进行存储和恢复这一过程，EasyGUI 提供了一个叫做 EgStore 的类。

为了记住某些设置，你的应用程序必须定义一个类（下面案例中的 “Settings”）继承自 EgStore 类。

然后你的应用程序必须创建一个该类的实例化对象（下面案例中的 “settings”）。

设置类的构造函数（__init__ 方法）必须初始化所有的你想要它所记住的那些值。

一旦你这样做了，你就可以在 settings 对象中通过设定值去实例化变量，从而很简单地记住设置。

之后使用 settings.store() 方法在硬盘上持久化保存。

2020-07-14 21:53:13  类的知识暂未掌握！！！

下面创建一个叫做 “Settings” 的类：

```
from easygui import EgStore

# 定义一个叫做“Settings”的类，继承自EgStore类
class Settings(EgStore):

    def __init__(self, filename):  # 需要指定文件名
        # 指定要记住的属性名称
        self.author = ""
        self.book = ""

        # 必须执行下面两个语句
        self.filename = filename
        self.restore()

# 创建“Settings”的实例化对象“settings”
settingsFilename = "settings.txt"
settings = Settings(settingsFilename)

author = "小甲鱼"
book = "《零基础入门学习Pyhon》"

# 将上面两个变量的值保存到“settings”对象中
settings.author = author
settings.book = book
settings.store()
print("\n保存完毕\n")
```



 **16. 捕获异常**

***exceptionbox()***

使用 EasyGUI 编写 GUI 程序，有时候难免会产生异常。当然这取决于你如何运行你的应用程序，当你的应用程序崩溃的时候，堆栈追踪可能会被抛出，或者被写入到 stdout 标准输出函数中。

EasyGUI 通过 exceptionbox() 函数提供了更好的方式去处理异常。

当异常出现的时候，exceptionbox() 会将堆栈追踪显示在一个 codebox() 中，并且允许你做进一步的处理。

exceptionbox() 很容易使用，下面举个例子：

```
try:
        print('I Love FishC.com!')
        int('FISHC') # 这里会产生异常
except:
        exceptionbox()
```

[![img](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714220025132-312819337.png)](https://img2020.cnblogs.com/blog/2096605/202007/2096605-20200714220025132-312819337.png)

 

## 课后作业

### Quiz





### Practice

1. 先练练手，把我们的刚开始的那个猜数字小游戏加上界面吧?

   ![img](https://img2018.cnblogs.com/blog/1442115/201812/1442115-20181209223851175-1976371461.png)

   ```python
   # 先练练手，把我们的刚开始的那个猜数字小游戏加上界面吧?
   
   import random
   import sys
   
   import easygui as g
   
   g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")
   secret = random.randint(1, 10)
   msg = "不妨猜一下小甲鱼现在心里想的是哪个数字（1~10）："
   title = "数字小游戏"
   guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
   
   # 如果选择cancel，直接退出
   if not guess:
       sys.exit()
       
   while True:
       if guess == secret:
           g.msgbox("我草，你是小甲鱼心里的蛔虫吗？！")
           g.msgbox("哼，猜中了也没有奖励！")
           break
       else:
           if guess > secret:
               g.msgbox("哥，大了大了~~~")
           else:
               g.msgbox("嘿，小了，小了~~~")
           guess = g.integerbox(msg, title, lowerbound=1, upperbound=10)
   
   g.msgbox("游戏结束，不玩啦^_^")
   
   
   ```

   

2. 实现一个用于登记用户账号信息的界面（如果是带*号的必填项，要求一定要有输入并且不能是空格）

   ![img](https://img2018.cnblogs.com/blog/1442115/201812/1442115-20181209223900309-1800557256.png)

   ```python
   # 实现一个用于登记用户账号信息的界面（如果是带*号的必填项，要求一定要有输入并且不能是空格）
   
   import easygui as g
   import sys
   
   
   message = "【真实姓名】为必填项 \n【手机号码】为必填项 \n【*E-mail地址】为必填项 "
   title = "账号中心"
   fields = ['*用户名', '*真实姓名', '固定电话', '*手机号码',  'QQ', '*E-mail']
   result = g.multenterbox(msg=message, title=title, fields=fields, values=['小甲鱼'], callback=None, run=True)
   while True:
       if not result:
           sys.exit()
       elif result[1].isspace() or not result[1]:
           g.msgbox('【真实姓名】为必填项, 一定要有输入并且不能是空格')
       elif result[3].isspace() or not result[3]:
           g.msgbox('【手机号码】为必填项, 一定要有输入并且不能是空格')
       elif result[5].isspace() or not result[5]:
           g.msgbox('【E-mail】为必填项, 一定要有输入并且不能是空格')
       else:
           break
       result = g.multenterbox(msg=message, title=title, fields=fields, values=['小甲鱼'], callback=None, run=True)
   
   g.msgbox('登记成功@！')
   ```

   

3. 提供一个文件浏览框，让用户选择需要打开的文本文件，打开并显示文件内容

   ![img](https://img2018.cnblogs.com/blog/1442115/201812/1442115-20181209223908751-1868690450.png)

   ```python
   # 提供一个文件浏览框，让用户选择需要打开的文本文件，打开并显示文件内容
   
   import easygui as g
   import sys
   
   f_name = g.fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
   if f_name:
       message = "文件" + f_name + "的内容如下： "
       title = "显示文件内容"
   
       with open(f_name, 'r') as f:
           f_content = f.readlines()
       g.textbox(msg=message, title=title, text=f_content, codebox=False, callback=None, run=True)
   
   else:
       sys.exit()
   ```

   

4. 在上一题的基础上增强功能：当用户点击“OK”按钮的时候，比较当前文件是否修改过，如果修改过，则提示“覆盖保存”、“放弃保存”或“另存为…”并实现相应的功能。

   ![img](https://img2018.cnblogs.com/blog/1442115/201812/1442115-20181209223915368-1198875933.png)

   ```python
   # 在上一题的基础上增强功能：当用户点击“OK”按钮的时候，比较当前文件是否修改过，
   # 如果修改过，则提示“覆盖保存”、“放弃保存”或“另存为…”并实现相应的功能。
   
   import easygui as g
   import sys
   import os.path
   
   
   def mfile_action(m_choice):
       if m_choice == '覆盖保存':
           with open(f_name, 'r') as fo:
               temp_content = fo.readlines()
               with open(f_name, 'w') as fw:
                   fw.writelines(temp_content)
       elif m_choice == '放弃保存':
           with open(f_name, 'w') as fw:
               fw.writelines(f_content)
       elif m_choice == '另存为':
           # with open(f_name, 'r') as fo:
           #     temp_content = fo.readlines()
           new_fname = g.filesavebox(msg=None, title=None, default='', filetypes=None)
           if new_fname:
               with open(f_name, 'r') as fo:
                   temp_content = fo.readlines()
               with open(new_fname, 'x') as fs:
                   fs.writelines(temp_content)
       else:
           sys.exit()
   
   
   f_name = g.fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
   old_mtime = os.path.getmtime(f_name)
   if f_name:
       message = "文件" + f_name + "的内容如下： "
       title = "显示文件内容"
   
       with open(f_name, 'r') as f:
           f_content = f.readlines()
           print(f_content)
       if g.textbox(msg=message, title=title, text=f_content, codebox=False, callback=None, run=True):
           new_mtime = os.path.getmtime(f_name)
           if new_mtime != old_mtime:
               warn_msg = '检测到文件内容发生改变，请选择以下操作：'
               warn_title = '警告'
               warn_choices = ['覆盖保存', '放弃保存', '另存为']
               choice = g.buttonbox(msg=warn_msg, title=warn_title, choices=warn_choices, image=None, images=None,
                           default_choice=None, cancel_choice=None, callback=None, run=True)
               mfile_action(choice)
   else:
       sys.exit()
   
   ```

   

5. 写一个程序统计你当前代码量的总和，并显示离十万行代码量还有多远？ 

   要求一：递归搜索各个文件夹 要求二：显示各个类型的源文件和源代码数量 要求三：显示总行数与百分比

   ![img](https://img2018.cnblogs.com/blog/1442115/201812/1442115-20181209223924767-1833087716.png)

   ![img](https://www.programminghunter.com/images/121/3f/3f4dda2326c5bf9b6508d481ad974ee1.png)
   
   

```python
# 写一个程序统计你当前代码量的总和，并显示离十万行代码量还有多远？
# 要求一：递归搜索各个文件夹 要求二：显示各个类型的源文件和源代码数量 要求三：显示总行数与百分比

import easygui as g
import sys
import os
import os.path


def code_cal(dir_path):
    format_list = ['.py', '.tf', '.sh']
    code_lines = 0
    ext_dic = {'.py': [0, 0], '.tf': [0, 0], '.sh':[0, 0]}

    # os.walk() 返回的是一个三元组迭代器，有三元组参数，通过for 循环使用
    for folder, sub_folders, sub_files in os.walk(dir_path):
        for each_file in sub_files:
            ext_temp = os.path.splitext(each_file)[1]

            if ext_temp in format_list:

                ext_dic[ext_temp][0] += 1

                with open(os.path.join(folder, each_file), 'r') as f_py:
                    len_temp = len(f_py.readlines())
                    ext_dic[ext_temp][1] += len_temp
                    code_lines += len_temp

    return code_lines, ext_dic


f_path = g.diropenbox(msg=None, title=None, default=None)

if f_path:
    total_lines, ext_row_line = code_cal(f_path)
    message = '您目前共累计编写了 %d 行代码，' % total_lines + '完成进度 {:.2%} \n'.format(total_lines/100000) + ' 离 %d 行代码还差 %d 行，请继续努力' % ( 100000, 100000-total_lines)
    text_title = '统计结果'
    text_content = ''
    for each in ext_row_line.keys():
        text_content += '[%s]源文件 %d 个，源代码 %d 行 \n' % (each, ext_row_line[each][0], ext_row_line[each][1])
    g.textbox(msg=message, title=text_title, text=text_content, codebox='', callback=None, run=True)
else:
    sys.exit()

```

