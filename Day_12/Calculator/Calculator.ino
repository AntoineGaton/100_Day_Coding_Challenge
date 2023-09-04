/*
Title: Simple Arduino Calculator
Description: This Arduino code implements a basic calculator using a 4x4 keypad for input.
NOTE: Decimal calculation doesn't work and is buggy, need to be fixed. Idea is to convert int into doubles and go from there.
*/

#include <Key.h>
#include <Keypad.h>

String userInput;
int num1 = 0;
int num2 = 0;
char operatorChar = ' ';
int result = 0;

void (*resetFunc)(void) = 0;

const byte ROWS = 4;
const byte COLS = 4;

byte rowPins[ROWS] = {5, 4, 3, 2};
byte colPins[COLS] = {6, 7, 8, 9};

char buttons[ROWS][COLS] = {
  {'1', '2', '3', '+'},
  {'4', '5', '6', '-'},
  {'7', '8', '9', '*'},
  {'0', '.', '=', '/'}
};

Keypad myPad = Keypad(makeKeymap(buttons), rowPins, colPins, ROWS, COLS);

void setup() {
  Serial.begin(9600);
  Serial.println("===============================");
  Serial.println("\tCalculator");
  Serial.println("===============================");
   // Print the button layout
  for (int i = 0; i < ROWS; i++) {
    for (int j = 0; j < COLS; j++) {
      Serial.print(buttons[i][j]);
      Serial.print('\t');
    }
    Serial.println();
  }
  Serial.println("===============================");
}

void loop() {
  char resultChar = myPad.getKey();

  if (resultChar) {
    Serial.print(resultChar);

    if (resultChar == '+' || resultChar == '-' || resultChar == '*' || resultChar == '/') {
      operatorChar = resultChar;
      num1 = userInput.toInt();
      userInput = ""; // Clear userInput for the next number input
    } else if (resultChar == '=') {
      num2 = userInput.toInt();
      calculateResult();
    } else if (resultChar != '.') {
      userInput.concat(resultChar);
    }
  }
}

void calculateResult() {
  switch (operatorChar) {
    case '+':
      result = num1 + num2;
      break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
      result = num1 * num2;
      break;
    case '/':
      if (num2 != 0) {
        result = num1 / num2;
      } else {
        Serial.println("Error: Division by zero");
      }
      break;
    default:
      Serial.println("Error: Invalid operator");
      break;
  }

  Serial.println(result);

  // Reset the calculator
  userInput = "";
  num1 = 0;
  num2 = 0;
  operatorChar = ' ';
}