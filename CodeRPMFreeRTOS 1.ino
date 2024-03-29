#include <Arduino_FreeRTOS.h>
#include <semphr.h>


/******* *************** *********/
/******* Global Variables ********/
/******* *************** *********/
#define PIN_TACH1 2
#define PIN_TACH2 3
#define SIZE_BUFFER 15 // based on a minimum of 1000RPM
SemaphoreHandle_t mRPM1; // mutex
SemaphoreHandle_t mRPM2; // mutex
long timerRPM1; // No mutex needed
long timerRPM2; // No mutex needed
float RPM1[15]; // RPM buffer, mutexed
float RPM2[15]; // RPM buffer, mutexed
TickType_t lastPrint; // vTaskDelayUntil timemark
int printDelay = 1000; // Print delay of vTaskUntil


/******* *************** *********/
/******* Task prototypes *********/
/******* *************** *********/
void PrintRPM( void *pvParameters );
void ISR_tach1();
void ISR_tach2();


void setup()
{
    // Initilize pin
    pinMode(PIN_TACH1, INPUT);
    pinMode(PIN_TACH2, INPUT);

    // Begin serial comm
    Serial.begin(9600);

    // Initialize mutex
    mRPM1 = xSemaphoreCreateMutex();
    mRPM2 = xSemaphoreCreateMutex();

    // Initial time for RPM timers
    timerRPM1 = micros();
    timerRPM2 = micros();

    // Initialize arrays
    for (int i=0; i<SIZE_BUFFER; i++)
  {
    RPM1[i] = 0;
    RPM2[i] = 0;
  }

    // ISR initializing
    attachInterrupt(digitalPinToInterrupt(PIN_TACH1), ISR_tach1, RISING);
    attachInterrupt(digitalPinToInterrupt(PIN_TACH2), ISR_tach2, RISING);

    // Task creation
    xTaskCreate(PrintRPM,"Calculate average RPM and print it",128,NULL,1,NULL);

    // End of setup
    Serial.println("Setup done");
}

void loop()
{    

}

///////////////////////////
// ***     TASKS     *** //
///////////////////////////

void PrintRPM( void * pvParameters )
/*
  Task test
*/    
 {
    (void) pvParameters;
    // Initialize print timer
    lastPrint = xTaskGetTickCount();
    float averageRPM1 = 0;
    float averageRPM2 = 0;
     for( ;; )
     {
      averageRPM1 = 0;
      averageRPM2 = 0;

      if(xSemaphoreTake(mRPM1, 15) == 1)
      {
        for (int i=0; i<SIZE_BUFFER; i++)
        {
          averageRPM1 += RPM1[i];
        }
      }
      averageRPM1 = averageRPM1/SIZE_BUFFER;

      if(xSemaphoreTake(mRPM2, 15) == 1)
      {
        for (int i=0; i<SIZE_BUFFER; i++)
        {
          averageRPM2 += RPM2[i];
        }
      }
      averageRPM2 = averageRPM2/SIZE_BUFFER;

      Serial.println("RPM du tachymètre 1 : " + String(averageRPM1));
      Serial.println("RPM du tachymètre 2 : " + String(averageRPM2));

      Serial.println(digitalRead(7));
      Serial.println(digitalRead(8));

      vTaskDelayUntil( &lastPrint, 1000/portTICK_PERIOD_MS );
     }
 }


///////////////////////////
// ***      ISR      *** //
///////////////////////////
 
void ISR_tach1()
/*
  Interupt for Tachymeter pin
*/ 
{
  float difTemps = abs(micros()-timerRPM1)/1000000.0;
  if (xSemaphoreTakeFromISR(mRPM1, pdTRUE) == 1);
  {
    for (int i=SIZE_BUFFER-1; i>0; i--)
    {
      RPM1[i] = RPM1[i-1];
    }
    RPM1[0] = 60/difTemps;
    xSemaphoreGiveFromISR(mRPM1, pdTRUE);
  }
  timerRPM1 = micros();
}

void ISR_tach2()
/*
  Interupt for Tachymeter pin
*/ 
{
  float difTemps = abs(micros()-timerRPM2)/1000000.0;
  if (xSemaphoreTakeFromISR(mRPM2, pdTRUE) == 1);
  {
    for (int i=SIZE_BUFFER-1; i>0; i--)
    {
      RPM2[i] = RPM2[i-1];
    }
    RPM2[0] = 60/difTemps;
    xSemaphoreGiveFromISR(mRPM2, pdTRUE);
  }
  timerRPM2 = micros();
}