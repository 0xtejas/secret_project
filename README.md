# secret_project


## Python Challenge

- First upon analyzing the program we can find that there are three main functions used
  1. xor
  2. Hex convertor
  3. shift 
  
 - As we try to deconstruct the program by commenting all the functions except xor function, and try to see what the xor function does to the input given a single character,
   we get an output of xor of the char. lets see if the fucntion is a reversible function. So lets use the output which we have got as the input to see if we get the charater
   which we used in the first step. Yes! we get the same character. Hece this function is a reversible function.
  
 - Now Lets see what the shift function does. It converts the text to a ascii value and shifts it. We know that modulo has no invertable operator. Thus, we need not worry to 
   reverse the operator. Lets inverse the (+) operator to (-) and vice-versa. Now we have made the function to deshift the input.
   
  - The Finaly function encode, converts the string to a hex format. We can use binascii python module to unhexify
  
  - Logically we reconstruct the function to our advantage. And give the cipher text as input, Hurray we have solved this challenge. 
  
  </br >
  
  
## Reverse ME

- Here if you notice the hexdump of the corrupted file you will notice that the order of the bytes are changed. Which means its upside down. How did I know that?
  By checking the first and last line for the hex header for png file, I found the last line had it, but the nibbles were reversed to.
 
- First I extract the hex data from the corrupted file in bottom to top manner.
- Then, I swapped the nibble position (For Example: 89 -> 98).
- THe used hexdump library to reconstruct the image from the hex.
