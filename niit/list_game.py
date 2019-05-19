import random

def giveScore(x):
    return x*random.randint(1,20)

num_p = int(input("Enter number of players: "))
num_v = num_p

list_p = list(range(1,num_p+1))
list_v = list(range(1,num_v+1))

player_score = [giveScore(x) for x in list_p]
villain_score = [giveScore(x) for x in list_v]

win = True

len_p = len(player_score)

x = 0

player_score.sort()
villain_score.sort()

print("Player score is: ",player_score)
print("Villain score is: ",villain_score)

while x < len_p:
    if player_score[x] < villain_score[x]:
        win = False
    x += 1

if win == True:
    print("Player Wins!")
else:
    print("Villain Wins!")