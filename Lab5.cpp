#include <Servo.h>
Servo tilt, pan;
int joyX = A0;
int joyY = A1;
int x, y;
voide setup()
{
  tilt.attach(9);
  pan.attach(10);
}
voide loop()
{
  x = map(analogRead(joyX) , 0, 1023, 0, 180);
  y = map(analogRead(joyY), 0, 1023, 0, 180);
  tilt.write(x);
  pan.write(y);
  delay(15);
}

