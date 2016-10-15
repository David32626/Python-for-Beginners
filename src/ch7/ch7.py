'''
Write your module
'''
import calculator
print (calculator.plus(2, 3))
print (calculator.minus(8, 5))
print (calculator.multiplied(3, 4))
print (calculator.divided(10, 5))

'''
datetime module example
'''
from datetime import datetime
d1 = datetime.now()
print(d1)
print(d1.date())

d2 = datetime(2016,10,17)
print(d2)

delta = d2 - d1
print(delta)
print(delta.days)
print(delta.seconds)

s1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(s1,type(s1))

d1 = datetime.strptime("2016-10-15 15:26:13","%Y-%m-%d %H:%M:%S")
print(d1,type(d1))


'''
os module example
'''
import os
print (os.getcwd())
print (os.listdir())
os.mkdir("test")
print (os.listdir())
os.rmdir("test")
print (os.listdir())

