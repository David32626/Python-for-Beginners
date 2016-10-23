'''
txt example
'''
with open('test.txt', 'w') as file:
    file.write('Hello')
    file.write('Pycone')

with open('test.txt', 'w') as file:
    file.write('Hello \n')
    file.write('Pycone\n')

with open('test.txt', 'w') as file:
    file.writelines(['Hello','Pycone'])

with open('test.txt', 'r') as file:
    content = file.read()
    print (content)

with open('txt_example.txt', 'r') as file:
    content = file.readlines()
    print (content)

with open('txt_example.txt', 'r') as file:
    for line in file:
        print (line)

'''
json example
'''
import json

with open('player.json') as file:
    player = json.load(file)
    print (player) 
    print (type(player))
    print ("Player's name = ",player["name"])

with open('warriors_player.json', "w") as file:
    player = {}
    player["name"] = "Curry"
    player["age"] = 28
    player["championship"] = [2014]
    json.dump(player, file, indent=4)

'''
XML example
'''
import xml.etree.ElementTree as ET
tree = ET.ElementTree(file='student.xml')
print(type(tree))

root = tree.getroot()
print(type(root))
print(root.tag,root.attrib)

for child in root:
    print(child.tag,child.attrib)

print(root[0][1].text)


'''
csv example
'''
import csv
with open('TSMC.csv', 'r') as datafile:
    for row in csv.reader(datafile):
        print (row)

# warriors_data = [['Curry', 'G'], ['Durant', 'F']]
# lakers_data = [['Kobe', 'G'], ['Gasol', 'F']]
# with open('player.csv', 'w', newline='') as datafile:
#     player = csv.writer(datafile, delimiter=',')
#     player.writerow(warriors_data)
#     player.writerow(lakers_data)

# with open('Warriors.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     player = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     player.writeheader()
#     player.writerow({'first_name': 'Stephen', 'last_name': 'Curry'})
#     player.writerow({'first_name': 'Kevin', 'last_name': 'Durant'})
#     player.writerow({'first_name': 'Klay', 'last_name': 'Thompson'})

import os

path = "C:\\Users\\user\\Desktop\\Python-for-Beginners\\src\\CH1"
for root, dirnames,filenames in os.walk(path):
    print("root = ",root)
    print("dirnames = ",dirnames)
    print("filenames = ",filenames)

    # for file in filenames:
    #     if file.endswith(".py"):
    #         print("This is a Python file: ",file)
    print()

