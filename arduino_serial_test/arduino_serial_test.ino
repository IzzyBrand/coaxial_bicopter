#include <Servo.h>

#define CW_MOTOR_PIN 5
#define CCW_MOTOR_PIN 6
#define ROLL_SERVO_PIN 7
#define PITCH_SERVO_PIN 8

int cmd[] = {1000, 1000, 1500, 1500};
int out[] = {1000, 1000, 1500, 1500};

Servo servos[4];

void setup() {
  Serial.begin(57600);
  Serial.setTimeout(10);
  attach_servos();
  write_servos();
}

void loop() {
  printCmd();
  delay(50);
  
}

void attach_servos() {
  servos[0].attach(CW_MOTOR_PIN);
  servos[1].attach(CCW_MOTOR_PIN);
  servos[2].attach(ROLL_SERVO_PIN);
  servos[3].attach(PITCH_SERVO_PIN);
}

void write_servos() {
  for (int i = 0; i < 4; i++) {
    servos[i].writeMicroseconds(out[i]);
  }
}

void printCmd() {
  Serial.print(cmd[0]);
  Serial.print(",\t");
  Serial.print(cmd[1]);
  Serial.print(",\t");
  Serial.print(cmd[2]);
  Serial.print(",\t");
  Serial.print(cmd[3]);
  Serial.println();
}

// parse the incoming integers into the command array
void serialEvent() {
  for (int i = 0; i < 4; i++) {
    cmd[i] = Serial.parseInt();
  }
}
