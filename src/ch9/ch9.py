'''
txt example
'''
with open('test.txt', 'w') as datafile:
    datafile.write('hello pycone\n')

with open('test.txt', 'a') as datafile:
    datafile.write('hello pycone')

with open('test.txt', 'r') as datafile:
    content = datafile.read()
    print (content)

with open('txt_example.txt', 'r') as datafile:
    content = datafile.readlines()
    print (content)

with open('txt_example.txt', 'r') as datafile:
    for line in datafile:
        print (line)

'''
csv example
'''
import csv
with open('TSMC.csv', 'r') as datafile:
    for row in csv.reader(datafile):
        print (row)

warriors_data = [['Curry', 'G'], ['Durant', 'F']]
lakers_data = [['Kobe', 'G'], ['Gasol', 'F']]
with open('player.csv', 'w', newline='') as datafile:
    player = csv.writer(datafile, delimiter=',')
    player.writerow(warriors_data)
    player.writerow(lakers_data)

with open('Warriors.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    player = csv.DictWriter(csvfile, fieldnames=fieldnames)
    player.writeheader()
    player.writerow({'first_name': 'Stephen', 'last_name': 'Curry'})
    player.writerow({'first_name': 'Kevin', 'last_name': 'Durant'})
    player.writerow({'first_name': 'Klay', 'last_name': 'Thompson'})

'''
json example
'''
import json

with open('lakers_player.json', encoding='utf8') as datafile:
    player = json.load(datafile)
    print (player)

with open('warriors_player.json', "w", encoding='utf8') as datefile:
    player = {}
    player["name"] = "curry"
    player["age"] = 28
    player["championship"] = [2014]
    json.dump(player, datefile, indent=4, ensure_ascii=False)

