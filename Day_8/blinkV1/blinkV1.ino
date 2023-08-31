// PROGRAM: BLINKV1
// Description: This program blinks an external LED connected to pin 8 of the Arduino,
// as well as the built-in LED on the Arduino board, creating an alternating blink pattern.
// This is a simple introductory example for learning how to use digital pins and control LEDs.

// Define the pin number for the external LED
int LED_PIN = 12;

void setup() {
  // This function is executed once when the Arduino starts up.
  
  // Configure the pin modes
  pinMode(LED_PIN, OUTPUT);         // Set up the external LED pin as an output
  pinMode(LED_BUILTIN, OUTPUT);     // Set up the built-in LED pin as an output
}

void loop() {
  // This function is executed repeatedly in a loop after the setup() function.
  
  // Turn on the external LED and turn off the built-in LED
  digitalWrite(LED_PIN, HIGH);     // Set the voltage of the external LED pin to HIGH (5V)
  digitalWrite(LED_BUILTIN, LOW);  // Turn off the built-in LED
  
  delay(125);  // Pause for half a second (500 milliseconds)
  
  // Turn off the external LED and turn on the built-in LED
  digitalWrite(LED_PIN, LOW);      // Set the voltage of the external LED pin to LOW (0V)
  digitalWrite(LED_BUILTIN, HIGH); // Turn on the built-in LED
  
  delay(250); // Pause for one second (1000 milliseconds)
}