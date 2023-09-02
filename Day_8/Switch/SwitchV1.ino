// PROGRAM: Switch
// Description: This program adds a switch to turn on and off the LED

// Define the pin numbers for LED and the switch
int LED = 12;        // Pin number for the LED
int switch1 = 2;     // Pin number for the switch

void setup() {
  // Setup code that runs once at the beginning

  pinMode(LED_BUILTIN, OUTPUT);  // Set the built-in LED pin as an output
  pinMode(LED, OUTPUT);          // Set the LED pin as an output
  pinMode(switch1, INPUT);       // Set the switch pin as an input
}

void loop() {
  // Main code that runs repeatedly

  // Check if the switch is in the ON position (HIGH)
  if (digitalRead(switch1) == HIGH) {
    digitalWrite(LED_BUILTIN, HIGH); // Turn on the built-in LED
    digitalWrite(LED, HIGH);         // Turn on the external LED connected to pin 12
  } else {
    digitalWrite(LED, LOW);          // Turn off the external LED

    // Entering a loop to blink the built-in LED while the switch is OFF
    while (digitalRead(switch1) == LOW) {
      digitalWrite(LED_BUILTIN, HIGH); // Turn on the built-in LED (5V)
      delay(500);                      // Delay for half a second (LED ON)
      digitalWrite(LED_BUILTIN, LOW);  // Turn off the built-in LED (0V)
      delay(500);                      // Delay for half a second (LED OFF)
    }
    // Exiting the loop when the switch is turned ON again
  }
}