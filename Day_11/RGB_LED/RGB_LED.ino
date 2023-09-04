/*
  Title: RGB LED Control
  Description: This Arduino code controls an RGB LED using PWM to create various colors with delays between transitions.
*/

int red_pin = 9;
int green_pin = 10;
int blue_pin = 11;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set the RGB pins as OUTPUT
  pinMode(red_pin, OUTPUT);
  pinMode(green_pin, OUTPUT);
  pinMode(blue_pin, OUTPUT);
}

// Function to set RGB color using PWM
void RGB(int red, int green, int blue) {
  analogWrite(red_pin, red);
  analogWrite(green_pin, green);
  analogWrite(blue_pin, blue);
}

void loop() {
  // Main loop to create different colors and display with delays
  RGB(0, 0, 0); // Black
  delay(2000);
  RGB(255, 0, 0); // Red
  delay(2000);
  RGB(0, 255, 0); // Green
  delay(2000);
  RGB(0, 0, 255); // Blue
  delay(2000);
  RGB(255, 255, 0); // Yellow
  delay(2000);
  RGB(255, 0, 255); // Pink
  delay(2000);
  RGB(0, 255, 255); // Cyan
  delay(2000);
  RGB(255, 255, 255); // White
  delay(2000);
}
