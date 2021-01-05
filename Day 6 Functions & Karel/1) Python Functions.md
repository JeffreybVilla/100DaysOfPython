https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
https://www.askpython.com/python/python-functions

# Python Functions
    - A function is a block of code with a name.
    - We can call a function by its name. 
    - The code inside a function only runs when it's called.
    - A function can accept data from the caller program, it's called as function parameters.
    - The function parameters are inside parentheses and separated by a comma.
      - A function can accept any number of arguments.
    - A function can return data to the caller program.
      - Unline other popular programming languages, Python functions definition doesn't specify return type.
    - Can't use reserved keywords as function name.



## How to Define a Function?
    - Use **def** keyword to define a function.
    - def function_name(arguments):
          # code statements

    """
    def hello():
      print("Hello World!")

    def add(x, y):
      print(f"arguments are {x} and {y}")
      return x + y
    """

![](https://github.com/JeffLoboz/100DaysOfPython/blob/main/images/python-functions.png)



## How to Call a Function in Python?
    - Call a function by its name.
    - If the function accepts parameters, we have to pass them while calling the function. 

    """
    hello()
    sum = add(10, 5)
    print(f"sum is {sum}"
    """

    - We are calling hello() & add() functions that are defined by us.
    - Also calling print() function that is built-into Python.



## Python Function Types
    - 2 tpyes of funcitons in Python.
    1. Built-in functions: Functions provided by the Python language such as print(), len(), int(), etc
    2. User-defined functions: Functions defined by us in a Python program.



## Can a Function have default parameter value?
