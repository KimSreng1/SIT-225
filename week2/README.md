# Week 2 – SIT225: Data Capture Technologies

This folder contains all source code and resources for **Week 2 activities**, focused on working with various sensors and plotting data using Python.

## 🔧 Arduino Projects

### 1. `dht22_sensor.ino`
Reads temperature and humidity data from a DHT22 sensor using digital pin D2. Outputs the values in both Celsius and Fahrenheit to the Serial Monitor.

### 2. `ultrasonic_distance.ino`
Uses the HC-SR04 ultrasonic sensor (Trig: D9, Echo: D10) to measure distance and print it to the Serial Monitor in centimeters.

### 3. `accelerometer.ino`
Reads real-time X, Y, and Z axis acceleration from the built-in LSM6DS3 sensor on the Arduino Nano 33 IoT board. Displays data via Serial Monitor.

## 📊 Python Notebook

### `week2_notebook.ipynb`
A Jupyter Notebook that demonstrates how to load data and visualize it using `matplotlib`. Includes example plots using randomly generated values.

## 📝 Notes

- All Arduino sketches are compatible with **Arduino Nano 33 IoT**.
- Ensure VUSB pads are shorted to supply 5V power to DHT22 and HC-SR04 sensors.
- Install required libraries:
  - For DHT22: `DHT sensor library by Adafruit`
  - For Accelerometer: `Arduino_LSM6DS3`
  - For Python notebook: `matplotlib`, `pandas` (if using real CSV)

---
