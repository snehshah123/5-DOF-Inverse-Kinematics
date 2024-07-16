#include <VarSpeedServo.h>
#include "StringSplitter.h"
#include <EEPROM.h>

//MOTOR,0,0,0,0,0
//MOTOR,90,0,80,0,90
//MOTOR,81,220,48,24,86
//MOTOR,66,649,43,67,90

// Servo objects
VarSpeedServo S1;
VarSpeedServo S3;
VarSpeedServo S4;
VarSpeedServo S5;

// Pin assignments
const int ir = 13;
const int relay = 4;
const int a = 3;
const int b = 2;
const int pwm = 11;
const int dir = 12;
const int m1 = 5;
const int m3 = 10;
const int m4 = 6;
const int m5 = 9;

// Global variables
int e;
volatile int pos = 0;
int lastpos;
float target[5] = {};

// Enum for system state
enum State {
  IDLE,
  MOVING
};
State currentState = State::IDLE;

// Interrupt handler for encoder
void encoder() {
  pos += digitalRead(b) > 0 ? 1 : -1;
}

// Initialize the system
void setup() {
  Serial.begin(115200);

  // Pin modes
  pinMode(a, INPUT);
  pinMode(b, INPUT);
  pinMode(dir, OUTPUT);
  pinMode(relay, OUTPUT);
  pinMode(ir, INPUT);
  // Servo settings
  S1.attach(m1);
  S3.attach(m3);
  S4.attach(m4);
  S5.attach(m5);
  S1.write(0, 20);
  S4.write(0, 20);
  S3.write(0, 20);
  S5.write(0, 20);

  // Encoder interrupt
  attachInterrupt(digitalPinToInterrupt(a), encoder, RISING);
}

// Main loop
void loop() {
  if (currentState == State::IDLE) {
    waitForInput();
  }

  if (currentState == State::MOVING) {
    moveMotors();
  }
}

// Wait for the user to input the target positions for the motors
void waitForInput() {
  Serial.println("Enter Values (MOTOR,90,0,80,0,90) : ");
  if (Serial.available() > 0) {
    
    String input_string = Serial.readStringUntil('\n');

    if (input_string.startsWith("MOTOR,")) {
      StringSplitter splitter(input_string.substring(6), ',', 5);
      int itemCount = splitter.getItemCount();

      if (itemCount == 5) {
        for (int i = 0; i < itemCount; i++) {
          float item = splitter.getItemAtIndex(i).toFloat();
          target[i] = item;
        }

        Serial.println("Moving to the target positions...");


        // Debugging the values of target
        for (int i = 0; i < 5; i++) {
          Serial.print("target[");
          Serial.print(i);
          Serial.print("] = ");
          Serial.println(target[i]);
        }

        currentState = State::MOVING;
      } else {
        Serial.println("Invalid number of target positions.");
      }
    }
  }
}

// Move the motors to the target positions
void moveMotors() {

  // Motor 3
  S3.write(target[2], 10, true);


  // Motor 4
  S4.write(target[3], 10, true);

  // Motor 5
  S5.write(target[4], 10, true);

  // Motor 1
  S1.write(target[0], 10, true);

  // Motor 2
  int e = target[1] - pos;
  if (e >= 135) {
    digitalWrite(dir, HIGH);
    analogWrite(pwm, 75);
  } else if (e < 0) {
    digitalWrite(dir, LOW);
    analogWrite(pwm, 75);
  } else {
    analogWrite(pwm, 0);

    // Check if the target positions are reached
    if (target[0] == 66 && target[1] == 649 && target[2] == 43 && target[3] == 67 && target[4] == 90) {
      // Target positions are MOTOR,90,0,80,0,90, set relay to LOW
      digitalWrite(relay, HIGH);
    } else {
      // Target positions are not MOTOR,90,0,80,0,90, set relay to HIGH
      digitalWrite(relay, LOW);
    }

    //Serial.println("Reached target positions.");
    lastpos = pos;

    EEPROM.update(25, lastpos / 32.1254902);
    currentState = State::IDLE;


    Serial.println("DONE");
  }
}