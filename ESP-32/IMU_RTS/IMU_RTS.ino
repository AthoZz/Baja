#include <Arduino.h>
#include <ArduinoJson.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_MPU6050.h>

#define SDA_1 27
#define SCL_1 26

#define SDA_2 33
#define SCL_2 32
#define MESS 35





Adafruit_MPU6050 mpuOne;
Adafruit_MPU6050 mpuTwo;
Adafruit_MPU6050 mpuThree;
Adafruit_MPU6050 mpuFour;

Adafruit_Sensor *mpu_temp, *mpu_accel, *mpu_gyro;

TwoWire I2Cone = TwoWire(0);
TwoWire I2Ctwo = TwoWire(1);


struct Coord {
  float x, y, z;
};

int MPU6050_RANGE=1;
float x1, y11, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4 ;
bool StatusMPU1, StatusMPU2, StatusMPU3, StatusMPU4 = 0;


void SENDPi() {
  static unsigned long Time = millis();
  if (millis() - Time> 500 ){
    Serial.println("PIN ON");
    Time = millis();
  }
  
  
}

void I2CScanner() {
  byte error, address;
  int nDevices;

  Serial.println("Scanning...");
  nDevices = 0;
  for(address = 1; address < 127; address++ ) {
    I2Cone.beginTransmission(address);
    error = I2Cone.endTransmission();
    if (error == 0) {
      Serial.print("I2C device found at address 0x");
      if (address<16) {
        Serial.print("0");
      }
      Serial.println(address,HEX);
      nDevices++;
    }
    else if (error==4) {
      Serial.print("Unknow error at address 0x");
      if (address<16) {
        Serial.print("0");
      }
      Serial.println(address,HEX);
    }    
  }
  if (nDevices == 0) {
    Serial.println("No I2C devices found\n");
  }
  else {
    Serial.println("done\n");
  }
  delay(5000);          
}


void setupMPUOne()
{

 Serial.println(" MPU6050 1 sensor Found! Setup!");
 StatusMPU1 = 1;
  mpuOne.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: 8G");
  
  mpuOne.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: 500deg");
  
  mpuOne.setFilterBandwidth(MPU6050_BAND_5_HZ);
  Serial.print("Filter bandwidth set to: 5Hz");
  
  Serial.println("");
  delay(100);
}

struct Coord getMPUOne() {
  sensors_event_t a, g, temp;
  mpuOne.getEvent(&a, &g, &temp);
  struct Coord MPU1;

  
  MPU1.x=a.acceleration.x;
  MPU1.y=a.acceleration.y;
  MPU1.z=a.acceleration.z;
 
  delay(100);
  return MPU1;
}

void setupMpuTwo()
{

 Serial.println(" MPU6050 2 sensor Found!");
  StatusMPU2 = 1;
  mpuTwo.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: 8G");
  
  mpuTwo.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: 500deg");
  
  mpuTwo.setFilterBandwidth(MPU6050_BAND_5_HZ);
  Serial.print("Filter bandwidth set to: ");
   
  Serial.println("");
  delay(100);
}

struct Coord getMpuTwo() {
  //JsonDocument doc2;
  sensors_event_t a, g, temp;
  mpuTwo.getEvent(&a, &g, &temp);
  struct Coord MPU2;

  
  MPU2.x=a.acceleration.x;
  MPU2.y=a.acceleration.y;
  MPU2.z=a.acceleration.z;
  
  delay(100);
  return MPU2;
}

void setupMPUThree()
{

 Serial.println(" MPU6050 3 sensor Found! Setup!");
  StatusMPU3 = 1;
  mpuThree.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: 8G");
  
  mpuThree.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: 500deg");
  
  mpuThree.setFilterBandwidth(MPU6050_BAND_5_HZ);
  Serial.print("Filter bandwidth set to: 5Hz");
  
  Serial.println("");
  delay(100);
}


