#include <OneWire.h>
#include <DallasTemperature.h>
#include <Stepper.h>

#define Rx 7

OneWire oneWire(Rx);
DallasTemperature sensor(&oneWire);


float Temp=0;

const int stepsxRev = 32;  // 360/11.25  change this to fit the number of steps per revolution for your motor
const int gearReduction = 64;
const int stepsPerOutRev = stepsxRev * gearReduction;

Stepper CIStepper(stepsPerOutRev, 8, 10, 9, 11); // Pin 1, 2, 3, 4

int aux = 0;
int stopm = 0;

void setup() {

  Serial.begin(9600);
  sensor.begin();
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  CIStepper.setSpeed(5);

}

void loop() {

  sensor.requestTemperatures();
  Temp=sensor.getTempCByIndex(0);
  Serial.print(Temp);
  Serial.print(" C  ");
  Serial.print("\n");

  if (Temp > 28) {
    aux = 1;
    digitalWrite(5, HIGH);
    digitalWrite(6, LOW);  
  } if (Temp < 27) {
    aux = 0;
    digitalWrite(5, LOW);
    digitalWrite(6, HIGH);
  }

  if (aux == 1 and stopm == 0) {
    CIStepper.step(500);
    stopm = 1;
    delay(4);
  } else if (aux == 0 and stopm == 1) {
    CIStepper.step(-400);
    stopm = 0;
    delay(4);
  }

}
