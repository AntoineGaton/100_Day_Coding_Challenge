/*
  Title: Keypad Input with Serial Output
  Description: This code reads input from a 4x4 keypad and prints the pressed buttons to the serial monitor. 
               It can be used for practice or to send a secret message.
*/

#include <Key.h>
#include <Keypad.h>

String inputWord;

const byte ROWS = 4;
const byte COLS = 4;

byte rowPins[ROWS] = {5, 4, 3, 2};
byte colPins[COLS] = {6, 7, 8, 9};

// Uncomment one of the button setups based on your purpose:
// Button setup for practice keypad setup
// char buttons[ROWS][COLS] = {
//   {'1', '2', '3', 'A'},
//   {'4', '5', '6', 'B'},
//   {'7', '8', '9', 'C'},
//   {'*', '0', '#', 'D'},
// };

// Button setup to send a message to my fiance!
char buttons[ROWS][COLS] = {
  {'I', 'L', 'O', 'V'},
  {'E', 'Y', 'O', 'U'},
  {'B', 'I', 'A', 'N'},
  {'C', 'A', ' ', '.'},
};

// Create a Keypad object named 'myPad' with the specified button configuration and pin settings
Keypad myPad = Keypad(makeKeymap(buttons), rowPins, colPins, ROWS, COLS);

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Main loop to read keypad input and print to serial monitor
  char result = myPad.getKey();

  if (result) {
    Serial.print("The button ");
    Serial.print(result);
    Serial.println(" was pressed.");

    if (result != '.') {
      inputWord.concat(result);
    }

    if (result == '.') {
      Serial.print("Word typed was ");
      Serial.println(inputWord);
      inputWord = "";
    }
  }
}
