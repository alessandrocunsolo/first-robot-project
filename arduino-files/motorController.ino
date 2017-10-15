// Wire Slave Receiver
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Receives data as an I2C/TWI slave device
// Refer to the "Wire Master Writer" example for use with this

// Created 29 March 2006

// This example code is in the public domain.


#include <Wire.h>
#include <AFMotor.h>

AF_DCMotor motorL(3);
AF_DCMotor motorR(1);

void setup() {
  Wire.begin(8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  Serial.begin(9600);           // start serial for output
  
}

void loop() {
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  int buf[2];
  int i = 0;
  while (0 < Wire.available()) { // loop through all but the last
    //char c = Wire.read(); // receive byte as a character
    buf[i++] = Wire.read();
    //Serial.print(c);         // print the character
  }
  runMotors((char)buf[0],buf[1]);
}
void runMotors(char direction,int velocity)
{
  motorL.setSpeed(velocity);
  motorR.setSpeed(velocity);
  switch(direction)
  {
    case 'F': motorL.run(FORWARD);
              motorR.run(FORWARD);
              break;
    case 'L': motorL.run(BACKWARD);
              motorR.run(FORWARD);
              break;
    case 'R': motorL.run(FORWARD);
              motorR.run(BACKWARD);
              break;
    case 'B': motorL.run(BACKWARD);
              motorR.run(BACKWARD);
              break;
    case 'S': motorL.run(RELEASE);
              motorR.run(RELEASE);
              
    default:  break;
  }
}














