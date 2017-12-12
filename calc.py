from sys import argv

num_coins = argv[1]
num_heads = argv[2]
prob_head = argv[3]


def calculate():
    global num_coins, num_heads, prob_head
    prob_head**num_heads * (1 - prob_head)**(num_coins-num_heads) * ( 
    

print("running...")
calculate()
print("\n finished")
    
