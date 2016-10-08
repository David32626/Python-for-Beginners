'''
Import module example
'''
import math
print (math.factorial(3))
print (math.fsum([1, 1, 1]))
print (math.cos(math.pi))

'''
Write your module
'''
import calculator
print (calculator.plus(2, 3))
print (calculator.minus(8, 5))
print (calculator.multiplied(3, 4))
print (calculator.divided(10, 5))

'''
Import third- party packages
pip install numpy
'''
import numpy
a = numpy.arange(15).reshape(3, 5)
print (a)

'''
Import third- party packages
change import module name
'''
import numpy as np
a = np.arange(15).reshape(3, 5)
print (a)

'''
from xxx import yyy
'''
from orderedlist import OrderedList
mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print (mylist.size())
print (mylist.search(93))
print (mylist.search(100))

'''
time module example
datetime(), date(), time(), today()
import timedelta

'''
import time
print (time.localtime())
print (time.ctime())

time.sleep(2)

'''
datetime module example
'''
from datetime import datetime
print (datetime.today())
print (datetime.now())

from datetime import timedelta
print (datetime.now()  + timedelta(hours = 1))

'''
os module example
'''
import os
now = os.getcwd()
print (os.getcwd())
print (os.listdir())
workspace = 'C:\\Users\\hubert\\Desktop\\github\\Python-for-Beginners\\src\\ch7\\workspace'
os.chdir(workspace)
print (os.getcwd())
os.chdir(now)

for file in os.walk(now):
    print (file)

#os.mkdir('test1')
#os.rename('test1', 'test2')
#os.remove('test2/doc.txt')
#os.rmdir('test2')

'''
os.path module example
'''
file = 'C:\\Users\\hubert\\Desktop\\github\\Python-for-Beginners\\src\\ch7'
print (os.path.abspath(file))
print (os.path.dirname(file))
print (os.path.basename(file))

print (os.path.exists(file))
