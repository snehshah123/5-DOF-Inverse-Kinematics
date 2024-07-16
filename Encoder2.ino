int a=2;
int b=3;
int pwm=9;
int dir=10;
int pos=0;
int target=1200;
void setup() {
Serial.begin(9600);
pinMode(dir,OUTPUT);
pinMode(a,INPUT);
pinMode(b,INPUT);
attachInterrupt(digitalPinToInterrupt(a),encoder,RISING);
}
void loop() {
  Serial.println(pos);
int e=target-pos;
if(e>0){
    digitalWrite(dir,HIGH);
    analogWrite(pwm,255);
    Serial.println("+");
  if(e=0){
  analogWrite(pwm,0);
  Serial.println("++");
}}
else if(e<0){
   if(e=0){
    digitalWrite(dir,LOW);
    analogWrite(pwm,255);
    Serial.println("-");
  }
  analogWrite(pwm,0);
  Serial.println("--");
}
}
void encoder(){
  int v=digitalRead(b);
  if(v>0){
    pos++;
  }
  else{
    pos--;
  }  
}