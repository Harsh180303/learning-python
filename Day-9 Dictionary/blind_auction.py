import os

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

# Store all bids in a dictionary
auction_bids = {}

# Add a new bid
def add_bid(name, bid_price) :
    auction_bids[name] = bid_price

# Find highest bidder
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"\n🏆 The winner of the auction is {winner} with a bid of ${highest_bid}.")

# Main loop
def start_auction():
    print("🏁 Welcome to the Blind Auction 🏁\n")
    bidding_finished = False

    while not bidding_finished:
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))

        add_bid(name=name, bid_price=bid)
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'").lower()
        if more_bidders == 'no':
            bidding_finished = True
        elif more_bidders == 'yes':
            clear()
        else:
            print("Invalid input. Ending bidding by default.")
            bidding_finished = True

    clear()
    find_highest_bidder(auction_bids)

# Run the auction
start_auction()