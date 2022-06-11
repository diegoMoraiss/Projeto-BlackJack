# definicoes iniciais

import random

playing = False
chip_pool = 100

bet = 1

restart_phrase = "Press 'd' to play again or press 'q' to leave"

# definindo as cartas

suits = ('H', 'D', 'C', 'S')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K')
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'J':10, 'Q':10, 'K':10}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self): 
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print(self.suit + self.rank)

#definindo a mao dos jogadores

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ""

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return "The hand has {}".format(hand_comp)

    def card_add(self, card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True

        self.value += card_val[card.rank]

    def calc_val(self):                              
        if (self.ace == True and self.value < 12):                   #define quando o 'as' eh 10
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):                                          #serve para mostrar ou nao uma carta (util para o dealer)
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()                           

#definindo o baralho

class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):                       #embaralha o baralho de forma aleatoria (random)
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += " " + card.__str__()

        return "The deck has " + deck_comp


#definindo como ocorrerao as apostas

def make_bet():
    global bet
    bet = 0

    print("What amount of chips you like to bet?")

    while bet == 0:
        bet_comp = input()
        bet_comp = int(bet_comp)

        if bet_comp >=1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print("Invalid bet.")

#distribuindo as cartas entre dealer e player e iniciando a jogada:

def deal_cards():
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()                  #definindo a mao do player
    dealer_hand = Hand()                  #definindo a mao do dealer

    #entregando as cartas(2 para cada)

    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Hit or Stand? Press 'h' to hit or 's' to stand."

    playing = True
    game_step()       #funcao que ainda sera definida

def hit():            # esta funcao detalha a jogada hit, ou seja, quando o jogador pede mais uma carta
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())
        print("Player hand is %s" %player_hand)

        if player_hand.calc_val() >= 21:
            result = "Busted!" + restart_phrase
            chip_pool -= bet
            playing = False

    else:
        result = "Sorry, you can't hit. " + restart_phrase

    game_step()      #funcao que ainda sera definida

def stand():
    global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

    if playing == False:
        if player_hand.calc_val() > 0:
            result = "Sorry, you can't stand!"

    else:
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        if dealer_hand.calc_val() > 21:
            result = "Dealer busts! You win! " + restart_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = "You bet the dealer! You win! " + restart_phrase
            chip_pool += bet
            playing = False

        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = "Tied up! " + restart_phrase
            playing = False

        else:
            result = 'Dealer wins! ' + restart_phrase
            chip_pool -= bet
            playing = False
    
    game_step()        #funcao que sera definida futuramente

def game_step():       #roda o jogo de verdade
    print("")
    print("Player hand is: ")
    player_hand.draw(hidden=False)
    print("Player hand total hand is: " + str(player_hand.calc_val()))

    print("")
    print("Dealer hand is: ")
    player_hand.draw(hidden=True)
    print("Dealer hand total hand is: " + str(dealer_hand.calc_val()))

    if playing == False:
        print("Chip total: "+str(chip_pool))

    print(result)

    player_input()           #ainda definiremos

def game_exit():
    print("Thanks for playing!")
    exit()

def player_input():              #define a entrada do jogador
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print("Invalid input...  enter with 'h', 's', 'd', 'q': ")
        player_input()

def intro():
    print("Welcome to BlackJack!")

#Agora, basta rodar as funcoes e rodar o jogo

deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand()

intro()

deal_cards()




  



    


    









