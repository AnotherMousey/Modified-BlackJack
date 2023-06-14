import random
number = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
type = ["spades", "hearts", "diamonds", "clubs"]
count = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck = []
pts = []
for i in number:
    for j in type:
        deck.append(i+" of "+j)
for i in count:
    for j in range(0, 4):
        pts.append(i)
dealer_card_count=0
player_card_count=0
dealer_deck=[]
player_deck=[]
dealer_state=-1
player_state=-1
total_player_point=0
total_dealer_point=0
player_ace_count=0
dealer_ace_count=0
current_turn="player"
stay_count=0
print("Game start!")

def player_turn():
    print("Would you like to Draw or Stay? (D/S): ", end='')
    report=input()
    if report=='S': 
        print("You chose stay.")
        stay_count+=1
        return
    else:
        print("You chose draw.")
        card=random.randint(0, len(deck)-1)
        player_deck.append(deck[card])
        deck.pop(card)
        if pts[card]==0:
            player_ace_count+=1
        else:
            total_player_point+=pts[card]
        pts.pop(card)
        msg="You draw "+deck[card]
        print(msg)

def dealer_turn():
    if total_dealer_point<17:
        print("The dealer chose draw")
        card=random.randint(0, len(deck)-1)
        dealer_deck.append(deck[card])
        deck.pop(card)
        if pts[card]==0:
            dealer_ace_count+=1
        else:
            total_dealer_point+=pts[card]
        pts.pop(card)
        msg="You draw "+deck[card]
        print(msg)
    else:
        print("The dealer chose stay")
        stay_count+=1
        return


def game_main():
    #begin initial phase
    card=random.randint(0, len(deck)-1)
    player_deck.append(deck[card])
    deck.pop(card)
    if pts[card]==0:
        player_ace_count+=1
    else:
        total_player_point+=pts[card]
    pts.pop(card)
    card=random.randint(0, len(deck)-1)
    dealer_deck.append(deck[card])
    deck.pop(card)
    if pts[card]==0:
        dealer_ace_count+=1
    else:
        total_dealer_point+=pts[card]
    pts.pop(card)
    card=random.randint(0, len(deck)-1)
    player_deck.append(deck[card])
    deck.pop(card)
    if pts[card]==0:
        player_ace_count+=1
    else:
        total_player_point+=pts[card]
    pts.pop(card)
    card=random.randint(0, len(deck)-1)
    dealer_deck.append(deck[card])
    deck.pop(card)
    if pts[card]==0:
        dealer_ace_count+=1
    else:
        total_dealer_point+=pts[card]
    pts.pop(card)
    #end initial phase

    #alert player about the initial deck
    init_deck_msg="Your first 2 cards are: "+player_deck[0]+" and "+player_deck[1]+"."
    print(init_deck_msg)
    print("Your current")

    #begin draw phase
    while not (player_state==0 and dealer_state==0):
        msg="It is "+current_turn+"'s turn."
        print(msg)
        if current_turn=="player":
            current_turn="dealer"
            player_turn()
        else:
            current_turn="player"
            dealer_turn()
            if stay_count==2: break
    #end draw phase

    #begin compare phase
    
    #end compare phase

game_main()