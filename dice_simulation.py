#Plot probability distribution of dice

import matplotlib.pyplot as plt 
import itertools
from Farkle import *


#There are other data structures (and perhaps calculation methods) that are more optimum here
def calc_permutations(num_dice):
# ----------- The result of this function is used in all other functions ----------- #
    """
    calculates all the different permutations for a certain number of dice
    """
    hex_options = [1,2,3,4,5,6]

    #One Liner
    #permutations = [r for r in itertools.product(*(num_dice*[hex_options]))] 
    
    ## One Liner Broken Down 
    #Create list of hex_option lists of lenght num_dice
    all_dice = num_dice * [hex_options]
    #Create cartesianc prodcut using itertools
    cart_prod = itertools.product(*all_dice)
    #Populate a list from the cartesian product iterator
    permutations = [r for r in cart_prod]

    return permutations 

def chance_of_egg(permutations):
    """calculate the chance of getting an egg for num_dice"""
    top_scores = []
    for roll in permutations:
        top_scores.append(top_score(list(roll)))
    
    return top_scores.count(0)/len(top_scores)

def average_points_per_roll_1(permutations):
    """
    first order approximation of points per roll
    (simply chooses highest scoring option)
    """
    top_scores = []
    for roll in permutations:
        top_scores.append(top_score(list(roll)))
    
    return sum(top_scores) / len(top_scores)

def average_farkles(permutations):
    farkles = [] 
    for roll in permutations:
        if farkle(list(roll)):
            farkles.append(1)
        else:
            farkles.append(0)
    
    return sum(farkles) / len(farkles)

def plot_scores(num_dice, permutations):
    top_scores = []
    for roll in permutations:
        top_scores.append(top_score(list(roll)))

    fig, ax = plt.subplots()
    ax.hist(top_scores,7*num_dice)
    plt.plot()
    plt.title("{} dice score histogram".format(num_dice))
    plt.ylabel("roll frequency")
    plt.xlabel("points")
    plt.show()

if __name__ == "__main__":
    permuations = calc_permutations(2)

"""
if __name__ == "__main__":

    for i in [6,5,4,3,2,1]:
        permutations = calc_permutations(i)
        egg = chance_of_egg(permutations)
        average_point = average_points_per_roll_1(permutations)
        farkle_percent = average_farkles(permutations)
        cutoff = average_point / egg
        cutoff2 = average_point / egg + farkle_percent * 388
        print("{} Dice".format(i))
        print("   Chance of egg:{:.3f}".format(egg))
        print("   Average score:{:.3f}".format(average_point))
        print("   Average farkles:{:.3f}".format(farkle_percent))
        print("   Cutoff Score: {:.3f}".format(cutoff))
        print("   Cutoff Score2: {:.3f}".format(cutoff2))
        #plot_scores(i,permutations)
"""
