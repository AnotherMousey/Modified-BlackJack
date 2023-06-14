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
dealer_deck=[]
player_deck=[]
total_player_point=0
total_dealer_point=0
player_ace_count=0
dealer_ace_count=0
current_turn="player"
stay_count=0
print("Game start!")

def player_turn():
    global player_ace_count
    global total_player_point
    print("Would you like to Draw or Stay? (D/S): ", end='')
    report=input()
    if report=='S': 
        print("You chose stay.")
        global stay_count
        stay_count=1
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
        msg="Your current deck is: "
        for crd in player_deck:
            if crd==deck[card]:
                msg=msg+crd+"."
            else:
                msg=msg+crd+", "
        print(msg)

def dealer_turn():
    global total_dealer_point
    global dealer_ace_count
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
    else:
        print("The dealer chose stay")
        global stay_count
        stay_count+=1
        return

def dealer_best_score():
    global dealer_ace_count
    global total_dealer_point
    total_dealer_point+=dealer_ace_count
    if dealer_ace_count>0:
        if dealer_ace_count>1 and total_dealer_point+19<=21:
            total_dealer_point+=19
        elif dealer_ace_count>1 and total_dealer_point+18<=21:
            total_dealer_point+=18
        else:
            if total_dealer_point+10<=21:
                total_dealer_point+=10
            elif total_dealer_point+9<=21:
                total_dealer_point+=9

def player_best_score():
    global total_player_point
    global player_ace_count
    total_player_point+=player_ace_count
    if player_ace_count>0:
        if player_ace_count>1 and total_player_point+19<=21:
            total_player_point+=19
        elif player_ace_count>1 and total_player_point+18<=21:
            total_player_point+=18
        else:
            if total_player_point+10<=21:
                total_player_point+=10
            elif total_player_point+9<=21:
                total_player_point+=9

def reveal_result():
    msg="Your point is: "+str(total_player_point)
    print(msg)
    msg="Dealer's point is: "+str(total_dealer_point)
    print(msg)
    print("The result is: ", end='')
    if total_dealer_point>21 and total_player_point>21:
        print("Draw!")
    elif total_dealer_point==total_player_point:
        print("Draw!")
    elif total_dealer_point>21:
        print("You win!")
    elif total_player_point>21:
        print("Dealer wins!")
    elif total_dealer_point>total_player_point:
        print("Dealer wins!")
    else:
        print("You win!")

def game_main():
    global player_ace_count
    global total_dealer_point
    global total_player_point
    global dealer_ace_count
    global current_turn
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
    while stay_count<=2:
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
    dealer_best_score()
    player_best_score()
    reveal_result()
    #end compare phase

game_main()