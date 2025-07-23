# Week 2 – SIT225: Data Capture Technologies

This folder contains all source code and resources for **Week 2 activities**, focused on working with various sensors and plotting data using Python.

## 🔧 Arduino Projects

### 1. `dht22_sensor.ino`
Reads temperature and humidity data from a DHT22 sensor using digital pin D2. Outputs the values in both Celsius and Fahrenheit to the Serial Monitor.

### 2. `ultrasonic_distance.ino`
Uses the HC-SR04 ultrasonic sensor (Trig: D9, Echo: D10) to measure distance and print it to the Serial Monitor in centimeters.

### 3. `accelerometer.ino`
Reads real-time X, Y, and Z axis acceleration from the built-in LSM6DS3 sensor on the Arduino Nano 33 IoT board. Displays data via Serial Monitor.

### 4. `lsm6ds3_logger.ino`
Collects real-time X, Y, and Z axis acceleration from the LSM6DS3 sensor on the Arduino Nano 33 IoT. Sends the data via Serial in CSV format for long-term logging with `log_accelerometer.py`. Used specifically for SIT225 Task 2.1P (30+ minute data capture and analysis).

## 🐍 Python Script: `log_accelerometer.py`

This Python script connects to the Arduino Nano 33 IoT via Serial (COM port), reads X, Y, Z acceleration data from the LSM6DS3 sensor, adds a timestamp in the format `YYYYMMDDHHMMSS`, and logs it to a CSV file.

### How it works:
- Listens to data like: `0.0123,-0.0456,1.0001`
- Adds current time: `20250723120030`
- Saves to file as:  
  `20250723120030,0.0123,-0.0456,1.0001`

### How to run it:
1. Upload the Arduino sketch (`lsm6ds3_logger.ino`) to the board.
2. Close the Serial Monitor.
3. Run the script:
   ```bash
   python log_accelerometer.py
📊 Python Notebook
week2_notebook.ipynb
A Jupyter Notebook that demonstrates how to load data and visualize it using matplotlib. Includes example plots using randomly generated values.

accel_data.py / accel_data.ipynb
This script was used to analyze and visualize long-term acceleration data for Task 2.1P.

Features:

Loads real-time accelerometer data from accel_data.csv

Displays first 5 rows and basic statistics (mean, std, etc.)

Plots acceleration over time for X, Y, and Z axes

Example output:

When stationary, the Z-axis remains mostly stable

X and Y axes show clear spikes when the board is moved

📸 Task 2.1P Analysis Summary
Prediction (before graphing):
I believe the Z-axis will remain relatively stable while the board is stationary, while X and Y may show small fluctuations. When the board is moved or rotated, X, Y, and Z will show distinct spikes. I expect clear visual differences between stationary and movement periods in the graph.

Observation (after plotting):
The resulting plot confirmed the prediction. The Z-axis stayed relatively constant during periods of no movement, while X and Y showed spikes when the board was tilted or shaken. The visual change clearly indicated periods of motion.

Proof:
Screenshot of the plotted graph was captured and included as evidence

Graph includes labels, legend, and timestamp values

CSV file and plotting script are included in this repo

📝 Notes
All Arduino sketches are compatible with Arduino Nano 33 IoT.

Ensure VUSB pads are shorted to supply 5V power to DHT22 and HC-SR04 sensors.

Install required libraries:

For DHT22: DHT sensor library by Adafruit

For Accelerometer: Arduino_LSM6DS3

For Python notebook: matplotlib, pandas (if using real CSV)


