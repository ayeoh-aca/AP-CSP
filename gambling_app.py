import random
deck = []
hand = []
rank = range(2,15)
suit = ["S", "C", "D", "H"]
option = ""
for i in rank:
    for j in suit:
        deck.append(f"{i}-{j}")
def deal():
    hand = []
    hand.append(random.sample(deck, 5))
    print(hand)
while option != "stay": 
    option = input("Would you like to Hit or Stay: ")
    if option != "stay":
        deal()
