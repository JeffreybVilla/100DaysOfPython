# Python Dictionaries
    Define a dictionary with Key : Value
    programming_dictionary = {
        "Bug": "An error in a program that prevents the program from running as expected.",
        "Function": "A piece of code that you can easily call over and over again.",
    }


## Retrieving items from dictionary.
    print(programming_dictionary["Bug"])


## Adding new items to dictionary
    programming_dictionary["Loop"] = "The action of doing something over and over again."
    print(programming_dictionary)


## Create empty dictionary
    empty_dictonary = {}


## Wipe an existing dictionary
    programming_dictionary = {}
    print(programming_dictionary)


## Edit an item in dictionary
    programming_dictionary["Loop"] = "Loopy thing"
    print(programming_dictionary)



## Loop through a dictionary
    for key in programming_dictionary:
        print(key)
        print(programming_dictionary[key])
