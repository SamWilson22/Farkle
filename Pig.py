#Big is a simpler game than farkle. There is a paper that describes
#the optimal strategy here:
#chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://cs.gettysburg.edu/~tneller/papers/pig.pdf

#I am not a big fan of the way this optimal strategy has come about.
#It is based on the other player playing optimum as well, which doesn't seem quite right to me
#You are doing needless calculations if you have to calculate all the way to the end in order to determine 
#the optimum strategy. Instead, there are rules of thumb you can use to get pretty close.

#I want to do the simple pig game like in the paper, but the goal is not game theoretic.
#The goal is simply to minimize your average play time.


import random 

def flip_a_coin():
    return random.randint(0,1)

if __name__ == "__main__":
    for i in range(10):
        print(flip_a_coin())

# Goal, win in 5 turns.

#how to frame this problem....?????
print('hello world')

#round 1
flip_a_coin()