# Python Loops

## for Loop

- Used to iterate over a sequence of items.
- Implemented using the reserved keyword **for**.
- for-loop code is executed for each *element* of the sequence.
- Get out of the for loop using the **break** statement.
- Use **continue** statement to skip the execution of the code in the for loop for an element.
- Python for loop is different from other programming languages as it behaves more like an **iterator**.
- Use for loop to iterate over **Tuple**, **List**, **Set**, or **String**.
  - All of these objects are a sequence in Python.
- We can have **nested for loops** to iterate over a sequence of sequences. 

## for Loop Syntax
- Uses  **in** operator to iterate over the elementes in the sequence.

      for element in sequence::
        # for statement code block
  
## Flow Diagram of for Loop
![](https://github.com/JeffLoboz/100DaysOfPython/blob/main/images/for-loop-flow-diagram.jpg)


## for Loop Examples
- Examples of for loop with different types of sequences.


### String
- Python string is a sequence of characters. 
- Program to print the index and character in a string.

      message = "Hello"

      count = 0
      for character in message:
          print(f'Index:{count}, Character:{character}')
          count += 1
    
Output: 

    Index:0, Character: H
    Index:1, Character: e
    Index:2, Character: l
    Index:3, Character: l
    Index:4, Character: o


### for Loop with range() function
- range() function generates a sequence of numbers.
- Use with for loop to execute a code block for a specific number of times.
- We will try with for loop to execute a code block 5 times. 

      for i in range(5):
          print("Processing for loop:", i)

Output:

    Processing for loop: 0
    Processing for loop: 1
    Processing for loop: 2
    Processing for loop: 3
    Processing for loop: 4
