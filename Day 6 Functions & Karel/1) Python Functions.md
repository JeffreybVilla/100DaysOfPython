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
    - Python allows default values for the function parameters.
    - If the caller doesn't pass the parameter, then the default value is used.

    """
    def hello(year = 2021):
        print(f"Happy new year! #{year}")
    hello(2020) # function parameter is passed
    hello() # function parameter not passed, default value used
    """

    OUTPUT:
    Happy new year! #2020
    Happy new year! #2021
   


## Multiple return statements inside a Function?
    - Yes, a function have multiple return statements.
    - However, when one of the return statements is reached, the function execution terminates and value is returned to caller. 

    """
    def odd_even_checker(i):
        if i % 2 == 0:
            return "even"
        else:
            return "odd"

    print(odd_even_checker(20))
    print(odd_even_checker(15))
    """

    OUTPUT:
    even
    odd



## Python Function Return Multiple Values 1 by 1?
    - Yes, Python function can return multiple values one by one.
    - To implement, use the **yield** keyword.
    - Helpful when you want a function to return a large number of values and process them.
    - We can split the returned values into multiple chunks using **yield** statement.
    - This type of function is also called a generator function.

    """
    def return_odd_ints(i):
        x = 1
        while x <= i:
            yield x
            x += 2

    output = return_odd_ints(10)

    for out in output:
        print(out)
    """

    OUTPUT:
    1
    3
    5
    7
    9



## Python Function Variable Arguments
