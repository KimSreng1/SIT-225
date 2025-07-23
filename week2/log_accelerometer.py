import serial
import time
from datetime import datetime

COM_PORT = 'COM3'
BAUD_RATE = 9600
FILENAME = "accel_data.csv"

try:
    # Open Serial port
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to {COM_PORT}")
    time.sleep(2)

    with open(FILENAME, "a") as file:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                row = f"{timestamp},{line}"
                print(row)
                file.write(row + "\n")

except KeyboardInterrupt:
    print("\nStopped by user.")
    ser.close()
except Exception as e:
    print("Error:", e)
