from fractions import Fraction
import sys
from math import factorial
import matplotlib.pyplot as plt
max_coins = int(input("enter number of coins:")) #the number of coins
num_heads = int(input("enter number of heads your checking the probability (of that number turning up) for:")) #the number of heads your checking the probability for
prob_head = float(input("what will the chance be that each single coin turns up heads (THIS MUST BE A DECIMAL):")) #the chance that a single coin turns up heads (decimal)

probs = []

def calculate(num_coins):
    global num_heads, prob_head
    a = (prob_head**num_heads * (1 - prob_head)**(num_coins - num_heads))
    comb = (factorial(num_coins)) / (factorial(num_coins - num_heads) * factorial(num_heads))

#    answer = comb / (2**num_coins)
    answer = a * comb       

    return answer

for i in range(num_heads, max_coins):
    print(str(i) + " " + str(calculate(i)))
    probs.append(calculate(i))

plt.plot(probs)
plt.show()
    
