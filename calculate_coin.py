# to calculate the probability of a certain number of heads turning up when you flip x coins
from fractions import Fraction
import sys
from math import factorial

print("welcome!")
#this is the command line argument version:
#
# try:
#     num_coins = int(sys.argv[1]or input("number of coins")) #the number of coins
#     num_heads = int(sys.argv[2] or input("number of heads your checking the probability (of that number turning up) for")) #the number of heads your checking the probability for
#     prob_head = float(sys.argv[3] or input("what will the chance be that each single coin turns up heads (THIS MUST BE A DECIMAL)")) #the chance that a single coin turns up heads (decimal)
# except:
#     print("\nplease run this program with three arguments: python [program name] [number of coins] [number of heads your\
#  checking probability for] [chance that each single coin turns up heads (THIS MUST BE A DECIMAL)]")
#
#     exit()
#
# this is the input version:

num_coins = int(input("enter number of coins:")) #the number of coins
num_heads = int(input("enter number of heads your checking the probability (of that number turning up) for:")) #the number of heads your checking the probability for
prob_head = float(input("what will the chance be that each single coin turns up heads (THIS MUST BE A DECIMAL):")) #the chance that a single coin turns up heads (decimal)

def calculate():
    global num_coins, num_heads, prob_head

    answer = prob_head**num_heads * (1 - prob_head)**(num_coins - num_heads) * \
        (factorial(num_coins)) / (factorial(num_coins - num_heads) * factorial(num_heads))

    return answer


print("calculating...\n")
print("The probability that you will get " + str(num_heads) + " heads when you flip " + str(num_coins) + " coins, which \
each (seperately) have a " + str(prob_head * 100) + "% probability of landing on heads, is:\n")
print(str(calculate()) + " or " + str(Fraction(calculate())))
try:
    end = input("press enter to exit")
except:
    print("goodbye!")
