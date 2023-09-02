// PROGRAM: Switch
// Description: This program adds a switch to turn on and off the LED

// Define the pin numbers for LED and the switch
int LED1 = 12;        // Pin number for the LED
int LED2 = 11;        // Pin number for the LED
int LED3 = 10;        // Pin number for the LED
int switch1 = 4;     // Pin number for the switch
int switch2 = 3;     // Pin number for the switch
int switch3 = 2;     // Pin number for the switch

void setup() {
  // Setup code that runs once at the beginning

  pinMode(LED_BUILTIN, OUTPUT);  // Set the built-in LED pin as an output
  pinMode(LED1, OUTPUT);          // Set the LED pin as an output
  pinMode(LED2, OUTPUT);          // Set the LED pin as an output
  pinMode(LED3, OUTPUT);          // Set the LED pin as an output
  pinMode(switch1, INPUT);       // Set the switch pin as an input
  pinMode(switch2, INPUT);       // Set the switch pin as an input
  pinMode(switch3, INPUT);       // Set the switch pin as an input
}

void loop() {
  //now within loop() we'll take actions based on the status of the switches
  
  //testing...
  
    if (digitalRead(switch1) == HIGH){     //check switch #1
    digitalWrite(LED1, HIGH); // turn LED ON  
  }
  else {
    digitalWrite(LED1, LOW); // turn LED OFF
  }
  
    if (digitalRead(switch2) == HIGH){     //check switch #2
    digitalWrite(LED2, HIGH); // turn LED ON  
  }
  else {
    digitalWrite(LED2, LOW); // turn LED OFF
  }
  
    if (digitalRead(switch3) == HIGH){     //check switch #3
    digitalWrite(LED3, HIGH); // turn LED ON  
  }
  else {
    digitalWrite(LED3, LOW); // turn LED OFF
  }
  if ((digitalRead(switch1) == HIGH) && (digitalRead(switch2) == HIGH) && (digitalRead(switch3) == HIGH))
  {
    do
    {
      digitalWrite(LED1, HIGH);
      delay(100);
      digitalWrite(LED1, LOW);
      delay(100);
      digitalWrite(LED2, HIGH);
      delay(100);
      digitalWrite(LED2, LOW);
      delay(100);
      digitalWrite(LED3, HIGH);
      delay(100);
      digitalWrite(LED3, LOW);
      delay(100);
    }while((digitalRead(switch1) == HIGH) && (digitalRead(switch2) == HIGH) && (digitalRead(switch3) == HIGH));
  }
  if ((digitalRead(switch1) == HIGH) && (digitalRead(switch2) == HIGH) && (digitalRead(switch3) == LOW))
  {
    do
    {
      digitalWrite(LED3, LOW);
      delay(100);
      digitalWrite(LED3, HIGH);
      delay(100);
      digitalWrite(LED2, LOW);
      delay(100);
      digitalWrite(LED2, HIGH);
      delay(100);
      digitalWrite(LED1, LOW);
      delay(100);
      digitalWrite(LED1, HIGH);
      delay(100);
    }while((digitalRead(switch1) == HIGH) && (digitalRead(switch2) == HIGH) && (digitalRead(switch3) == LOW));
  }
  if ((digitalRead(switch1) == HIGH) && (digitalRead(switch2) == LOW) && (digitalRead(switch3) == HIGH))
  {
    do
    {
      digitalWrite(LED2, LOW);
      delay(100);
      digitalWrite(LED2, HIGH);
      delay(200);
      digitalWrite(LED1, LOW);
      digitalWrite(LED3, LOW);
      delay(200);
      digitalWrite(LED1, HIGH);
      digitalWrite(LED3, HIGH);
      delay(200);
    }while((digitalRead(switch1) == HIGH) && (digitalRead(switch2) == LOW) && (digitalRead(switch3) == HIGH));
  }
}