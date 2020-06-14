#!/usr/bin/env python2
from sense_hat import SenseHat
from datetime import datetime
import subprocess
import pandas as pd

sense = SenseHat()
temp = sense.get_temperature()

temp_c = sense.get_temperature()
cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
array = cpu_temp.split("=")
array2 = array[1].split("'")

cpu_tempc = float(array2[0])
cpu_tempc = float("{0:.2f}".format(cpu_tempc))
temp_calibrated_c = temp_c - ((cpu_tempc - temp_c)/5.466)
temp_calibrated_c = float("{0:.2f}".format(temp_calibrated_c))

pressure = sense.get_pressure()
humidity = sense.get_humidity()

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")


temp_time = current_time + "," + str(temp_calibrated_c) + ',' + str(pressure) + ',' + str(humidity) + '\n'
with open('document.csv','a') as fd:
    fd.write(temp_time)
