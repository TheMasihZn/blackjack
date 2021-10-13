from blackjack import BlackJack


while True:
    print('number of players: ')
    try:
        n = int(input())
    except ValueError:
        continue
    break

game = BlackJack(n)

print('players : ')
for player in game.players:
    print(f'{player.name}, ')
print("inputs : blank = true, anything = no")

while True:
    receiver_players = [player for player in game.players if player.will_receive]
    if len(receiver_players) < 2:
        break

    for player in receiver_players:
        print(f'will {player.name} continue? ')
        n = input()
        if n != '':
            player.will_receive = False

    game.give_cards()

    for player in game.players:
        print(f'\t\t{player.name} got total of {player.score}.\n')


game.evaluate()

print(f'Game finished:\n ')
if len(game.winners) == 0:
    print("\tthere were no winners.")
elif len(game.winners) == len(game.players):
    print("\teveryone won!!!!")
else:
    print('list of winners : \n')
    for player in game.winners:
        print(f'{player.name}, ')

