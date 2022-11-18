import os
from art import logo

print(logo)
store_data = {}
bidding_on = True


def h_bidder(bid_record):
    h_bid = 0
    winner = ""
    for x in bid_record:
        bid_amount = bid_record[x]
        if bid_amount > h_bid:
            h_bid = bid_amount
            winner = x
    print(f"the winner is {winner} with bid${h_bid}")


while bidding_on:
    name = input("name of the bidder: ")
    value = int(input("place bid: $"))
    store_data[name] = value
    bidding_off = input("any more bidders yes or no: ")
    if bidding_off == "no" or bidding_off == "n":
        bidding_on = False
        h_bidder(store_data)
    elif bidding_off == "yes" or bidding_off == "y":
        os.system("clear")
