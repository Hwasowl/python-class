import random as rd

for i in range(3):
    print(rd.random())

cards = [[1, '송학'], [2, '메조'], [3, '송학2'], [4, '메조2']]
print(cards)
for _ in range(3):
    rd.shuffle(cards)
    print(cards)

print(rd.sample(cards, 2))