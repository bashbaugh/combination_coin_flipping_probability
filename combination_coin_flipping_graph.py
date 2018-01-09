print("setting up...")
from fractions import Fraction
import sys
from math import factorial
import matplotlib.pyplot as plt
from time import sleep
input_max_coins = int(input("enter number of coins to calculate to when graphing variable number of coins:")) #the number of coins
input_num_heads = int(input("enter number of heads your checking the probability (of that number turning up) for:")) #the number of heads your checking the probability for
input_prob_head = float(input("what will the chance be that each single coin turns up heads (THIS MUST BE A DECIMAL):")) #the chance that a single coin turns up heads (decimal)
input_num_coins = int(input("enter number of coins:"))
#add prob head multiple

def graph_var_numcoins():
    probs = []
    print("calculating with variable number of coins...")
    sleep(2)
    for i in range(input_num_heads, input_max_coins + 1):
        prob = calculate(i, input_num_heads, input_prob_head)
        print(str(i) + " " + str(prob))
        probs.append(prob)
    plt.plot(probs, label="variable number of coins")
def graph_var_numheads():
    probs = []
    print("calculating with variable number of heads turning up...")
    sleep(2)
    for i in range(0, input_num_coins + 1):
        prob = calculate(input_num_coins, i, input_prob_head)
        print(str(i) + " " + str(prob))
        probs.append(prob)
    plt.plot(probs, label="variable number of heads turning up")
def graph_var_probhead():
    probs = []
    print("calculating with variable probability of a head turning up...")
    sleep(2)
    for i in range(0, 101):
        prob = calculate(input_num_coins, input_num_heads, i/100)
        print(str(i) + " " + str(prob))
        probs.append(prob)
    plt.plot(probs, label="variable probability of a head turning up")

def calculate(num_coins, num_heads, prob_head):
    a = (prob_head**num_heads * (1 - prob_head)**(num_coins - num_heads))
    comb = (factorial(num_coins)) / (factorial(num_coins - num_heads) * factorial(num_heads))

    answer = a * comb       

    return answer



graph_var_numcoins()
graph_var_numheads()
graph_var_probhead()
print("done.")
sleep(1)
plt.legend()
plt.text(50, 0.01, "coins: " + str(input_num_coins) + ", heads: " + str(input_num_heads) + ", prob of a head: " + str(input_prob_head))
plt.show()
print("goodbye!")
    