struct Coord getMPUThree() {
 // JsonDocument doc;
  sensors_event_t a, g, temp;
  mpuThree.getEvent(&a, &g, &temp);
  struct Coord MPU3;

 
  MPU3.x=a.acceleration.x;
  MPU3.y=a.acceleration.y;
  MPU3.z=a.acceleration.z;


  delay(100); 
  return MPU3;
}


void setupMPUFour()
{

 Serial.println(" MPU6050 4 sensor Found! Setup!");
  StatusMPU4 = 1;
  mpuFour.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Accelerometer range set to: 8G");
  
  mpuFour.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: 500deg");
  
  mpuFour.setFilterBandwidth(MPU6050_BAND_5_HZ);
  Serial.print("Filter bandwidth set to: 5Hz");
  
  Serial.println("");
  delay(100);
  
}


struct Coord getMPUFour() {
 // JsonDocument doc;
  sensors_event_t a, g, temp;
  mpuFour.getEvent(&a, &g, &temp);
  struct Coord MPU4;

  
  MPU4.x=a.acceleration.x;
  MPU4.y=a.acceleration.y;
  MPU4.z=a.acceleration.z;

  delay(100);
  return MPU4;
}



void setup() {
  Serial.begin(115200);
  I2Cone.begin(SDA_1, SCL_1, 100000); 
  I2Ctwo.begin(SDA_2, SCL_2, 100000);
  I2CScanner();
  pinMode(MESS, INPUT_PULLDOWN);
  attachInterrupt(digitalPinToInterrupt(MESS), SENDPi, RISING);

   
  bool status1 = mpuOne.begin(0x68, &I2Cone);  
  delay(100);
  if (!status1) {
    Serial.println("Could not find a valid MPU6050 1 sensor, check wiring!");
    
  }
  if(status1) {
    Serial.println((String)"Device found on pin "+SDA_1+" & "+SCL_1+"& adress x68");
    setupMPUOne();
  }

  delay(100);
  bool status2 = mpuTwo.begin(0x69, &I2Cone);  
  delay(100);
  if (!status2) {
    Serial.println("Could not find a valid MPU6050 2 sensor, check wiring!");  
  }
  if (status2) {
    Serial.println((String)"Device found on pin "+SDA_1+" & "+SCL_1+"& adress x69");
    setupMpuTwo();
  }


  bool status3 = mpuThree.begin(0x68, &I2Ctwo);  
  delay(100);
  if (!status3) {
    Serial.println("Could not find a valid MPU6050 3 sensor, check wiring!");  
  }
  if (status3) {
    Serial.println((String)"Device found on pin "+SDA_2+" & "+SCL_2+"& adress x68");
    setupMPUThree();
  }

  bool status4 = mpuFour.begin(0x69, &I2Ctwo);  
  delay(100);
  if (!status4) {
    Serial.println("Could not find a valid MPU6050 4 sensor, check wiring!");  
  }
  if (status4) {
    Serial.println((String)"Device found on pin "+SDA_2+" & "+SCL_2+"& adress x69");
    setupMPUFour();
  }
  
   
   delay(2000);

}

void loop() {
      JsonDocument doc;
      Serial.println(digitalRead(MESS));
        if (digitalRead(MESS) == 1) {
    if (StatusMPU1==1){
      struct Coord MPU1 = getMPUOne();
      doc["ID"] = "1";
      doc["x"] = MPU1.x;
      doc["y"] = MPU1.y;
      doc["z"] = MPU1.z;
      //Serial.println(MPU1.x);

      serializeJson(doc, Serial);
    
  }
  if (StatusMPU2==1){
    struct Coord MPU2 = getMpuTwo();
    //Serial.println(MPU2.x);
  }
  if (StatusMPU3==1){
    struct Coord MPU3 = getMPUThree();
    //Serial.println(MPU3.x);
  }
  if (StatusMPU4==1){
    struct Coord MPU4 = getMPUFour();
    //Serial.println(MPU4.x);
  }
  }
  
  
  //getMpuTwo();
  //Serial.println("A");
  
  delay(1000);

}



/*
Reste à faire les packet Json pour acc 2-3-4, et des les envoyer juste quand ya le iinterrupt 
*/