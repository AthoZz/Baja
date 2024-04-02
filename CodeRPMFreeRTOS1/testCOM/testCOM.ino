void setup() {
  // put your setup code here, to run once:
  pinMode(52, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  digitalWrite(52, HIGH);
  Serial.println("1");
  delay(1000);
  digitalWrite(52, LOW);
  Serial.println("0");
}
