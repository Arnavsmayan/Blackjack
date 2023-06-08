import random

cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A","2","3","4","5","6","7","8","9","10","J","Q","K","A",]
suits=["Spades","Hearts","Diamonds","Clubs"]

playerHand=[]
dealerHand=[]

#Input will be playerHand or dealerHand
def dealHand(hand):
    card=random.choice(cards)
    hand.append(card)
    cards.remove(card)
    return hand

dealHand(playerHand)
print(playerHand[0])
    