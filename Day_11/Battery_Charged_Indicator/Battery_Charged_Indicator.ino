// Title: Battery LED Indicator
// Description: This code controls an RGB LED using three PWM pins to display different colors in a loop and displays the battery charge percentage.

// Define the analog pin for the battery sensor
int sensorPin = A0;
int sensorValue = 0;

// Define the pins for the RGB LED
int red_pin = 9;
int green_pin = 10;
int blue_pin = 11;

// Define the total battery capacity and current battery level
unsigned int batteryCapacity = 50000;
unsigned int batteryLevel = 0;

// Variables for time tracking
unsigned int ticks = 0;
unsigned int wait = 100;
double percentFull;

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);
  
  // Set the pinMode for the RGB LED pins as OUTPUT
  pinMode(red_pin, OUTPUT);
  pinMode(green_pin, OUTPUT);
  pinMode(blue_pin, OUTPUT);
}

// Function to set the RGB LED color
void RGB(int red, int green, int blue)
{
  analogWrite(red_pin, red);     // Set the intensity of the red LED
  analogWrite(green_pin, green); // Set the intensity of the green LED
  analogWrite(blue_pin, blue);   // Set the intensity of the blue LED
}

// Function to calculate the battery charge percentage
double getBatteryPercentage() {
  return (((double)batteryLevel / (double)batteryCapacity) * 100);
}

// Function to display battery charge percentage and control LED color
void ShowBatteryPercentage() {
  // Calculate the charge percentage with a custom function
  percentFull = getBatteryPercentage();

  if(ticks % 1000 == 0) {
    // Print the elapsed time
    Serial.print((ticks/1000));
    Serial.print(" seconds  --->  charge at ");
    // Print the percent charge
    Serial.print(percentFull);
    // Print a percent character and line return
    Serial.println("%");
  
    // Set the LED color based on charge percentage
    if (percentFull >= 0 && percentFull <= 25) {
      RGB(125, 0, 0); // Red
    }
    else if (percentFull > 25 && percentFull <= 75) {
      RGB(255, 140, 0); // Orange
    }
    else if (percentFull > 75 && percentFull < 100) {
      RGB(0, 128, 0); // Green
    }
  }
  else {
    return;
  }
}

void loop() {
  // Read the value from the battery sensor
  sensorValue = analogRead(sensorPin);
  batteryLevel += sensorValue;
  ticks += wait;
 
  if(batteryLevel >= batteryCapacity) {
    while(true){
      // Battery fully charged
      Serial.print((ticks/1000));
      Serial.print(" seconds  --->  ");
      Serial.println("FULLY CHARGED");
      batteryLevel = batteryCapacity; // Prevent integer overflow
      ticks = 0;
      RGB(0, 255, 0); // Green
      delay(500);
      RGB(0, 0, 255); // Blue
      delay(50);
      RGB(255, 255, 0); // Yellow
      delay(500);
      RGB(255, 0, 255); // Pink
      delay(500);
      RGB(0, 255, 255); // Cyan
    }
  }
  else {
    ShowBatteryPercentage();
  }
 
  delay(wait);
}
