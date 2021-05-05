void setup() {
Serial.begin(9600);
}
int a;
void loop() {
  
  if (Serial.available()) { 
    a = Serial.read();
    Serial.write(a);
  }

}
