#define SERVO_PIN1 2
#define SERVO_PIN2 3
#include <Servo.h>
Servo servo1;
Servo servo2;
int count=0;

void setup() {
  // serial通信のsetup
  Serial.begin(115200);
  while (!Serial) {
    ;
  }
  // servoのsetup
  servo1.attach(SERVO_PIN1);
  servo1.write(0);
  servo2.attach(SERVO_PIN2);
  servo2.write(180);
}

void loop() {
  Serial.println("serial");
  delay(100);
  if (Serial.available() > 0) {
    Serial.println("received");
    String str = Serial.readStringUntil("\n"); // \nまで読む
    str.trim(); // \nまで読んで、\nまでを消す
    //Serial.println(str);
    if (str == "RUBU") { //red up blue up
      //count = 1;
      servo1.write(180);
      servo2.write(0);
    } else if (str == "RUBD") { //red up blue down 
      //count = 2;
      servo1.write(180);
      servo2.write(180);
    } else if (str == "RDBU") { //red down blue up
      //count = 3;
      servo1.write(0);
      servo2.write(0);
    } else if (str == "RDBD") { //red down blud down
      //count = 4;
      servo1.write(0);
      servo2.write(180);
    }
  }
  /*
  switch (count){
    case 1:
      servo1.write(180);
      servo2.write(0);
      break;
    case 2:
      servo1.write(180);
      servo2.write(180);
      break;
    case 3:
      servo1.write(0);
      servo2.write(0);
      break;
    case 4:
      servo1.write(0);
      servo2.write(180);
      break;
    default:
      break;
  }
  */
  //Serial.println(count);
  //delay(100); // 今回はいらない
}
