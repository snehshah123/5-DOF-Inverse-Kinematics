#define ENCA 2
#define ENCB 3

#define PWM 9
#define IN1  10

int pos = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ENCA,INPUT);
  pinMode(ENCB,INPUT);
  pinMode(PWM,OUTPUT);
  attachInterrupt(digitalPinToInterrupt(ENCA),readEncoder,RISING);
}

void loop() {
  int t=1;
  while (t==1){

  
  setMotor(0, 200, PWM, IN1);

  break;
  Serial.println(pos);
  setMotor(-1, 200, PWM, IN1);
  delay(200);
  Serial.println(pos);

  }
}

void setMotor(int dir, int pwmVal, int pwm, int in1){
  analogWrite(pwm,pwmVal);
  int t=1;
  while (t==1)
  {
  if(dir == 1){
    digitalWrite(in1,HIGH);
    delay(1000);
    break;
  }
  else if(dir == -1){
    digitalWrite(in1,LOW);
    delay(1000);
  }
  }
}

void readEncoder(){
  int b = digitalRead(ENCA);
  if(b > 0){
    pos++;
  }
  else{
    pos--;
  }
}