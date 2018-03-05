# coin flipping probability calculator
print("setting up...")
#import modules
from fractions import Fraction
import sys
from math import factorial
import matplotlib.pyplot as plt
from time import sleep
#get user input
input_max_coins = int(input("enter number of coins to calculate to when graphing variable number of coins:"))
input_num_heads = int(input("enter number of heads your checking the probability (of that number turning up) for:")) #the number of heads your checking the probability for
input_prob_head = float(input("what will the chance be that each single coin turns up heads (THIS MUST BE A DECIMAL):")) #the chance that a single coin turns up heads (decimal)
input_num_coins = int(input("enter number of coins:"))# number of coins

def graph_var_numcoins():
    #graph with variable number of coins
    probs = []
    print("calculating with variable number of coins...")
    sleep(.8)
    #add 0 chance to graph where number of coins is less than number of heads being checked for:
    for i in range(0, input_num_heads + 1):
        probs.append(0)
    #calculate graph from number pof heads being checked for to max coins input:
    for i in range(input_num_heads, input_max_coins + 1):
        prob = calculate(i, input_num_heads, input_prob_head)
        print(str(i) + " " + str(prob))
        probs.append(prob)
    plt.plot(probs, label="variable number of coins")

def graph_var_numheads():
    #graph with variable number of heads being checked for
    probs = []
    print("calculating with variable number of heads turning up...")
    sleep(.8)
    for i in range(0, input_num_coins + 1):
        prob = calculate(input_num_coins, i, input_prob_head)
        print(str(i) + " " + str(prob))
        probs.append(prob)
    plt.plot(probs, label="variable number of heads turning up")
def graph_var_probhead():
    #graph with variable probability of a head turning up.
    probs = []
    print("calculating with variable probability of a head turning up...")
    sleep(.8)
    for i in range(0, 101):
        prob = calculate(input_num_coins, input_num_heads, i/100)
        print(str(i) + " " + str(prob))
        probs.append(prob)
    plt.plot(probs, label="variable probability of a head turning up(percentage)")

def calculate(num_coins, num_heads, prob_head):
    #calculate answer(probability) using a mathematical combination formula:
    a = (prob_head**num_heads * (1 - prob_head)**(num_coins - num_heads))
    comb = (factorial(num_coins)) / (factorial(num_coins - num_heads) * factorial(num_heads))

    answer = a * comb

    return answer


#calculate and graph:
graph_var_numcoins()
graph_var_numheads()
graph_var_probhead()
answer = calculate(input_num_coins, input_num_heads, input_prob_head)
print("done.")
print(str(answer) + " or " + str(Fraction(answer)))
sleep(1)
#add graph labels and show it:
plt.xlabel("coins, heads, and chance of a head")
plt.ylabel("probability of certain scenario turning up")
plt.legend(loc='upper right')
plt.text(50, 0.01, "coins: " + str(input_num_coins) + ", heads: " + str(input_num_heads) + ", prob of a head: " + str(input_prob_head))
plt.show("me")
print("goodbye!")
