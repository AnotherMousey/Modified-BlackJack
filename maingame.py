import random
number = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
type = ["spades", "hearts", "diamonds", "clubs"]
deck = []
for i in number:
    for j in type:
        deck.append(i+" of "+j)
dealer_card_count=0
player_card_count=0
dealer_deck=[]
player_deck=[]
dealer_state=-1
player_state=-1
current_turn="player"

#def player_turn():

#def dealer_turn():

def game_main():
    #begin initial phase
    card=random.randint(0, len(deck)-1)
    player_deck.append(card)
    deck.pop(card)
    card=random.randint(0, len(deck)-1)
    dealer_deck.append(card)
    deck.pop(card)
    card=random.randint(0, len(deck)-1)
    player_deck.append(card)
    deck.pop(card)
    card=random.randint(0, len(deck)-1)
    dealer_deck.append(card)
    deck.pop(card)
    #end initial phase

    #begin draw phase
    while not (player_state==0 and dealer_state==0):
        return;
    #end draw phase

    #begin compare phase

    #end compare phase

game_main()