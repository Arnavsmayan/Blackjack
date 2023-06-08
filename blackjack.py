import random

cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
num=["2","3","4","5","6","7","8","9","10"]
suits=["Spades","Hearts","Diamonds","Clubs"]
deck=[]
for i in cards:
    for j in suits:
        deck.append(i+" of "+j)
playerHand=[]
dealerHand=[]

#Input will be playerHand or dealerHand
def dealHand(hand):
    card=random.choice(deck)
    hand.append(card)
    deck.remove(card)
    return hand
    #Output is in format "2 of spades"

#Again input will be playerHand or dealerHand
def total(hand):
    totalValue=0
    face=["J","Q","K"]
    playerHandValue=[unit[:2] for unit in hand]
    playerHandValue=[u.strip() for u in playerHandValue]
    for cardValue in playerHandValue:
        if cardValue in num:
            cardValue=int(cardValue)
            totalValue = totalValue + cardValue
        elif cardValue in face:
            totalValue = totalValue + 10
        else:
            if cardValue=="A" and totalValue > 10:
                totalValue = totalValue + 1
            elif cardValue == "A":
                totalValue = totalValue + 11
    return totalValue
              
#actual gameplay
for _ in range(2):
    dealHand(playerHand)
    dealHand(dealerHand)

print("Dealer's Hand:\n<Card Hidden>\n",dealerHand[1],"\n")
print("Player's Hand:\n",playerHand[0],"\n",playerHand[1])
print("The player total is :",total(playerHand))



    