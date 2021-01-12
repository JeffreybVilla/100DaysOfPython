# Python Dictionaries
    Define dictionary with key : value
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




## Nesting
    capitals = {
        "France:" "Paris",
        "Germany:" "Berlin"
    }

## Nesting a List in a programming_dictionary
    travel_log = {
        "France": ["Paris", "Lille", "Dijon"],
        "Germany": ["Berlin", "Hamburg", "Stuttgart"]
    }


## Nesting a List in a List
    ["A", "B", ["C", "D"]]


## Nesting a Dictionary in a Dictionary
    travel_log = {
        "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
        "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
    }


## Nesting a Dictionary inside a list
     [{
         Key: [List],
         Key2: {Dict},
     },
     {
         Key: Value,
         Key2: Value,
     }]

## Multiple Nesting
    A list that contains 2 items.
    Each item is a Dictionary
    Each Dictionary has 3 Key Value pairs
    3 Different data types
    Country key has a string value
    cities_visited key has a list Value
    total_visits key has a number value
    travel_log = [
      {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
      },
      {
        "Country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
      },
    ]
