// Minimal placeholder logger for onboard telemetry.

void setup() {
  Serial.begin(115200);
  Serial.println("ESP32 Sensor Logger Ready");
}

void loop() {
  int hall = hallRead();
  Serial.print("hall=");
  Serial.println(hall);
  delay(2000);
}
