import random

def Entrance(bal,bet):
    Entrance = input("Welcome to Blackjack, press ENTER to continue and type E to leave:\n")
    if Entrance == "E":
        exit()
    else:
        Menu(bal,bet)

def Menu(bal,bet):
    menuSelect = "0"
    while menuSelect != 1 and menuSelect != 2:
        print("\n1. Tutorial")
        print("2. Player vs House")
        
        menuSelect = input("Please enter the corresponding number:\n")
        if menuSelect == "1":
            Tutorial()
        elif menuSelect == "2":
            Player(bal,bet)
            
def Tutorial():
    cont = ""
    input("Press ENTER to continue")
    input("\nThe goal of the game is to make your cards add up to 21. The winner of the round is whoever is closer. However if you are over, you are automatically out and the house wins.")

    input("\nYou will first get two cards and then based on how close you are, you may chose to pick another card, by hitting, or stay with the card you have.")

    input("\nAll cards are equal to their numbers and the face cards are all equal to 10. The ace may act as a 1 or 11, depending on what you need.")

    input("\nWhen you finish with your hand, the house will go. However they are forced to hit if they are below 17 and stay if they are 17 or above. Knowing this can help you as a player make strategies to succeed.")
    
    input("\nThis game is commonly found in casinos and is known to be the most fair game there. When facing the house all the bets made will be blind, or made before the round starts. Each player gets paid the amount they risk, if they win, and pays the house the amount they risked, if they lose.")
    
    while cont != "c":
        cont = input("\nReady to begin? Please enter c to continue back to the menu:\n")
        if cont == "c":
            Menu(bal,bet)
     
def Player(bal,bet):

    for i in range(0,1):
        bet = int(input("\nYour current balance is $" + str(bal) + ". How much would you like to bet?\n"))
        while bet > bal or bet < 0:
            bet = int(input("\nYour current balance is $" + str(bal) + ". How much would you like to bet?\n"))

        print("\nPlayer" + str(i + 1)  + ":")

        val[x] = random.choice(deck)
        deck.remove(val[x])
        print(str(val[x]))

        val[x] = cardConvert(val[x])      

        sum[x] += int(val[x])
            
        val[x] = random.choice(deck)
        deck.remove(val[x])
        print(str(val[x]))

        val[x] = cardConvert(val[x])
        
        sum[x] += int(val[x])

        while sum[x] < 22:
            hit = input("Please enter hit if you would like another card:\n")
            if hit == "hit":
                
                val[x] = random.choice(deck)
                deck.remove(val[x])
                print(val[x])
                
                val[x] = cardConvert(val[x])
                sum[x] += int(val[x])
            else:
                break
        if sum[x] > 21:
            resultScreen(0,sum[x],bal,bet)
        print("Player 1's sum is: " + str(sum[x]))
    house(bal,bet)

def cardConvert(card):
    if card[0] == "K" or card[0] == "Q" or card[0] == "J" or card[0] == "1":
        return 10

    elif card[0] == "A":
        ace = input("Type 1, if you would like to change the ace from 11 to 1:\n")

        if ace == "1":
            return 1
        else:
            return 11
    else:
        return int(card[0])

def house(bal,bet):
    house = ""
    houseSum = 0
    print("\nHouse:")

    house = random.choice(deck)
    deck.remove(house)
    print(str(house))
    house = cardConvertH(house,houseSum)      

    houseSum += int(house)

    house = random.choice(deck)
    deck.remove(house)
    print(str(house))
    house = cardConvertH(house,houseSum)
        
    houseSum += int(house)

    while houseSum < 22:
        if houseSum < 17:    
            house = random.choice(deck)
            deck.remove(house)
            print(house)
                
            house = cardConvertH(house,houseSum)
            houseSum += int(house)
        else:
            break
    print("The house's sum is: " + str(houseSum))

    resultScreen(houseSum,sum[x],bal,bet)

def cardConvertH(cardH,cardS):
    if cardH[0] == "K" or cardH[0] == "Q" or cardH[0] == "J" or cardH[0] == "1":
        return 10

    elif cardH[0] == "A":

        if cardS == 0 or cardS == 10 or cardS == 9 or cardS == 8 or cardS == 7:
            return 11
        else:
            return 1
    else:
        return int(cardH[0])

def resultScreen(houseSum,playerSum,bal,bet):
    result = ""
    if playerSum > 21:
        bal = bal - bet
        print("\nUnfortunately you lost, your current balance is $" + str(bal) + ". Press r for another chance, e to give up and m for the menu")
    elif houseSum > 21:
        bal = bal + bet
        print("\nYou Won, your current balance is $" + str(bal) + ". Press r to try and keep your win streak, e to give up and m for the menu")
    elif houseSum == playerSum:
        print("\nDraw, your balance stayed at $" + str(bal) + ". Press r to settle it, e to give up and m for the menu")
    elif houseSum > playerSum:
        bal = bal - bet
        print ("\nUnfortunately you lost, your current balance is $" + str(bal) + ". Press r for another chance, e to give up and m for the menu")
    else:
        bal = bal + bet
        print("\nYou Won, your current balance is $" + str(bal) + ". Press r to try and keep your win streak, e to give up and m for the menu")

    while result != "e" and result != "r" and result != "m":
        if bal < 1:
            repay = input("You are out of money, press r to put in another $100000 in.\n")
            if repay == "r":
                bal = int(100000)
            else:
                quit()
        if bal > 999999:
            input("You have beat the casino, the house is now bankrupt...")
            quit()
            
        result = input("What would you like to do?\n")
    if result == "e":
        exit()
    elif result == "r":
        val[x] = 0
        sum[x] = 0
        house = 0
        houseSum = 0
        deck = ["A♠","A♥","A♣","A♦","2♠","2♥","2♣","2♦","3♠","3♥","3♣","3♦","4♠","4♥","4♣","4♦","5♠","5♥","5♣","5♦","6♠","6♥","6♣","6♦","7♠","7♥","7♣","7♦","8♠","8♥","8♣","8♦","9♠","9♥","9♣","9♦","10♠","10♥","10♣","10♦","J♠","J♥","J♣","J♦","Q♠","Q♥","Q♣","Q♦","K♠","K♥","K♣","K♦"]
        Player(bal,bet)
    elif result == "m":
        val[x] = 0
        sum[x] = 0
        house = 0
        houseSum = 0
        deck = ["A♠","A♥","A♣","A♦","2♠","2♥","2♣","2♦","3♠","3♥","3♣","3♦","4♠","4♥","4♣","4♦","5♠","5♥","5♣","5♦","6♠","6♥","6♣","6♦","7♠","7♥","7♣","7♦","8♠","8♥","8♣","8♦","9♠","9♥","9♣","9♦","10♠","10♥","10♣","10♦","J♠","J♥","J♣","J♦","Q♠","Q♥","Q♣","Q♦","K♠","K♥","K♣","K♦"]
        Menu(bal,bet)
        
        
#Main
x = int(0)
sum = [0,0,0,0]
val = [0,0,0,0]
deck = ["A♠","A♥","A♣","A♦","2♠","2♥","2♣","2♦","3♠","3♥","3♣","3♦","4♠","4♥","4♣","4♦","5♠","5♥","5♣","5♦","6♠","6♥","6♣","6♦","7♠","7♥","7♣","7♦","8♠","8♥","8♣","8♦","9♠","9♥","9♣","9♦","10♠","10♥","10♣","10♦","J♠","J♥","J♣","J♦","Q♠","Q♥","Q♣","Q♦","K♠","K♥","K♣","K♦"]
bal = int(100000)
bet = int(0)
Entrance(bal,bet)




