print("Welcome to Blackmarket auctioning app")
question1 = input("would you like to bid for a car today?, yes or no").title()

bidder_data = {}

start_auction = False


def highest_bidder(bidder_dic):
    highest_price = 0
    for values in bidder_dic:
        amount = bidder_dic[values]
        if amount > highest_price:
            name = values
            highest_price = amount
    print(f"the highest amount is {highest_price} by {values}")


if question1 == "Yes":

    start_auction = True
    while start_auction:

        name = input("what is your name?")
        price = int(input("how much are you bidding for?"))
        bidder_data[name] = price
        new_bidder = input(f"is there another person who wants to bid, apart from {name}").title()

        if new_bidder == "Yes":
            pass
        elif new_bidder == "No":
            print("thank you, have a great day")

        else:
            highest_bidder(bidder_data)
            start_auction = False


elif question1 == "No":
    print("Thank you, Goodbye")

else:
    print("invalid response")



