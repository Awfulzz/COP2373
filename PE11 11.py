import random


class Card:
    '''Represents a single playing card.'''

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    '''Represents a standard deck of 52 playing cards.'''

    def __init__(self):
        ranks = [
            'Ace', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'Jack', 'Queen', 'King'
        ]
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        '''Shuffle the cards in the deck.'''
        random.shuffle(self.cards)

    def deal(self):
        '''Deal one card from the top of the deck.'''
        return self.cards.pop()


def display_hand(hand):
    '''Display the cards in the player\'s hand with positions.'''
    print('\nYour hand:')
    for index, card in enumerate(hand, start=1):
        print(f'{index}. {card}')


def get_replacement_choices():
    '''Prompt the user for card positions to replace and validate the input.'''
    while True:
        user_input = input(
            '\nEnter card numbers to replace (example: 1, 3, 5)\n'
            'Press Enter to keep all cards: '
        ).strip()

        if user_input == '':
            return []

        parts = [part.strip() for part in user_input.replace(' ', '').split(',') if part.strip() != '']

        try:
            choices = sorted(set(int(part) for part in parts))
        except ValueError:
            print('Invalid entry. Please enter only numbers from 1 to 5, separated by commas.')
            continue

        if all(1 <= choice <= 5 for choice in choices):
            return choices

        print('Invalid card number. Please choose numbers from 1 to 5.')


def replace_cards(hand, deck, choices):
    '''Replace the selected cards in the hand with new cards from the deck.'''
    for choice in choices:
        hand[choice - 1] = deck.deal()


def main():
    '''Run the poker draw program.'''
    deck = Deck()
    deck.shuffle()

    # Deal the initial five-card poker hand.
    hand = []
    for _ in range(5):
        hand.append(deck.deal())

    print('Poker Draw')
    print('----------')
    display_hand(hand)

    # Ask the user which cards should be replaced.
    choices = get_replacement_choices()

    # Replace any selected cards and show the final hand.
    replace_cards(hand, deck, choices)

    print('\nFinal hand:')
    for index, card in enumerate(hand, start=1):
        print(f'{index}. {card}')


if __name__ == '__main__':
    main()
