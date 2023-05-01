#Q1 

void fadeLED(int LED_Pin) {
  // set LED_Pin as an output
  pinMode(LED_Pin, OUTPUT);

  // increase brightness of LED
  for (int brightness = 0; brightness <= 255; brightness++) {
    analogWrite(LED_Pin, brightness);
    delay(10);
  }

  // fade out LED
  for (int brightness = 255; brightness >= 0; brightness--) {
    analogWrite(LED_Pin, brightness);
    delay(10);
  }
}


#Q2

void blinkLEDs(int LED1_Pin, int LED2_Pin, int delay_time) {
  pinMode(LED1_Pin, OUTPUT); // set LED1_Pin as an output
  pinMode(LED2_Pin, OUTPUT); // set LED2_Pin as an output

  while (true) { // keep looping indefinitely
    digitalWrite(LED1_Pin, HIGH); // turn on LED1
    digitalWrite(LED2_Pin, LOW); // turn off LED2
    delay(delay_time); // wait for delay_time ms
    digitalWrite(LED1_Pin, LOW); // turn off LED1
    digitalWrite(LED2_Pin, HIGH); // turn on LED2
    delay(delay_time); // wait for delay_time ms
  }
}
