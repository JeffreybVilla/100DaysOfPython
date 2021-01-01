# Python List Data Structure
# CODE
https://repl.it/@JeffreyV/day-4-list-practice


- Data structure: A way of organizing and storing data. 
- Storing single pieces of data is done with *variables*.

      a = 3
      b = "hello"
    
- To store grouped pieces of data that have connections with each other you can use a *List*.
- EX: All 50 states in United States of America. 
  - Doesn't make sense to store names of states individually. 
  - All states are related to each other. 
  - You can place states in certain order. 
  
  
  
## List
- Set of square brackets with many items stored inside.
- Order is determined by order of data input in list.
- The items can be any data type.
  - Mixed data types allowed. Like strings together with numbers or booleans.
EX:

    fruits = [item1, item2, item3]



# Nested List

      #dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries" "Pears", "Tomatoes", "Celery", "Potatoes"]

      # Make a Nested List to separate fruits & vegetables

      fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

      vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

      dirty_dozen = [fruits, vegetables]

      print(dirty_dozen)



