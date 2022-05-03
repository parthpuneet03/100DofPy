from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
def highest_Bidder(auction):
    highest_bid=0
    highest_bidder=""
    for key in auction:
        if auction[key]>highest_bid:
            highest_bid=auction[key]
            highest_bidder=key
    print(f"The winner of the bid is {highest_bidder} with a bid of ${auction[highest_bidder]}.")
print(logo)
print("Welcome to the silent bidding program")
auction={}
keep_bidding=True


while keep_bidding:
    name=input("What is your name?: ")
    bid= int(input("What's your bid?: $"))
    auction[name]=bid
    Bidders=input("Are there any other bidders? Type 'yes' or 'no'.").lower().strip()
    if Bidders=="no":
        keep_bidding=False
        clear()
    else:
        clear()
highest_Bidder(auction)
