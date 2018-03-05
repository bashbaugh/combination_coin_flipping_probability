import random
output = []
total_heads = 0
num_dice = int(input("Enter number of dice to roll:"))
num_rolls = int(input("Enter number of rolls:"))

def roll():
    out = random.randint(1, 6)
    return(out)

for i in range(0, 6*num_dice + 1):
    output.append(0)

for i in range(1, num_rolls +1):
    curr_roll = 0
    for s in range(1, num_dice + 1):
        x = roll()
        curr_roll += x
    output[curr_roll] += 1

print("each possible result turned up:")
for i in range(1, 6*num_dice + 1):
    print(str(i) + ".) \t %s" % output[i])

# for d in range(0, len(dicerolls)):
#     for r in range(0, 6):
#         results[r] += dicerolls[d][r]
