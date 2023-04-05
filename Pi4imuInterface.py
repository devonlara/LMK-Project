#This script will continuously output the GPS coordinates (latitude and longitude) received from the BerryGPS-IMU. You can use these coordinates to control your rover.


import time
import serial

# set up the serial connection to the BerryGPS-IMU device
ser = serial.Serial('/dev/ttyUSB0', 9600)

# loop indefinitely
while True:
    # read a line of data from the BerryGPS-IMU device
    data = ser.readline().decode('utf-8').strip()

    # if the line of data starts with "$GPIMU", parse it
    if data.startswith('$GPIMU'):
        imu_data = data.split(',')

        # print out the parsed data
        print('Accelerometer (m/s^2):', imu_data[1], imu_data[2], imu_data[3])
        print('Gyroscope (deg/s):', imu_data[4], imu_data[5], imu_data[6])
        print('Magnetometer (uT):', imu_data[7], imu_data[8], imu_data[9])

    # wait a little bit before reading the next line of data
    time.sleep(0.1)
