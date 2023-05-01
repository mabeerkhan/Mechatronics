Lab #2

Q1
for(int i==0; i=<99;i++)
{
if(i%3) {serial.printIn("Mechanical");
}
elseif(i%5) {serial.printIn("Electronics");
}
elseif(i%3&&i%5) {serial.printIn("Mechatronics")
}
else {serial.print("-")
}
}


Q2
#define pin1 = int a;
#define pin2 = int b;
#define pin3 = int c;
#digitalRead(pin1);
#digitalRead(Pin2);
#digitalRead(Pin3);
void setup()
{
int result = (a*b)+c;
serial.printIn(result);
}
