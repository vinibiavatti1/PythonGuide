"""
Truc game

* Truc is a game for four players in fixed partnerships; it can also be played
  by two, but the two player game is considerably less interesting. As usual
  you sit opposite your partner. It's played anticlockwise to a final score of
  twelve points and each hand is worth from 1 to 3 points, depending on the
  bets
"""
from random import shuffle, choice, randrange
from functools import reduce


###############################################################################
# Constants
###############################################################################


# General
TESTS = False
CARDS = '4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3'
SUITS = 'Coins', 'Swords', 'Cups', 'Clubs'
JOKER_VALUE = 100

# Card Compare
COMPARE_CARD_EQUAL = 0
COMPARE_CARD_1_BETTER = 1
COMPARE_CARD_2_BETTER = 2

# Turn state
TURN_STATE_PLAYER_DECLINED = 1
TURN_STATE_PLAYER_TRUC = 2
TURN_STATE_PLAYER_PLAY = 3
TURN_STATE_PLAYER_ACCEPTED = 4
TURN_STATE_COMPUTER_DECLINED = 4
TURN_STATE_COMPUTER_TRUC = 5
TURN_STATE_COMPUTER_PLAY = 6
TURN_STATE_COMPUTER_ACCEPTED = 7

# Player turn
TURN_PLAYER = 1
TURN_COMPUTER = 2

# Interaction commands
COMMANDS = '0', '1', '2', 'T', 'D'

# Turns
FIRST_TURN = 1
SECOND_TURN = 2
THIRD_TURN = 3


###############################################################################
# Classes
###############################################################################


# Excpetion
class TrucError(Exception):
    pass


class Card:
    def __init__(self, sign, suit):
        self.sign = sign
        self.suit = suit

    def get_value(self, joker):
        if self.sign == joker:
            return JOKER_VALUE
        for i, c in enumerate(CARDS):
            if self.sign == c:
                return i + 1
        return None

    def get_suit_value(self):
        for i, s in enumerate(SUITS):
            if self.suit == s:
                return i + 1
        return None


class TrucUtils:
    @staticmethod
    def generate_deck():
        cards = []
        for c in CARDS:
            for s in SUITS:
                cards.append(Card(c, s))
        return cards

    @staticmethod
    def get_next_sign(sign):
        cards = list(CARDS)
        index = cards.index(sign)
        if index == len(cards) - 1:
            return cards[0]
        else:
            return cards[index + 1]


class Truc:
    def __init__(self):
        self.deck = None
        self.joker = None
        self.player_turn = None
        self.turn = None
        self.current_game_score = None
        self.truc = None
        self.game_score = None
        self.turn_ended = None

    def init_game(self, player, computer):
        # Create deck
        self.deck = TrucUtils.generate_deck()

        # Shuffle deck
        shuffle(self.deck)

        # Define joker
        pop = self.deck.pop()
        self.joker = TrucUtils.get_next_sign(pop.sign)

        # Give cards to players
        self._give_cards_to_player(player)
        self._give_cards_to_player(computer)

        # Other initial data
        self.current_game_score = 1
        self.turn = FIRST_TURN
        self.turn_count = 0
        self.truc = False
        self.turn_ended = False

    def compare_cards(self, card1, card2):
        l1 = card1.get_value(self.joker)
        l2 = card2.get_value(self.joker)
        result = l1 - l2
        if result < 0:
            return COMPARE_CARD_2_BETTER
        elif result > 0:
            return COMPARE_CARD_1_BETTER
        else:
            return COMPARE_CARD_EQUAL

    def swap_player_turn(self):
        if self.player_turn == TURN_COMPUTER:
            self.player_turn = TURN_PLAYER
        else:
            self.player_turn = TURN_COMPUTER

    def next_turn(self, next_player):
        self.turn += 1
        self.player_turn = next_player

    def end_turn(self, win_player):
        win_player.score += self.current_game_score

    def _give_cards_to_player(self, player):
        c1 = self.deck.pop()
        c2 = self.deck.pop()
        c3 = self.deck.pop()
        player.cards = [c1, c2, c3]


# Player
class Player:
    def __init__(self):
        self.cards = []
        self.score = 0
        self.turn_score = 0

    def is_turn_winner(self):
        return self.turn_score >= 2

    def get_cards_score(self, joker):
        return reduce(lambda a, c: c.get_value(joker), self.cards)


