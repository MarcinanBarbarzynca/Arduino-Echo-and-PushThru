//int VCC = 20;
//int GND = 17;

int a = 0;
int b = 0;
void setup() {
  //  pinMode(VCC,OUTPUT);
  //  pinMode(GND,OUTPUT);
  //digitalWrite(VCC,HIGH);
  //digitalWrite(GND,LOW);
  Serial.begin(9600);
  Serial1.begin(9600);
  Serial2.begin(9600);
}

void loop() {
  if (Serial.available()) {      // If anything comes in Serial (USB),
    a = Serial.read();
    Serial1.write(a);   // read it and send it out Serial1 (pins 0 & 1)
    b =  Serial2.read();   // read it and send it out Serial1 (pins 0 & 1)
    Serial.write(b);
  }

}
