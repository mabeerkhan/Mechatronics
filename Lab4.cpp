"3MD_LED_Blink_Function"

const int analogPin = A0;
const int LedCount = 3;
int LedPins[] = (16, 5, 4);

void setup() {
for (int thisLed = 0; thisLead < Ledcount; thisLed++)  {
        pinMode (LedPins[thisLed], OUTPUT);
    }
}


void loop() {
     int sensorReading = analogread (A0);
     int LedLevel = map(sensorreading, 0, 1023, 0, LedCount);
     
     for (int thisLed = 0; thisLed < LedCount; thisLed++) {
         if (thsLed < LedLevel) {
           digitalWrite(LedPins[thisLed], HIGH);
         }else{
           digitalWrite(LedPins[thisLed], LOW);
         }
      }
 }
 
 
