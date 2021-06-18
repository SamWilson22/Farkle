# --------------------------------------------------------------------------------------------
#                                  Farkle
#
#                   Playing around with the game Farkle
#                                 Sam Wilson
#
# --------------------------------------------------------------------------------------------
# 2021-05-14: Beginning of project

import itertools 

"""
Pseudo-code:

Game functionality: 
1. Create random dice
2. Create 6 random dice 
3. Detect dice values
4. Allow user to choose what to keep
5. Tabulate score

Game solving:
1. Identify relevant inputs, options, and strategies
2. Identify basic elements to strategy,(in words)
3. Research analytical methods using discrete math
4. Research calculated methods (either running simulation of calculating) 
Both are actually quite similar. 
5. Research random brute force method. Uses some sort of recursive function that
tries 
6. Symetry considerations can be used in all methods

Gui:
1. Look for online dice tools
"""

def flatten(lis):
    """flattens a list of lists"""
    return list(itertools.chain(*lis))

def valid_combination(list1,list2):
    """
    Determines whether the first list of values exists within the second list of value
    Input:
        list1 - target list (most likely smaller)
        list2 - reference list
    Output:
        True/False
    """
    list2_copy = list2.copy()
    for elem in list1:
        if elem in list2_copy:
            list2_copy.remove(elem)
            continue
        else:
            return False
    return True

def scoring_combos(dice_roll):
    """
    Lists the scoring options for a given dice roll
    Input:
        dice_roll - list of integers valued 1-6
    Ouput:
        combos - some data type that stores all individual combos
            -dice values used
            -num dice used
            -individual score 
    """
    combos = [] 
    #[dice values,scored points]]

    pairs = []
    triplets = []
    #ideally combos should be a set of ordered lists 

    #Check for 1
    for j in range(dice_roll.count(1)):
        #print("1 availble")
        combos.append([[1],100])

    #Check for 5
    for j in range(dice_roll.count(5)):
        #print("5 available")
        combos.append([[5],50])

    for i in [1,2,3,4,5,6]:
        # Check for three of a kind
        if dice_roll.count(i) >= 3:
            #print("three of a kind of {}".format(i))
            if i == 1:
                combos.append([[i]*3,300])
            else:
                combos.append([[i]*3,i*100])
        
        if dice_roll.count(i) >= 4:
            #print("four of a kind of {}".format(i))
            combos.append([[i]*4,1000])
        
        if dice_roll.count(i) >= 5:
            #print("five of a kind of {}".format(i))
            combos.append([[i]*5,2000])

        if dice_roll.count(i) >= 6:
            #print("six of a kind of {}".format(i))
            combos.append([[i]*6,3000])

        #Check for pairs
        pair_count = dice_roll.count(i)//2
        if pair_count:
            pairs += [i] * (2*pair_count)

        #Check for triplets
        triplet_count = dice_roll.count(i)//3
        if triplet_count:
            triplets += [i] * (3*triplet_count)
         
    #Check for 3 pairs [Broken if we see more than than 3 pairs in additional dice variations]
    if len(pairs) == 6:
        #print("3 pair available")
        combos.append([pairs,1500])

    #Check for straight 
    if 1 in dice_roll and 2 in dice_roll and 3 in dice_roll and 4 in dice_roll and 5 in dice_roll and 6 in dice_roll:
        #print("straight available")
        combos.append([[1,2,3,4,5,6],1500])
    
    #Check for 2 triplets  [Broken if we see more than than 2 triplets in additional dice variations]
    if len(triplets) == 6:
        #print("two triplets available")
        combos.append([triplets,2500])

    if combos == []:
        pass
        #print("no combos, no points this turn!")

    return combos

