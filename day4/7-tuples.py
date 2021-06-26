
#a list of tuples
game_score = [('Pong', 238), ('Snake', 98), ('Bounce', 397), ('Super Mario', 182)]
print("Original:")
print(game_score)

#sorts the list of tuples using lambda
game_score.sort(key = lambda x: x[1])
print("\nSorted:")
print(game_score)