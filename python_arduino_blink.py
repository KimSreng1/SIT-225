import serial
import time
import random

arduino = serial.Serial('COM3', 9600)  # 
time.sleep(2)  # Wait for Arduino to reset

while True:
    num = random.randint(1, 5)
    print(f"[{time.strftime('%H:%M:%S')}] Sending: {num}")
    arduino.write(f"{num}\n".encode())

    while not arduino.in_waiting:
        pass

    reply = arduino.readline().decode().strip()
    print(f"[{time.strftime('%H:%M:%S')}] Received delay time: {reply} seconds")
    time.sleep(int(reply))
    print(f"[{time.strftime('%H:%M:%S')}] Waited {reply} seconds\n")
