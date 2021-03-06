import serial
import time
import requests
import json
firebase_url = 'https://garbage-sensor-data.firebaseio.com/'
#Connect to Serial Port for communication
print 'initializing script....'
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
#Setup a loop to send distance values at fixed intervals
#in seconds
time.sleep(2)
fixed_interval = 1
while 1:
  try:          
    distance_c = ser.readline()
    
    #current location name
    dustbin_location = 'Vidhyanagar';
    print distance_c +'\n'+ dustbin_location
    
    #insert record
    data = {'name':"sensor_data",'value':distance_c}
    result = requests.patch(firebase_url + '/' + dustbin_location + '/distance.json', data=json.dumps(data))
    
    print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
    time.sleep(fixed_interval)
  except IOError:
    print('Error! Something went wrong.')
time.sleep(fixed_interval)
