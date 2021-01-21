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
