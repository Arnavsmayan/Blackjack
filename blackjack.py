import random
import sys

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
#Dealing first round of cards
for _ in range(2):
    dealHand(playerHand)
    dealHand(dealerHand)


print("Dealer's Hand:\n<Card Hidden>\n",dealerHand[1],"\n")
print("Player's Hand:\n",playerHand[0],"\n",playerHand[1])
print("Player's total is:",total(playerHand))


#Next Round
while True:
    hitOrStand=input("Would you like to hit or stand? Please enter 'h' or 's': ").strip()
    hitOrStand=hitOrStand[:1]
    if hitOrStand != "h" and hitOrStand != "s":
        continue
    else:
        if hitOrStand == "h":
            dealHand(playerHand)
            print("Player drew",playerHand[2])
        if total(playerHand) > 21:
            print(f"Player's total is {total(playerHand)}. Player is bust. PLAYER LOSES!!")
            sys.exit()
        if total(playerHand) <= 21:
            print("Player's new total is:",total(playerHand))
        if hitOrStand == "s":
            while True:
                if total(dealerHand) < 16:   #Dealer's logic
                    dealHand(dealerHand)
                    print("Dealer drew <Card Hidden>")
                if total(dealerHand) > 21:
                    print(f"Dealer's total is {total(dealerHand)}. Dealer is bust. PLAYER WINS!!") #Can Add option to retry here
                    sys.exit()
                if total(dealerHand) >=16:
                    break  
            break 


if total(dealerHand) > total(playerHand):
    print(f"Dealer has {total(dealerHand)} and player has {total(playerHand)}. PLAYER LOSES!!")
if total(dealerHand) == total(playerHand):
    print(f"Dealer has {total(dealerHand)} and player has {total(playerHand)}. DRAW!!")
elif total(playerHand) > total(dealerHand):
    print(f"Dealer has {total(dealerHand)} and player has {total(playerHand)}. PLAYER WINS!!")







