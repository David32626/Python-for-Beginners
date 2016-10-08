'''
Function example
'''
# ((a + b) * c) / d
def compute(a, b, c, d):
    return ((a + b) * c) / d

print (compute(2, 2, 2, 2))

'''
Recursive example
'''
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

def fibonacci(n):
    if n >1 :
        return fibonacci(n -1) + fibonacci(n - 2)
    else:
        return 1

print (factorial(3))
print (fibonacci(3))

'''
Function overloading example
'''
def func(a, b, c):
    return a + b + c

def func(a, b, c):
    return a * b * c

print (func(1, 2, 3))


'''
Gobal variable, Local variable example
'''
x = 10
def compute_method1(a, b):
    answer = x + (a + b)
    return answer

def compute_method2(a, b):
    x = 5
    answer = x + (a + b)
    return answer

print (compute_method1(3, 5))
print (compute_method2(3, 5))

'''
Bubble sort example
'''
def bubble_sort(number_list):
    for j in range(len(number_list)-1,0,-1):
        for i in range(j):
            if number_list[i]>number_list[i+1]:
                temp = number_list[i]
                number_list[i] = number_list[i+1]
                number_list[i+1] = temp

number_list = [22,11,44,33,99,55,77,66,88]
bubble_sort(number_list)
print (number_list)