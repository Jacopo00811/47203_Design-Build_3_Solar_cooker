#include <Stepper.h>

const int stepsxRev = 32;  // 360/11.25 
// change this to fit the number of steps per revolution for your motor

const int gearReduction = 64;
const int stepsPerOutRev = stepsxRev * gearReduction;

int stepsRequired;
int rotdir;

// initialize the stepper library on pins 8 through 11:
Stepper DB3_Stepper(stepsPerOutRev, 8, 10, 9, 11);
// 1-> pin 8, 2-> pin 9, 3-> pin 10, 4-> pin 11 on Arduino

void setup() { 

  pinMode(2, INPUT_PULLUP);

}

void loop() {

  rotdir = digitalRead(2);

  if (rotdir == HIGH) {
  // step one revolution in one direction:
  DB3_Stepper.setSpeed(5);
  stepsRequired = 2*stepsPerOutRev;
  DB3_Stepper.step(stepsRequired);
  delay(2000);
  } else {
  // step one revolution in the other direction:
  DB3_Stepper.setSpeed(6);
  stepsRequired = -3*stepsPerOutRev;
  DB3_Stepper.step(stepsRequired);
  delay(1000);
  }
}
