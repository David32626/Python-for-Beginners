'''
List example
'''
numbers = [1, 2]
numbers.append(3)
numbers.remove(3)
len(numbers)
numbers.pop()
numbers = [5, 7, 1, 2, 3]
numbers.sort()
numbers[0]
numbers[1]
numbers[2] = 'hello python'
print (numbers)

numbers = [[1,2,3],[4,5,6]]

students = []
students.append(['David', 123, True])
students.append(['Hubert', 321, False])
print (students)
print (type(students))

students = ['David', 'Hubert', 'Kobe', 'Curry']
students[0:2]
students[:4]
students[0:]
students[:]
students[:-1]

name = 'David'
name[0:2]
name[:4]
name[0:]
name[:]
name[:-1]

name[0:4:1]
name[1::1]
name[2::2]
name[::2]
name[::-1]

'''
Set example
'''
Warriors = set()
Warriors.add('Curry')
Warriors.add('Thompson')
Warriors.add('Durant')
Warriors.remove('Durant')

print ('David' in students)
{'Hubert', 'David', 'Kobe'}
#{{'Hubert', 'David', 'Kobe'}}
#{['Hubert', 'David', 'Kobe']}
set('kkbox')
print (set(['Hubert', 'David', 'Kobe']))
print (type(set(['Hubert', 'David', 'Kobe'])))

'''
Tuple example
'''
(1, 2, 3)
print (type((1, 2)))
student = ('David', 123)
name, student_id, = student
print (name, student_id)

'''
Dict example
'''
Warriors = {"Curry":"G","Green":"F","Durant":"F"}

students = {'David' : 1, 'Hubert' : 2, 'Kobe' : 3}
students['David']
students['Hubert'] = 5
del students['Hubert']
students.items()
students.keys()
students.values()
print (type(students))