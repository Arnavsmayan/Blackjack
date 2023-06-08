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

#Again input will be playerHand or dealerHand
def total(hand):
    totalValue=0
    face=["J","Q","K"]
    for cardValue in hand:
        if cardValue in range(1,11):
            totalValue = totalValue + cardValue
        elif cardValue in face:
            totalValue = totalValue + 10
        else:
            if totalValue > 10:
                totalValue = totalValue + 1
            else:
                totalValue = totalValue + 11
    return totalValue

dealHand(playerHand)
dealHand(playerHand)
print(total(playerHand))                


    