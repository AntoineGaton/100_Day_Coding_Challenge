# create a hexadecimal to binary converter
# create a binary to hexadecimal converter
# create a decimal to hexadecimal converter
# create a hexadecimal to decimal converter
# create a binary fraction to decimal converter
# create a decimal to binary fraction converter
# create a decimal fraction to hexadecimal converter
# create a one's complement converter
# create a two's complement converter

import os # Used to clear the terminal
import time # Used to pause the program

# Function to clear the terminal
def clear_terminal():
   os.system('cls')

# Function to convert a string to binary
def string_to_binary(string):
   binary = ''
   for char in string:
      binary += decimal_to_binary(ord(char)) + ' ' # Convert each character to binary and add it to the binary string
   return binary

# Function to convert a binary string to a string
def binary_to_string(binary):
   string = ''
   binary = binary.split(' ') # Split the binary string into a list of binary numbers
   for num in binary:
      string += chr(binary_to_decimal(num)) # Convert each binary number to decimal and add it to the string
   return string

# Function to convert a binary number to decimal
def binary_to_decimal(binary_num):
   decimal = 0
   binary_num = binary_num[::-1]  # Reverse the binary string
   for i in range(len(binary_num)): # Iterate through the binary string
      if binary_num[i] == '1': # If the current digit is 1, add 2^i to the decimal value
         decimal += 2**i 
   return decimal

# Function to convert a decimal number to binary
def decimal_to_binary(num):
   if num == 0:
      return '0'
    
   binary = ''
   while num > 0: # Divide the number by 2 until it is 0
      remainder = num % 2 # The remainder is the current digit in the binary representation
      binary = str(remainder) + binary # Add the remainder to the beginning of the binary string
      num //= 2 # Divide the number by 2
   return binary

# Main function
def main():
   print("Binary to Decimal or Decimal to Binary Converter")

   binary = string_to_binary("Hello World")
   str = binary_to_string(binary)
   print("Binary: ", binary)
   print("String: ", str)
   
   while True:
      choice = input("Choose 'B' for Binary to Decimal, 'D' for Decimal to Binary, 'SB' for String to Binary,  'BS' for Binary to String, or 'Q' to quit: ").upper() # Get user input
      
      if choice == 'Q':
         break  # Exit the loop if 'Q' is pressed

      elif choice == 'B':
         binary_input = input("Enter a binary number: ") 
         decimal_result = binary_to_decimal(binary_input) # Convert the binary number to decimal
         print(f"The decimal representation of {binary_input} is: {decimal_result}")
         time.sleep(5)
         input("Press Enter to continue...")
         clear_terminal()

      elif choice == 'D':
         decimal_input = int(input("Enter a decimal number: "))

         if decimal_input < 0:
            print("Please enter a non-negative integer.")

         else:
            binary_result = decimal_to_binary(decimal_input)  # Convert the decimal number to binary
            print(f"The binary representation of {decimal_input} is: {binary_result}")
            time.sleep(3)
            input("Press Enter to continue...")
            clear_terminal()
      
      elif choice == 'SB':
         string_input = input("Enter a string: ")
         binary_result = string_to_binary(string_input)
         print(f"The binary representation of {string_input} is: {binary_result}")
         time.sleep(5)
         input("Press Enter to continue...")
         clear_terminal()
         return
      
      elif choice == 'BS':
         binary_input = input("Enter a binary string: ")
         string_result = binary_to_string(binary_input)
         print(f"The string representation of {binary_input} is: {string_result}")
         time.sleep(5)
         input("Press Enter to continue...")
         clear_terminal()

         return

      else:
         print("Invalid choice. Please choose 'B', 'D', or 'Q'.")

if __name__ == "__main__":
   main()