# Computer Player
class Computer(Player):
    def accept_truc(self, turn, joker):
        score = self.get_cards_score(joker)
        if score > JOKER_VALUE + (3 * (turn - 1)):
            return True
        return False

    def choose_card(self, joker, player_card=None):
        if not player_card:
            card = self.cards[randrange(0, len(self.cards))]
            self.cards.remove(card)
            return card
        else:
            strong = None
            week = None
            for c in self.cards:
                if not strong or c.get_value(joker) > strong.get_value(joker):
                    strong = c
                if not week or c.get_value(joker) < week.get_value(joker):
                    week = c
            if strong.get_value(joker) > player_card.get_value(joker):
                return strong
            else:
                return week


###############################################################################
# User interaction
###############################################################################


class Interaction:
    @staticmethod
    def welcome():
        print('Welcome to Truc!')
        print('By Vini (PythonGuide)')
        print()
        print('*** Press enter to start! ***')
        input()

    @staticmethod
    def input_command(player, game):
        ok = False
        valid_card_indexes = []
        while not ok:
            ok = True
            print(f'JOKER: {game.joker}')
            print('Choose a card or other command:')
            for i, c in enumerate(player.cards):
                print(f'{i} -  {c.sign} / {c.suit}')
                valid_card_indexes.append(str(i))
            if not game.truc:
                print('T - Truc!')
            print('D - Decline')
            cmd = input()
            if (cmd not in COMMANDS or
                    cmd not in valid_card_indexes or
                    (cmd == 'T' and game.truc)):
                print('Invalid command')
                ok = False
        return cmd

    @staticmethod
    def process_command(cmd, game, player, computer):
        if cmd == 'D':
            print('Player declined :(')
            game.end_turn(computer)
            return TURN_STATE_PLAYER_DECLINED, None
        elif cmd.isdigit():
            index = int(cmd)
            print('Player played:')
            card = player.cards[index]
            player.cards.remove(card)
            print(f'{card.sign} / {card.suit}')
            return TURN_STATE_PLAYER_PLAY, card
        elif cmd == 'T':
            player('Player ask Truc!!!')
            if computer.accept_truc(game.turn, game.joker):
                print('Computer accepted!')
                game.truc = True
                return TURN_STATE_COMPUTER_ACCEPTED, None
            print('Computer declined...')
            game.end_turn(player)
            return TURN_STATE_COMPUTER_DECLINED, None
        else:
            raise TrucError('Invalid input command')

    @staticmethod
    def show_pontuation(player, computer):
        msg = f'Player {player.turn_score} x {computer.turn_score} Computer'
        print(msg)

    @staticmethod
    def process_play(game, player, computer, player_card, computer_card):
        compare = game.compare_cards(player_card, computer_card)
        if compare == COMPARE_CARD_1_BETTER:
            print('Player 1 hit!')
            player.turn_score += 1
            Interaction.show_pontuation(player, computer)
            game.next_turn(TURN_PLAYER)
            pass
        elif compare == COMPARE_CARD_2_BETTER:
            print('Computer hit!')
            computer.turn_score += 1
            Interaction.show_pontuation(player, computer)
            game.next_turn(TURN_COMPUTER)
            pass
        else:
            return

    @staticmethod
    def process_player_turn(game, player, computer):
        cmd = Interaction.input_command(player, game)
        turn_state, card = Interaction.process_command(
            cmd,
            game,
            player,
            computer
        )
        return turn_state, card

    @staticmethod
    def process_computer_turn(game, player_card, computer):
        computer_card = computer.choose_card(game.joker, player_card)
        print('Computer player:')
        print(f'{computer_card.sign} / {computer_card.suit}')
        return computer_card


# Main
def main():
    Interaction.welcome()

    game = Truc()
    player = Player()
    computer = Computer()

    while True:
        game.init_game(player, computer)

        player_card = None
        computer_card = None
        while True:
            # Process computer turn
            if game.player_turn == TURN_COMPUTER and not computer_card:
                computer_card = Interaction.process_computer_turn(
                    game,
                    player_card,
                    Computer
                )

            # Process player turn
            turn_state, card = Interaction.process_player_turn(
                game,
                player,
                computer
            )
            if turn_state == TURN_STATE_PLAYER_DECLINED:
                break
            elif turn_state == TURN_STATE_COMPUTER_DECLINED:
                break
            elif turn_state == TURN_STATE_COMPUTER_ACCEPTED:
                continue
            elif turn_state == TURN_STATE_PLAYER_PLAY:
                player_card = card

            # Process computer turn
            if not computer_card:
                computer_card = Interaction.process_computer_turn(
                    game,
                    player_card,
                    computer
                )

            Interaction.process_play(
                game,
                player,
                computer,
                player_card,
                computer_card
            )

        if game.turn_ended:
            print('Turn finished!')
            continue


# Init
if __name__ == '__main__':
    main()
