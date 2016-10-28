# import standard module
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

# numpy module
import numpy as np

# matplotlib module
import matplotlib.pyplot as plt

# weather data
data_path = 'data/C-B0024-001.xml'

class WeatherAnalyzer():
    def __init__(self, data_path, location):
        self.data_path = data_path
        self.location = location

    def read_data(self):
        tree = ET.parse(self.data_path)
        root = tree.getroot()
        return root

    def parse_data(self, root):
        # Parse data information
        for item in root.iter('cwbopendata'):
            self.identifier = item[0].text
            self.sender = item[1].text
            self.sent = item[2].text
            self. status = item[3].text
            self.status = item[4].text
            self.dataid = item[5].text
            self.scope = item[6].text

        # Parse locationName, stationId, obsTime, temperature, humidity, rainfall
        daily_data = []
        for location in root.iter('location'):       
            if location[0].text == self.location:
                for time in location.iter('time'):
                    hours_data = {}
                    hours_data['locationName'] = location[0].text
                    hours_data['stationId'] = location[1].text

                    hours_data['obsTime'] = self.parse_time(time[0].text)

                    try:
                        hours_data['temperature'] = float(time[2][1][0].text)
                    except ValueError as e:
                        hours_data['temperature'] = 0

                    #print (time[3][0].text)
                    try:
                        hours_data['humidity'] = float(time[3][1][0].text)
                    except ValueError as e:
                        hours_data['humidity'] = 0

                    #print (time[6][0].text)
                    try:
                        hours_data['rainfall'] = float(time[6][1][0].text)
                    except ValueError as e:
                        hours_data['rainfall'] = 0
                
                    daily_data.append(hours_data)

        return daily_data

    def parse_time(self, time):
        time_format = '%Y/%m/%d %H:%M'
        try:
            dt = datetime.strptime(time, time_format)
            return dt
        except ValueError as e:
            time = time.replace('24:', '23:')
            dt = datetime.strptime(time, time_format)
            dt += timedelta(hours=1)
            return dt

    def mean_temperature(self, daily_data, month):
        temperature = []
        for data in daily_data:
            date = data['obsTime'].timetuple()
            # date[0] -> year, date[1] -> month, date[2] -> day, date[3] -> hour
            if date[1] == month:
                temperature.append(data['temperature'])
        total = 0
        noise_num = 0
        for temp in temperature:
            if temp == 0:
                noise_num += 1
            else:
                total += temp
        #print (len(temperature))
        #print (temperature)
        mean_temperature = round(total / (len(temperature) - noise_num), 2)
        print ('Mean temperature: {}'.format(mean_temperature))
        return (month, mean_temperature)

    def plot_temperature(self, data):
        
        month = [x for x in range(1, 13)]
        n_groups = len(month)

        means_temperatures = [0, 0, 0, 0, 0, 0, 0, 0, 26.64, 26.39, 0, 0]

        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.1

        rects1 = plt.bar(index, means_temperatures, bar_width, color='b', label='Men')

        plt.xlabel('Temperature')
        plt.ylabel('Month')
        plt.title('Weather')
        plt.xticks(index + bar_width, month)
        plt.legend()

        plt.show()


def main():
    wa = WeatherAnalyzer(data_path, 'Tamsui,淡水')
    root = wa.read_data()
    daily_data = wa.parse_data(root)
    month_temperature = [x for 0 in range(0, 12)]
    wa.mean_temperature(daily_data, 9)
    wa.mean_temperature(daily_data, 10)

    wa.plot_temperature([26.64, 26.39])

if __name__ == '__main__':
    main()