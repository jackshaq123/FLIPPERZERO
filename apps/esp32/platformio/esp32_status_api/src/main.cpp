#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  Serial.println("ESP32 Status API (serial placeholder)");
}

void loop() {
  digitalWrite(2, !digitalRead(2));
  Serial.println("heartbeat");
  delay(1000);
}
