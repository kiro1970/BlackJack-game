import random
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["H", "D", "S", "C"]
        for suit in suits:
            for v in range(1, 14):
                self.cards.append((v, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
    
class Blackjack:

    def start_game(self):
        self.player = []
        self.dealer = []
        self.deck = Deck()
        self.deck.shuffle()
        for x in range(2): 
            self.player.append(self.deck.deal())
            self.dealer.append(self.deck.deal())

        if self.sum(self.player) == 21:
            print("BLACKJACK!")
            exit()

        if self.is_busted(self.dealer):
            print('DEALER BUSTED!')
            exit()

        standing = False
        while not standing:
            self.show(standing)
            if self.is_busted(self.player):
                print('BUST!')
                exit()
            s = input("Would you like to (s)tand or (h)it? ")
            if s == "s":
                standing = True
            elif s == "h":
                self.player.append(self.deck.deal())

        self.show(standing)
        p = self.sum(self.player)
        d = self.sum(self.dealer)
        if p > d:
            print('You win!')
        elif d > p:
            print('you lose!')
        else:
            print('Tie!')

    def is_busted(self, hand):
        return self.sum(hand) > 21

    def sum(self, hand):
        return sum(i[0] for i in hand)

    def show(self, is_standing):
        if is_standing:
            print(f"Dealer's hand: {self.dealer}")
            print(f"Your hand: {self.player}")
        else:
            print(f"Dealer's hand: {self.dealer[0]} ( , )")
            print(f"Your hand: {self.player}")
        

b = Blackjack()
b.start_game()