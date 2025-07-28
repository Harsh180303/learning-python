import os

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

auction_bids = []


def auction(name, bid_price) :
    new_bid = {}
    new_bid["name"] = name
    new_bid["bid_price"] = bid_price
    auction_bids.append(new_bid)


more_bidders = 'yes'
while more_bidders == 'yes':
    name = input("What is your name? ")
    bid = int(input("What is your Bid Price? $"))
    auction(name=name, bid_price=bid)
    clear()
    more_bidders = input("Is there anyone else who want's to bid 'yes' or 'no'? ").lower()

clear()
max_bid = 0
winner = ''
for bid in auction_bids:
    if bid["bid_price"] > max_bid :
        max_bid = bid["bid_price"]
        winner = bid['name']

print(f"The winner of the auction is {winner} with ${max_bid}")