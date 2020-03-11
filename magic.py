import sys
import random
import urllib.request
import json 


# TODO: - Get rid of 'NONE' at the start of every card print.
#       - Figure out correct algorithm to use to predict correct mana base.

#Magic Card object.
class Card:

    #creates the card
    def __init__(self, name, type_line, cmc, mana_cost,
                color, effect):
        self.name = name
        self.type_line = type_line
        self.cmc = cmc
        self.mana_cost = mana_cost
        self.color = color
        self.effect = effect
        #self.power = None
        #self.toughness = None
    
    # repr function to return the class in string format.
    def __repr__(self):
        return str(self.name)

    # Get function to return the card type.
    def card_type(self):
        return str(self.type_line)

    # Get function to return the color of the card.
    def ret_color(self):
        return str(self.color)

    # Get function to return the converted mana cost of the card.
    def ret_cmc(self):
        return str(self.cmc)
    
    # Get function to print off all information of the card.
    def info(self):
        print(str(self.name), str(self.type_line), str(self.mana_cost)+"\n"+
            str(self.cmc), str(self.color), str(self.effect)+"\n\n")

#Deck object containing a list of card objects.
class Deck:

    # Create the deck object
    def __init__(self):
        self.name = "deck"
        self.deck = []

    # repr function to return class in str format
    def __repr__(self):
        return str(self.name)
    
    # Adds a card to the decklist.
    def add_to_deck(self, card):
        self.deck.append(card)

    # Shuffles the deck.
    def shuffle(self):
        random.shuffle(self.deck)
    
    #Prints all cards in the deck.
    def print_all(self):
        for a in self.deck:
            print(a.info())
            #if i % 3 == 2:
            #    print("\n")


test_deck = Deck()

# Menu for user input.
def menu():
    val=True

    while val:
        print ("""
        Welcome to the Magic Deck Builder!
        1.List Current Cards 
        2.Display ideal mana-base
        3.Exit
        """)
        
        choice=input("Please Choose an Option: ")

        if choice == "1":
            test_deck.print_all()
        elif choice == "2":
            print("You chose 2.\n")
        elif choice == "3":
            print("You chose 3.\n")
            break


# Function to retrieve Json data from online, create a card object from it,
# and then add it to a deck.
def add_to_database(line):
    line = line.strip('\n')
    line = line.replace(" ", "+")
    # Access mtg database 'scryfall' to obtain correct json data for the card we need.
    with urllib.request.urlopen("https://api.scryfall.com/cards/named?fuzzy="+line) as url:
        data = json.loads(url.read().decode())

    # Create card object.    
    card = Card(data["name"], data["type_line"], data["cmc"],
                data["mana_cost"], data["colors"], data["oracle_text"])
    test_deck.add_to_deck(card)

if __name__ == '__main__':

    FILE = sys.argv[1]

    with open(FILE) as fp:
        line = fp.readline()
        while line:
            add_to_database(line)
            line = fp.readline()

    menu()
