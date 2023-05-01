LAB #1

Q1 
#include math.h library

int a[12]= {1,2,3,4,5,6,7,8,9,10,11,12}
serial.print a(7)

Q2
void setup()
{
if (t>25) {serial.print("fan on")};
elseif (t<10) {serial.print("fan off")};
serial.begin(9600);
delay(1000);
serial.printIn(a)
