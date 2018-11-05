import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Please enter your bet: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            if chips.bet > chips.total:
                print(f"You don't have enough chips! Current chips: {chips.total}")
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        hit_or_stand = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")

        if hit_or_stand[0].lower() == 'h':
            print("\n----- Player hits. Showing hands. -----")
            hit(deck,hand)

        elif hit_or_stand[0].lower() == 's':
            print("\n----- Player stands. Dealer is playing. -----")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    
    # print(f"Player's hand: {player.cards}, total value: {player.value}")
    # print(f"Dealer's hand: {dealer.cards[1:]}, total value: {dealer.value}")##
    
    print("\n----- Dealer's Hand -----\n")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\n----- Player's Hand -----\n", *player.cards, sep='\n ')
    print("Player's Hand Value =",player.value)
    
def show_all(player,dealer):
    
    # print(f"Player's hand: {player.cards}, total value: {player.value}")
    # print(f"Dealer's hand: {dealer.cards}, total value: {dealer.value}")
    
    print("\n----- Showing all hands -----")
    print("\n----- Dealer's Hand -----\n", *dealer.cards, sep='\n ')
    print("Dealer's Hand Value",dealer.value)
    print("\n----- Player's Hand -----\n", *player.cards, sep='\n ')
    print("Player's Hand Value =",player.value)

def player_busts(player,dealer,chips):
    
    print("\n----- Player busted! -----")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    
    print("\n----- Player wins! -----")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    
    print("\n----- Dealer busted! -----")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    
    print("\n----- Dealer wins! -----")
    chips.lose_bet()
    
def push(player,dealer):

    print("\n----- It's a draw! -----")

while True:
    # Print an opening statement
    print("\nHi, welcome to the Python Blackjack Game! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.\n")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    player = Hand()
    dealer = Hand()
    
    deck.shuffle()
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    
    # Set up the Player's chips
    player_chip = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chip)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,dealer,player_chip)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        
        while dealer.value < 17:
            hit(deck, dealer)
        
        # Show all cards
        show_all(player,dealer)
        
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player,dealer,player_chip)
        
        elif dealer.value > player.value:
            dealer_wins(player,dealer,player_chip)
        
        elif dealer.value < player.value:
            player_wins(player,dealer,player_chip)
        
        else:
            push(player,dealer)
    
    # Inform Player of their chips total 
    print(f"\nPlayer's chips in total: {player_chip.total}")
    
    # Ask to play again
    while True:
        play_again = input("\nWould you like to play again? Enter y or n: ")

        if play_again[0].lower() == 'y':
            
            playing = True
            break

        elif play_again[0].lower() == 'n':
            
            playing = False
            print("\nThanks for playing!")
            break
            
        else:
            print("\nPlease eneter a valid input.")
    
    if playing == False:
        break