# Function Parameters
![](https://github.com/JeffLoboz/100DaysOfPython/blob/main/images/Parameters-vs-Arguments.png)



## Positional Arguments
    def greet_with(name, location):
         print(f"I am {name}, and I'm from {location}")

     greet_with("Jeffrey", "Sacramento.")



## Keyword Arguments
    def greet_with(name, age, location):
        print(f"Hello {name}")
        print(f"Your age is {age}")
        print(f"From {location}")

    greet_with(location = "Sacramento", name = "Jeffrey", age = "26")

