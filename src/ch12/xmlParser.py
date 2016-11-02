# python standard module
import xml.etree.ElementTree as ET

import sys
import os
import json

class WeatherXMLParser():
    def __init__(self, input_file):
        self.input_file = input_file
        self.targetList = ["TAIPEI,臺北","CHIAYI,嘉義","KAOHSIUNG,高雄"]

    def read_data(self):
        print("read data")
        tree = ET.parse(self.input_file)
        self.root = tree.getroot()

    def parse_data(self):
        # Parse data information
        data = {}
        dataset = self.root[7]
        for location in dataset:
            location_name = location[0]
            if location_name.text in self.targetList:
                print("location = ",location_name.text)
                data[location_name.text] = []
                for child in location[2]:
                    if child.tag == "{urn:cwb:gov:tw:cwbcommon:0.1}time":
                        tempDict = {}
                        tempDict["time"] = child[0].text
                        tempDict["rainfall"] = child[6][1][0].text
                        tempDict["temperature"] = child[2][1][0].text
                        data[location_name.text].append(tempDict)

        with open("weather_data.json", "w", encoding='utf8') as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii=False)

        return []

def main():
    input_file = sys.argv[1]
    parser = WeatherXMLParser(input_file)
    parser.read_data()
    parser.parse_data()
    

if __name__ == '__main__':
    main()