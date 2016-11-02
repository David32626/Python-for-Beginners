# python standard module
import sys
import json
from datetime import datetime, timedelta

# numpy module
import numpy as np

# matplotlib module
import matplotlib.pyplot as plt

class WeatherAnalyzer():
    def __init__(self):
        self.data = {}
        self.location_rainfall_list = {}

    def load_json(self,input_file):
        jsonFile = open(input_file, encoding='utf8')
        self.data = json.load(jsonFile)
        jsonFile.close()

    def analyze_data(self):
        for location in self.data:
            print(location)
            self.location_rainfall_list[location] = []
            monthly_rainfall = 0.0
            current_month = 9
            for hour in self.data[location]:
                dt = self.parse_time(hour["time"])
                if dt.month == current_month:
                    if hour["rainfall"] == "T": # rainfall less than 0.1mm
                        continue
                    monthly_rainfall += float(hour["rainfall"])
                else:
                    self.location_rainfall_list[location].append(monthly_rainfall)
                    current_month += 1
                    if current_month > 12:
                        current_month -= 12
                    monthly_rainfall = 0
                    if hour["rainfall"] == "T":
                        continue
                    monthly_rainfall += float(hour["rainfall"])
            print(self.location_rainfall_list[location])

    def parse_time(self, time):
        time_format = '%Y-%m-%d %H:%M'
        try:
            dt = datetime.strptime(time, time_format)
            return dt
        except ValueError as e:
            time = time.replace('24:', '23:')
            dt = datetime.strptime(time, time_format)
            dt += timedelta(hours=1)
            return dt

    def plot_rainfall(self):
        n_groups = 12

        # index = [ 0  1  2  3  4  5  6  7  8  9 10 11]
        index = np.arange(n_groups)

        bar_width = 0.35

        opacity = 0.4

        plt.title("Rainfall per month")
        plt.xlabel("Month")
        plt.ylabel("Rainfall per month(mm)")
        plt.xticks(index,("201509","10","11","12","201601","02","03","04","05","06","07","08"))
        taipei_rect = plt.bar(left=index,height=tuple(self.location_rainfall_list["Taipei"]),width=bar_width\
                            ,align="center",color="b",label="Taipei",alpha=opacity)
        kaohsiung_rect = plt.bar(left=index+bar_width,height=tuple(self.location_rainfall_list["Kaohsiung"]),width=bar_width\
                            ,align="center",color="r",label="Kaohsiung",alpha=opacity)
        plt.legend()

        plt.show()


def main():
    try:
        input_file = sys.argv[1]
    except IndexError as e:
        print("[Usage] python WeatherAnalyzer.py input\\weather_data.json")
        return
    analyzer = WeatherAnalyzer()
    analyzer.load_json(input_file)
    analyzer.analyze_data()
    analyzer.plot_rainfall()

if __name__ == '__main__':
    main()