//Reading Light
//This program monitors a light sensor connected to pin A0 and using the sensor readings to determine the lighting conditions in a room. Based on the light level detected by the sensor, it takes different actions and can potentially shut down the Arduino under certain conditions.

// Define the analog input pin for the light sensor
int sensorPin = A0;

// Define the digital output pin for an onboard LED (usually 13 on many Arduino boards)
int onBoardLED = 13;

// Declare a variable to store the sensor reading
int sensorValue = 0;

// Variables to count different light conditions
int countBright = 0;
int countDim = 0;
int countDark = 0;

// Variables to manage battery status
unsigned int batteryCapacity = 50000;
unsigned int batteryLevel = 0;
unsigned int ticks = 0;
unsigned int wait = 100;
double percentFull; 

void setup() {
  // Setup code that runs once when the Arduino starts or is reset

  // Initialize communication with the computer via the serial port
  Serial.begin(9600);

  // Set the onboard LED pin as an output
  pinMode(onBoardLED, OUTPUT);
}

// Function to print battery percentage
void printBatteryPercentage(){
  Serial.print(ticks);
  Serial.print("ms charge at ");
  percentFull = 100 * ((double)batteryLevel / (double)batteryCapacity);
  Serial.print(percentFull);
  Serial.println("%");
}

void loop() {
  // Main code that runs repeatedly

  // Print a message to the serial monitor (the computer's screen)
  Serial.println("Charging battery with light sensor...");
  printBatteryPercentage();

  // Read the analog voltage from the sensor and store it in the sensorValue variable
  sensorValue = analogRead(sensorPin);

  // Print the sensor value to the serial monitor
  Serial.print("SensorValue: ");
  Serial.println(sensorValue);

  if(sensorValue > 100)
  {
    Serial.println("The room is bright!");
    digitalWrite(onBoardLED, HIGH);
    delay(5000);
    digitalWrite(onBoardLED, LOW);
    countBright++;
    if (countBright == 2)
    {
      Serial.println("The room is too bright! Shutting down...");
      delay(1000);
      exit(0);
    }
  }
  else if(sensorValue > 50 && sensorValue < 100)
  {
    Serial.println("The room is dim...");
    delay(1000);
    countDim++;
    if (countDim == 2)
    {
      Serial.println("The room has been dim for too long! Shutting down...");
      delay(1000);
      exit(0);
    }
  }
  else
  {
    Serial.println("The room is dark.");
    delay(1000);
    countDark++;
    if (countDark == 2)
    {
      Serial.println("The room has been dark for too long! Shutting down...");
      delay(1000);
      exit(0);
    }
  }
}
