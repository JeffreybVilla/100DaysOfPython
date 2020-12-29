# Python List Data Structure

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





# CODE
# WITHOUT LISTS
state1 = "Delaware"
state2 = "Pennyslvania"
state3 = "New Jersey"

food1 = "Strawberries"
food2 = "Spinach"

print(f"{state1}, {state2}, {state3}, {food1}, {food2}\n\n\n")



# WITH LISTS
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(f"{states_of_america}\n\n\n")

# To print first state
print(states_of_america[0])


# To print third state
print(states_of_america[2])


# To print last state in list
print(states_of_america[-1])


# To change data of list
states_of_america[1] = "pencilvania"
print(f"{states_of_america[1]}")


# Append/Add element to end of list (queue)
# Use append function to add SINGLE item 
states_of_america.append("JeffreyLand")
print(f"\n\n\n{states_of_america}")


# Extend/Add element to end of list (queue)
# Use append function to add MULTIPLE item 
states_of_america.extend(["DadLand", "PhoebeLand","MomLand"])
print(f"\n\n\n{states_of_america}")

