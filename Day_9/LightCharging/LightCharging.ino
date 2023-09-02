/************************************************************
  Title: Battery Charging Monitor with Light Sensor
  Description: This Arduino program monitors a light sensor
  connected to analog pin A0 and uses the sensor readings to
  simulate charging a battery. It keeps track of the cumulative
  sensor readings as if they were charging the battery and
  calculates the battery's charge level as a percentage.
************************************************************/

// Define the analog input pin for the light sensor
int sensorPin = A0;

// Define the digital output pin for the onboard LED (usually 13 on many Arduino boards)
int onboardLED = 13;

// Variable to store the current sensor reading
int sensorValue = 0;

// Variables related to battery monitoring
unsigned int batteryCapacity = 50000;
unsigned int batteryLevel = 0;
unsigned int ticks = 0;
unsigned int wait = 100;
double PercentFull;

void setup() {
  // Setup code that runs once when the Arduino starts or is reset

  // Set the onboard LED pin as an output
  pinMode(onboardLED, OUTPUT);

  // Initialize communication with the computer via the serial port
  Serial.begin(9600);
}

void PrintBatteryPercentage() {
  // Print the elapsed time
  Serial.print(ticks);
  Serial.print(" ms    charge at ");

  // Convert the integers to decimal numbers, divide them, and print as a percentage
  PercentFull = 100 * ((double)batteryLevel / (double)batteryCapacity);
  Serial.print(PercentFull);

  // Print a percent character and line return
  Serial.println("%");
}

void loop() {
  // Main code that runs repeatedly

  // Read the value from the light sensor
  sensorValue = analogRead(sensorPin);

  // Accumulate sensor readings as if they were charging the battery
  batteryLevel += sensorValue;
  ticks += wait;

  if (batteryLevel >= batteryCapacity) {
    Serial.print(ticks);
    Serial.print(" ms     ");
    Serial.println("FULLY CHARGED");
    batteryLevel = batteryCapacity; // Prevent integer from continuing to increase
    ticks = 0;
    delay(20000); // Long pause
  } else {
    // Print battery charge percentage
    PrintBatteryPercentage();
  }

  // Delay before the next iteration
  delay(wait);
}
