/*
This is an example how to use Touch Intrrerupts and read touch values
*/

int threshold = 40;
int buttonState = 0;
int prevState = 1;
int buttonCount = 0;

void setup() {
  Serial.begin(115200);
  pinMode(2, INPUT_PULLUP);
  delay(1000); // give me time to bring up serial monitor

}

void loop(){
  int buttonState = digitalRead(2);
  if (buttonState != prevState) 
  {
      buttonCount++;
      Serial.println(buttonCount);
    }
    delay(50);
    prevState = buttonState;
  }
