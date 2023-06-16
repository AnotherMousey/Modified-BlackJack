import random
number = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
type = ["spades", "hearts", "diamonds", "clubs"]
deck = []
pts = []
hash = {}
for i in number:
    for j in type:
        hash[i+" of "+j]=len(deck)//4+1
        if hash[i+" of "+j]>10:
            hash[i+" of "+j]=10
        if hash[i+" of "+j]==1:
            hash[i+" of "+j]=0
        deck.append(i+" of "+j)
random.shuffle(deck)
for i in deck:
    pts.append(hash[i])
dealer_deck=[]
player_deck=[]
total_player_point=0
total_dealer_point=0
total_best_player_point=0
total_best_dealer_point=0
player_ace_count=0
dealer_ace_count=0
current_turn="player"
stay_count=0
print("Game start!")
print()

def player_turn():
    global player_ace_count
    global total_player_point
    print("Would you like to Draw or Stay? (D/S): ", end='')
    report=input()
    if report=='S': 
        print("You chose to stay.")
        global stay_count
        stay_count+=1
        return
    else:
        print("You chose to draw.")
        card=random.randint(0, len(deck)-1)
        player_deck.append(deck[card])
        msg="You draw "+deck[card]
        deck.pop(card)
        if pts[card]==0:
            player_ace_count+=1
        else:
            total_player_point+=pts[card]
        pts.pop(card)
        print(msg)
        msg="Your current deck is: "
        for crd in player_deck:
            if crd==deck[card]:
                msg=msg+crd+"."
            else:
                msg=msg+crd+", "
        print(msg)
        player_best_score()
        msg="Your current score is "+str(total_best_player_point)
        print(msg)

def dealer_turn():
    global total_best_dealer_point
    global total_dealer_point
    global dealer_ace_count
    #this is for the AI
    dealer_best_score()
    if total_best_dealer_point<17:
        print("The dealer chose to draw")
        card=random.randint(0, len(deck)-1)
        dealer_deck.append(deck[card])
        deck.pop(card)
        if pts[card]==0:
            dealer_ace_count+=1
        else:
            total_dealer_point+=pts[card]
        pts.pop(card)
    elif total_best_dealer_point>=19:
        print("The dealer chose to stay")
        global stay_count
        stay_count+=1
        return
    else:
        seed=17030
        probability=seed*(total_best_dealer_point**random.randint(1, 5))%len(deck)
        if probability==0: probability=len(deck)
        if probability<=(21-total_best_dealer_point)*4:
            print("The dealer chose to draw")
            card=random.randint(0, len(deck)-1)
            dealer_deck.append(deck[card])
            deck.pop(card)
            if pts[card]==0:
                dealer_ace_count+=1
            else:
                total_dealer_point+=pts[card]
            pts.pop(card)
        else:
            print("The dealer chose to stay")
            global stay_count
            stay_count+=1
            return

def dealer_best_score():
    global dealer_ace_count
    global total_dealer_point
    global total_best_dealer_point
    total_best_dealer_point=total_dealer_point
    total_best_dealer_point+=dealer_ace_count
    if dealer_ace_count>0:
        if dealer_ace_count>1 and total_best_dealer_point+19<=21:
            total_best_dealer_point+=19
        elif dealer_ace_count>1 and total_best_dealer_point+18<=21:
            total_best_dealer_point+=18
        else:
            if total_best_dealer_point+10<=21:
                total_best_dealer_point+=10
            elif total_best_dealer_point+9<=21:
                total_best_dealer_point+=9

def player_best_score():
    global total_player_point
    global player_ace_count
    global total_best_player_point
    total_best_player_point=total_player_point
    total_best_player_point+=player_ace_count
    if player_ace_count>0:
        if player_ace_count>1 and total_best_player_point+19<=21:
            total_best_player_point+=19
        elif player_ace_count>1 and total_best_player_point+18<=21:
            total_best_player_point+=18
        else:
            if total_best_player_point+10<=21:
                total_best_player_point+=10
            elif total_best_player_point+9<=21:
                total_best_player_point+=9

def reveal_result():
    msg="Your hand has "+str(len(player_deck))+" cards, with a total of "+str(total_best_player_point)+ " points."
    print(msg)
    msg="Dealer's hand has "+str(len(dealer_deck))+" cards, with a total of "+str(total_best_dealer_point)+ " points."
    print(msg)
    print("The result is: ", end='')
    if total_best_dealer_point>21 and total_best_player_point>21:
        print("Draw!")
    elif total_best_dealer_point>21:
        print("You win!")
    elif total_best_player_point>21:
        print("Dealer wins!")
    elif len(dealer_deck)==5 and len(player_deck)==5:
        print("Draw!")
    elif len(dealer_deck)==5:
        print("Dealer wins!")
    elif len(player_deck)==5:
        print("You win!")
    elif total_best_dealer_point==total_best_player_point:
        if len(player_deck)==len(dealer_deck):
            print("Draw!")
        elif len(player_deck)>len(dealer_deck):
            print("You win!")
        else:
            print("Dealer wins!")    
    elif total_best_dealer_point>total_best_player_point:
        print("Dealer wins!")
    else:
        print("You win!")

def game_main():
    global player_ace_count
    global total_dealer_point
    global total_player_point
    global dealer_ace_count
    global current_turn
    global stay_count
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
    player_best_score()
    msg="Your current score is "+str(total_best_player_point)
    print(msg)
    print()

    #begin draw phase
    while stay_count<2 and len(player_deck)<=5 and len(dealer_deck)<=5:
        msg="It is "+current_turn+"'s turn."
        print(msg)
        if current_turn=="player":
            stay_count=0
            current_turn="dealer"
            player_turn()
        else:
            current_turn="player"
            dealer_turn()
        print()
    #end draw phase

    #begin compare phase
    dealer_best_score()
    player_best_score()
    reveal_result()
    #end compare phase

game_main()