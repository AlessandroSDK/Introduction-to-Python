import random

class Greeter(object):
   
    def __init__(self, name):
        self.name = name
        
    def hello(self):
        print("Hello " + self.name)

    def goodbye(self):
        print("Goodbye " + self.name)

g = Greeter("Alessandro")
g.hello()
g.goodbye()


class Die(object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

print("D6 rolls")
d = Die(6)
print(d.roll())
print(d.roll())
print(d.roll())

print("D20 rolls")
d = Die(20)
print(d.roll())
print(d.roll())
print(d.roll())


# Generating a list with all cards combinations and shuffle 3 at the time

class Deck(object):
    def shuffle(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank + " of " + suit)
        random.shuffle(self.cards)
     
    def deal(self):
         return self.cards.pop()
d = Deck()
d.shuffle()
print(d.deal())
print(d.deal())
print(d.deal())
