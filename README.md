# 21
You will be playing with a dealer (AI) in a 21 game. The rules are simple: the closest one that has a score of less than or equal to 21 wins. The ace card can be 1, 10 or 11 points. Both you and the dealer will initially have 2 cards. The game is turn-based. The draw phase ends once both call stay.
## How the AI works
The dealer AI works as follow:
- Every turn, it will calculate the maximum number of cards that he can pick to guarantee a score that is lower than or equal to 21. This number will be calculate from the dealer's hand and his deduction on your hand. Lets call the number $k$.
- Then the dealer will randomize a number from 1 to the number of remaining cards and compare it to $k$. If $k$ is larger than or equal to the randomize number, the dealer will call a draw, else he will call a stay.
