#include <Servo.h>
char serialData;
Servo myservo;  

int pos = 0;    

void setup() {
  myservo.attach(11);  
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  if(Serial.available() >0){
    serialData = Serial.read();
  if(serialData == '1'){ 
  digitalWrite(LED_BUILTIN, HIGH);   
  for (pos = 0; pos <= 180; pos += 1) { 
    // in steps of 1 degree
    myservo.write(pos);              
    delay(15);                      
  }
  delay(2000);
  for (pos = 180; pos >= 0; pos -= 1) { 
    myservo.write(pos);              
    delay(15);   
  }
  }
  else{
    digitalWrite(LED_BUILTIN, LOW);    W
 // delay(1000);
  }
}
}
