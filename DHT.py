import Adafruit_DHT
import csv
from datetime import datetime
import time

sensor = Adafruit_DHT.DHT11

pin = 4

fieldnames = ['time_of_day', 'temperature', 'humidity']
filename = ''
newHour = False
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
    now = datetime.now()

    time_of_day = now.strftime("%H:%M:%S")
    if now.strftime("data/%Y:%m:%d:%H.csv") != filename:
        filename = now.strftime("data/%Y:%m:%d:%H.csv")
        newHour = True


    if newHour is True:
        try:
            csvfile.close()
        except:
            print('Starting to read DHT11')

        csvfile = open(filename, 'a+', newline='')
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        newHour = False
    print(filename)
    print(time_of_day)


    if humidity is not None and temperature is not None:
        writer.writerow({'time_of_day': time_of_day, 'temperature': temperature, 'humidity': humidity,})
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    
    time.sleep(1)