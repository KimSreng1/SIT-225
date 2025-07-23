#include "DHT.h"

#define DHTPIN 2      // Using D2 for data pin
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  delay(2000); // Let sensor settle
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float tempC = dht.readTemperature();       // Celsius
  float tempF = dht.readTemperature(true);   // Fahrenheit

  if (isnan(humidity) || isnan(tempC) || isnan(tempF)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print(" % | Temperature: ");
  Serial.print(tempC);
  Serial.print(" °C / ");
  Serial.print(tempF);
  Serial.println(" °F");

  delay(2000); // Match sensor's 0.5Hz sampling rate
}
