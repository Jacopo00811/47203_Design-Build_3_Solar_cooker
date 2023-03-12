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

int target = 27; // Target temperature
int aux = 0; // Open
int closingTime = 0; // Needs to be initialized to 0
int closeStep = -400; 
int openStep = 400;
int period = 50; // Is 10000 ms but it is 100 otherwise it goes in overflow

void setup() {

  Serial.begin(9600);
  sensor.begin();
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  CIStepper.setSpeed(15);

}

void loop() {

  sensor.requestTemperatures();
  Temp=sensor.getTempCByIndex(0);
  Serial.print(Temp);
  Serial.print(" C\n");

  if ((Temp < target-3) && (Temp >= target-5)) { // 20%
    closingTime = period*20;
    Serial.print("Setting to 20% \n");
    Serial. println();
  
  } else if ((Temp < target-2) && (Temp >= target-3)) { // 30% // Nope
    closingTime = period*30;
    Serial.print("Setting to 30% \n");
    Serial. println();

  } else if ((Temp < target-1) && (Temp >= target-2)) { // 40%
    closingTime = period*40;
    Serial.print("Setting to 40% \n");
    Serial. println();

  } else if (abs(Temp-target) <= 1) {  // 50%
    closingTime = period*50;
    Serial.print("Setting to 50% \n");
    Serial. println();

  } else if (Temp > target+4) { // Full period
    closingTime = period;
    Serial.print("Setting to 100% \n");
    Serial. println();
    
  } else if ((Temp >= target+3) && (Temp <= target+4)) { // 80%
    closingTime = period*80;
    Serial.print("Setting to 80% \n");
    Serial. println();

  } else if ((Temp >= target+2) && (Temp < target+3)) { // 70% // Nope
    closingTime = period*70;
    Serial.print("Setting to 70% \n"); 
    Serial. println();   
    
  } else if ((Temp > target+1) && (Temp < target+2)) { // 60%
    closingTime = period*60;
    Serial.print("Setting to 60% \n"); 
    Serial. println();   
  
  } else { // 0%
    closingTime = 0;
    Serial.print("Too cold \n");
    Serial. println();
  }

  
  if ((closingTime == period*100) && (aux == 0)) {
    digitalWrite(5, LOW); // Close
    digitalWrite(6, HIGH);    
    CIStepper.step(closeStep);
    aux = 1;
    
  } else if ((closingTime == period*100) && (aux == 1)) {
    // Nothing
    
  } else if ((closingTime != 0) && (closingTime != period*100) && (aux == 0)) {            
    digitalWrite(5, LOW); // Close
    digitalWrite(6, HIGH);    
    CIStepper.step(closeStep);
    aux = 1;
    delay(closingTime);
    
    digitalWrite(5, HIGH); // Open
    digitalWrite(6, LOW);
    CIStepper.step(openStep);
    aux = 0;
    delay((period*100)-closingTime); 

  } else if ((closingTime != 0) && (closingTime != period*100) && (aux == 1)) {                
    delay(closingTime);
    
    digitalWrite(5, HIGH); // Open
    digitalWrite(6, LOW);
    CIStepper.step(openStep);
    aux = 0;
    delay((period*100)-closingTime);            
  
  } else if ((closingTime == 0) && (aux == 1)) {
    digitalWrite(5, HIGH); // Open
    digitalWrite(6, LOW);
    CIStepper.step(openStep);
    aux = 0;
  }
}