'''
except example
'''
n1 = 10
n2 = 0
print (n1 / n2)

'''
built-in exceptions example
'''
try:
    n1 = 10
    n2 = 0
    print (n1 / n2)
except ZeroDivisionError as e:
    print ('ZeroDivisionError: ',e)

'''
raise example
'''
try:
    raise NameError('hello pycone')
except NameError:
    print('An exception flew by!')

try:
    n1 = 10
    n2 = 0
    if n2 == 0:
        raise ZeroDivisionError("Divided by zero.")
    print (n1 / n2)
except ZeroDivisionError as e:
    print ('ZeroDivisionError: ',e)

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


# Exception hierachy
try:
    n1 = 10
    n2 = 0
    if n2 == 0:
        raise ZeroDivisionError("Divided by zero.")
    print (n1 / n2)


except ArithmeticError as e:
    print("ArithmetricError: ",e)
except ZeroDivisionError as e:
    print ('ZeroDivisionError: ',e)
except:
    print("BaseException: ")