from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.\n")

#Created an empty dictionary
bids = {}

#Keep track if bidding is finished
bidding_finished = False

def find_highest_bidder(bidding_record):
    #use for loop to look through each KEY records
    #Use key to get value for each bidder
    #pass in the key [bidder]
    #save it in bid_amount
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        
    print(f"\n\nThe winner is {winner} with a bid of ${highest_bid}.")



while not bidding_finished:
    #Asking the user for their name and bid $ amount
    name = input("What is your name? \n")
    price = int(input("\nWhat is your bid? \n$"))

    #Adding entries to bids dictionary
    bids[name] = price

    #Must provide condition to exit loop
    #Unless user types no, loop will keep going
    should_continue = input("\nAre there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
