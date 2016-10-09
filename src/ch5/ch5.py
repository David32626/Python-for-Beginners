'''
If example
'''
if 2 > 1:
    print ('hello pycone')

number = 5
if number == 5:
    print ('')
else:
    print ('')

number = 10
if number > 5:
    if number % 2:
        print ('number > 5 and number is odd')
    else:
        print ('score > 5 and number is even')

score = 90
if score >= 90:
    print ('A')
elif 90 > score >= 80:
    print ('B')
elif 80 > score >= 70:
    print ('C')
else:
    print ('D')

'''
For example
'''
for i in range(5):
    print (i)

players = ["Curry", "Green", "Durant"]
for player in players:
    print (player)

for i, player in enumerate(players):
    print (i, player)

'''
While example
'''
number = 0
while number < 5:
    number = number + 1
    print (number)

'''
Pass example
'''
if number % 2:
    print ('number is even')
else:
    pass

'''
Break example
'''
for i in range(10):
    if i == 5:
        break
    print (i)

'''
Continue example
'''
for i in range(10):
    if i == 5:
        continue
    print (i)


