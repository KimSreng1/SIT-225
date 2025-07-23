#include <Arduino_LSM6DS3.h>

void setup() {
  Serial.begin(9600);
  while (!Serial); // Wait for serial
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  Serial.println("IMU initialized!");
}

void loop() {
  float x, y, z;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
    Serial.print("X: ");
    Serial.print(x);
    Serial.print(" g | Y: ");
    Serial.print(y);
    Serial.print(" g | Z: ");
    Serial.println(z);
  }

  delay(100); // 10Hz sampling
}
