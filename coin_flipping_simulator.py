import random
heads = []
total_heads = 0
num_coins = int(input("Enter number of coins:"))
num_flips = int(input("enter number of flips:"))
prob_head = float(input("Enter probability of a coin turning up heads:"))


def flip():
    out = random.random()
    return(out)


for i in range(0, num_flips):
    output = 0
    for i in range(0, num_coins):
        if flip() <= prob_head:
            output += 1
    heads.append(output)

for i in range(0, len(heads)):
    total_heads += heads[i]

print(total_heads / num_flips)    

    
    
    

