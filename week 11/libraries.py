# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

# number = random.randint(1,10)
# print(number)

# cards = ["jack", "queen", "king", "Ace"]
# random.shuffle(cards)
# for card in cards:
#     print(cards)

# import statistics
# print(statistics.mean([100, 90]))

import sys
import cowsay
try:
    cowsay.cow("Hello,", sys.argv[1])
except IndexError:
    # print("Too few arguments")
    sys.exit()