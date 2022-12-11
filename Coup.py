# Import necessary modules
import sys
import random

# Prompt user for number of players
num_players = int(input('Enter number of players:'))

# Set up players and their initial coins
players = []
for i in range(num_players):
    # Prompt user for player's name
    player_name = input('Enter player ' + str(i+1) + "'s name:")
    players.append({'name': player_name, 'coins': 2})

# Set up deck of cards
deck = ['Duke', 'Contessa', 'Ambassador', 'Captain', 'Assassin']
random.shuffle(deck)

# Deal cards to players
for player in players:
    # Check if deck is empty
    if len(deck) == 0:
        print('Error: not enough cards in deck to deal to all players!')
        break

    player['cards'] = [deck.pop(), deck.pop()]

# Game loop
while True:
    # Loop through players
    for player in players:
        # Check if player has any coins
        if player['coins'] > 0:
            # Prompt player to take an action
            action = input(player['name'] + ', choose an action:')

            # Process player's action
            if action == 'Coup':
                # Prompt player to choose a target
                target = input(player['name'] + ', choose a target:')

                # Check if target has enough coins
                target_player = None
                for p in players:
                    if p['name'] == target:
                        target_player = p
                        break

                if target_player['coins'] >= 7:
                    # Coup target player and end game
                    target_player['coins'] -= 7
                    print(target_player['name'] + ' has been couped!')
                    print('Game over!')
                    sys.exit()
                else:
                    print('Cannot coup ' + target_player['name'] + '!')
            elif action == 'Income':
                # Give player 1 coin
                player['coins'] += 1
            elif action == 'Foreign Aid':
                # Give player 2 coins
                player['coins'] += 2
            else:
                # Invalid action
                print('Invalid action!')
        else:
            # Player has no coins and is eliminated
            print(player['name'] + ' has been eliminated!')
            players.remove(player)

        # Check if only one player remains
        if len(players) == 1:
            print(players[0]['name'] + ' wins!')
            break