def scoring_choices(dice_roll):
    """
    Input:
        dice_roll - list of integers valued 1-6
    Output:
        options - some data type that stores all valid options
            -num dice used
            -total score
    """
    #combos - list of lists that containts all possible combos
    combos = scoring_combos(dice_roll)

    choices = []

    #L is the length of different choce options 
    for L in range(0, len(combos)+1):
        for subset in itertools.combinations(combos, L):
            total = [[],0]
            for option in subset:
                total[0].append(option[0])
                total[1] += option[1]

            choices.append(total)

    #print(choices)
    #Get rid of choices that 1. use extra dice, 2. are duplicates
    choices2 = []
    for choice in choices:
        if not choice[0] == []:
            #check that all dice from choice exist in dice roll and ignore duplicates
            #print("flattening")
            #print(flatten(choice[0]))
            #print("dice_roll")
            #print(dice_roll)
            #print("end")
            #breakpoint()
            pass

        if valid_combination(flatten(choice[0]),dice_roll) and not choice in choices2:
            choices2.append(choice)
    
    #breakpoint()
    #print(choices2)
    return choices2

def top_score(dice_roll):
    """
    """
    max_score = 0
    for choice in scoring_choices(dice_roll):
        max_score = max(max_score,choice[1])
    
    return max_score

def farkle(dice_roll):
    """
    """
    for choice in scoring_choices(dice_roll):
        if len(flatten(choice[0])) == len(dice_roll):
            return True
    return False


# XXXX #
def optimal_option(options,hand_score, total_score, opponent_score = None):
    #How does this guy determine the optimal option? 
    # 1. discrete math
    # 2. brute force    

    
    pass

def possible_rolls(num_dice):
    """
    input:
        dice - number of dice
    output: 
        dice_rolls - ordered list lists.  all possible dice rolls
            ^ ideally this shoud be handled as a set
        frequency - ordered list of ints. frequency of each dice roll
    """

    # Nested for loop that is deeper depending value of input

    dice_rolls = []
    roll_frequencies = []

    # one dice case
    if num_dice == 1:
        for i in range(6):
            dice_rolls.append([i+1])
            roll_frequencies.append(1)
        pass

    # two dice case
    if num_dice == 2:
        for i in range(6):
            die1 = i+1
            for j in range(6):
                die2 = j+1
                dice_roll = [die1,die2]
                dice_roll.sort()
                if dice_roll in dice_rolls:
                    ind = dice_rolls.index(dice_roll)
                    roll_frequencies[ind] = roll_frequencies[ind] + 1
                else:
                    dice_rolls.append(dice_roll)
                    roll_frequencies.append(1)

    # how to generalize this to n dice case? 
    return (dice_rolls,roll_frequencies)

"""
What if we made an object? 
    why object?
    - there are several steps to computing the options of a hand, but 
        we don't really wnat to forget the global information. 

"""

"""
TODO:
def possible_rolls_recursive(num_dice, dicefaces = 6):
    ##this does nests the right amount of times, but it doesn't store the data correctly. 
    if num_dice == 0:
        return [die for die in range(6)]

    for i in range(6):
        return possible_rolls_recursive(num_dice - 1)[i]
"""


if __name__ == "__main__":
    #print(possible_rolls(1))
    #print(possible_rolls(2))

    #print(scoring_combos([1,1,1,2,2,2,3,3]))
    scoring_choices([1,1,1,1])
    print("1 dice roll")
    print(possible_rolls(1))
    print("2 dice roll")
    print(possible_rolls(2))
    pass



"""
Starting from 6 dice:

    Option                              permutations
Uses all dice:
    straight                            ?
    3 pair
    nx1, (6-n)x5
    3 of a kind, nx1, (3-n)x5

Uses 5 dice:
    nx1, (5-n)x5
    3 of a kind, nx1, (2-n)x5

Uses 4 dice:
    nx1, (4-n)x5
    3 of a kind, 1
    3 of a kind, 5

Uses 3 dice:
    nx1, (3-n)x5
    3 of a kind

Uses 2 dice:
    nx1, (2-n)x5

Uses 1 dice:
    1
    5


"""


#%% Write some unit tests for hands 