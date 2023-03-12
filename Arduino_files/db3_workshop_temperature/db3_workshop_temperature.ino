#include <OneWire.h>
#include <DallasTemperature.h>

#define Rx 7

OneWire oneWire(Rx);

DallasTemperature sensor(&oneWire);

float Temp=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.print(" Starting... ");
  sensor.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  sensor.requestTemperatures();
  Temp=sensor.getTempCByIndex(0);
  Serial.print(Temp);
  Serial.print(" C  ");
  Serial.print('\n'); 
  delay(500);
}
