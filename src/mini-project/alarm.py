import time
from datetime import datetime
import webbrowser

total_breaks = 1
break_count = 0
print ("This program started on " + str(datetime.now()))
while(break_count < total_breaks):
    time.sleep(2)
    webbrowser.open('https://www.youtube.com/watch?v=u57d4_b_YgI')
    break_count += 1