const int ledPin = 6; 

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  randomSeed(analogRead(A0)); 
}

void loop() {
  if (Serial.available()) {
    int blinkCount = Serial.parseInt(); 
    for (int i = 0; i < blinkCount; i++) {
      digitalWrite(ledPin, HIGH);
      delay(500);
      digitalWrite(ledPin, LOW);
      delay(500);
    }

    int delayTime = random(1, 6); 
    Serial.println(delayTime);
  }
}
