face = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, "Ace": 14, "Jack": 11, "Queen": 12, "King": 13}
# game = [input() for _ in range(6)]
# for i in range(len(game)):
#     if game[i] in face:
#         game[i] = face[game[i]]
# game[:] = map(int, game)
# print(sum(game) / len(game))
mid = 0
for _ in range(6):
    mid += face[(input())]
print(mid / 6)
