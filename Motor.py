#include <ESP8266WiFi.h>

// Motor control pins
const int motorPin1 = D1; // Motor driver input pin 1
const int motorPin2 = D2; // Motor driver input pin 2
const int speedPin = D3;  // Motor speed control (PWM)

void setup() {
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(speedPin, OUTPUT);

  // Initial state: motor stopped
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  analogWrite(speedPin, 0);
}

void loop() {
  // Forward direction
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  analogWrite(speedPin, 1023); // Maximum speed (PWM value)
  delay(2000); // Run for 2 seconds
  
  // Stop
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  analogWrite(speedPin, 0); // Stop the motor
  delay(1000); // Wait for 1 second
  
  // Reverse direction
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  analogWrite(speedPin, 512); // Half speed
  delay(2000); // Run for 2 seconds
  
  // Repeat...
}
