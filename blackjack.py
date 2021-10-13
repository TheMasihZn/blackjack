import random

#  name, value, count in deck           4 sets of cards
cards = [(card, (i + 1) if i < 10 else 3) for i, card in enumerate(list("A123456789XJQK"))]
cards = cards + cards + cards + cards

sample_names = ["Jack", "Micheal", "Muhammad", "Adam", "Daniel", "George", "Alex", "Cristian"]


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.alive = True
        self.will_receive = True

    def die(self):
        self.alive = False
        self.will_receive = False


class Dealer(Player):
    def __init__(self):
        super().__init__("--Dealer--")


class BlackJack:
    players = [Dealer(), ]

    def __init__(self, n_players):
        self.winners = []
        n = min(n_players, len(sample_names))
        for i in range(n):
            name = f"{sample_names[i % len(sample_names)]}{(int(i / len(sample_names)))}"  # --> jake0
            self.players.append(Player(name))

    def give_cards(self):
        for player in [player for player in self.players if player.will_receive]:
            my_card = random.choice(cards)
            cards.remove(my_card)
            player.score += my_card[1]
            if my_card[0] == 'A':
                if player.score < 11:
                    player.score += 10
            if player.score > 21:
                player.die()

    def evaluate(self):
        dealer = self.players.pop(0)
        if not dealer.alive:
            self.winners = self.players
        else:
            for player in [player for player in self.players if player.alive]:
                if player.score >= dealer.score:
                    self.winners.append(player)

