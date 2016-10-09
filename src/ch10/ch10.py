'''
try, except example
'''
numbers = [2, 4, 6, 8, 10]
sum_number = 0
for number in numbers:
    sum_number = number + sum_number
print (sum_number)

'''
#SyntaxError: invalid syntax
numbers = [2, 4, 6, 8, 1o]
sum_number = 0
for number in numbers:
    sum_number = number + sum_number
print (sum_number)
'''

try:
    numbers = [2, 4, 6, 8]
    sum_number = 0
    error_number = '1o'
    for number in numbers:
        sum_number = number + sum_number
    sum_number + error_number
    print (sum_number)
except TypeError as e:
    print (e)

'''
StopIteration example
'''
numbers = iter([1, 2, 3])
print (next(numbers))
print (next(numbers))
print (next(numbers))
#print (next(numbers))

def for_in(iterator):
    try:
        while True:
            print (next(iterator))
    except StopIteration:
        pass
for_in(iter([1, 2, 3]))

'''
built-in exceptions example
'''
try:
    dividend = 10
    divisor = 0
    print (dividend / divisor)
except ArithmeticError as e:
    print ('ArithmeticError')
except ZeroDivisionError as e:
    print ('ZeroDivisionError')

'''
# can not use ctrl + c to stop the program
while True:
    try:
        print ('hello pycone')
    except:
        print ('stop')
'''
'''
# can use ctrl + c to stop the program
while True:
    try:
        print ('hello pycone')
    except Exception:
        print ('stop')
'''

'''
raise example
'''
try:
    raise NameError('hello pycone')
except NameError:
    print('An exception flew by!')

'''
try, except, else, finally example
'''
number1 = 1
number2 = 2
try:
    if number1 < number2:
        print(n)
except:
    print("except")
else:
    print("else except")
finally:
    print("finally")
 
print("after exception")