#include <Key.h>
#include <Keypad.h>

const byte ROWS = 4;
const byte COLS = 4;

int buzzerPin = 10;

byte rowPins[ROWS] = {5, 4, 3, 2};
byte colPins[COLS] = {6, 7, 8, 9};
// Uncomment one of the button setups based on your purpose:
// Button setup for practice keypad setup
char buttons[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'},
};

// Create a Keypad object named 'myPad' with the specified button configuration and pin settings
Keypad myPad = Keypad(makeKeymap(buttons), rowPins, colPins, ROWS, COLS);

int tones[ROWS][COLS] = {
  {100, 200, 300, 400},
  {500, 600, 700, 800},
  {900, 1000, 700, 800},
  {1000, 2000, 3000, 4000},
};

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  int toneFrequency = 0;
  // Main loop to read keypad input and print to serial monitor
  char result = myPad.getKey();

  if (result) {
    for(byte i = 0; i < ROWS; i++){
      for(byte j = 0; j < COLS; j++){
        if(result == buttons[i][j]){
          toneFrequency = tones[i][j];
        }
      }
    }

    Serial.print("Key: ");
    Serial.println(result);
    Serial.print("Frequency: ");
    Serial.println(toneFrequency);

    tone(buzzerPin, toneFrequency, 200);
    delay(200);
    noTone(buzzerPin);
  }
}
