'''
Default argument
'''
def hello(name="David"):
    print("Hello,",name)

hello()
hello("John")

'''
關鍵字引數
'''
def student(name,age,score):
    print(name,"is",age,"years old, and got",score,"scores.")

student("David",18,90)
student(name="John",age=20,score=100)

'''
不定參數
'''
def sum(*num):
    total = 0
    for n in num:
        total += n
    return total

print("sum = ",sum(1,2,3,4,5,6))

'''
不定關鍵字引數
'''
def sum(**scores):
    total = 0
    for subject, score in scores.items():
        print(subject,"is",score)
        total += score
    return total

print("Total score = ",sum(Chinses=88,English=70,math=85,Science=95,Social=76))

'''
Full arguments
'''
def some(a,b=0,*c,**d):
    print("a =",a)
    print("b =",b)
    print("c =",c)
    print("d =",d)

some(10,20,30,40,name="David",age=18)


'''
Recursive example
'''
def factorial_rec(n):
    if n > 1:
        return n * factorial_rec(n - 1)
    else:
        return 1


def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def fibonacci(n):
    if n >1 :
        return fibonacci(n -1) + fibonacci(n - 2)
    else:
        return 1

print (factorial(3))
print (fibonacci(3))

'''
Pass by value, pass by reference
'''
def foo(a):
    print(id(a))
    a += 1

num = 1
print(id(num))
foo(num)
print(num)

def foo(a):
    print(id(a))
    a.append(1)

aList = []
print(id(aList))
foo(aList)
print(aList)

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