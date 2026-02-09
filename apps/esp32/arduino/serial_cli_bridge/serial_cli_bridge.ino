const int LED_PIN = 2;
String cmd;

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  Serial.begin(115200);
  Serial.println("ESP32 CLI Bridge Ready. Type 'help'.");
}

void handleCommand(const String &c) {
  if (c == "help") {
    Serial.println("Commands: help, led on, led off, status");
  } else if (c == "led on") {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("OK: LED ON");
  } else if (c == "led off") {
    digitalWrite(LED_PIN, LOW);
    Serial.println("OK: LED OFF");
  } else if (c == "status") {
    Serial.print("LED=");
    Serial.println(digitalRead(LED_PIN) ? "ON" : "OFF");
  } else {
    Serial.println("ERR: unknown command");
  }
}

void loop() {
  while (Serial.available()) {
    char ch = (char)Serial.read();
    if (ch == '\n' || ch == '\r') {
      if (cmd.length() > 0) {
        cmd.trim();
        handleCommand(cmd);
        cmd = "";
      }
    } else {
      cmd += ch;
    }
  }
}
