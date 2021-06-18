from Farkle import scoring_combos
from Farkle import scoring_choices
from Farkle import top_score

def test_scoring_combos_empty():
    """scoring combos of empty list should be none"""
    assert scoring_combos([]) == []

def test_scoring_combos_five():
    """scoring combos of 5 is correct"""
    assert [[5],50] in scoring_combos([5])

def test_scoring_combos_one():
    """scoring combos of 1 is correct"""
    assert [[1],100] in scoring_combos([1])

def test_scoring_combos_triple():
    """scoring combos of triplets are correct"""
    assert [[1,1,1],300] in scoring_combos([1,1,1])
    assert [[2,2,2],200] in scoring_combos([2,2,2])
    assert [[3,3,3],300] in scoring_combos([3,3,3])
    assert [[4,4,4],400] in scoring_combos([4,4,4])
    assert [[5,5,5],500] in scoring_combos([5,5,5])
    assert [[6,6,6],600] in scoring_combos([6,6,6])

def test_scoring_combos_4ofakind():
    """scoring combos of 4ofakind are correct"""
    assert [[1,1,1,1,1],1000] in scoring_combos([1,1,1,1])

def test_scoring_combos_4ofakind():
    """scoring combos of 5ofakind are correct"""
    assert [[1,1,1,1,1],2000] in scoring_combos([1,1,1,1,1])
    
def test_scoring_combos_6ofakind():
    """scoring combos of 6ofakind are correct"""
    assert [[1,1,1,1,1,1],3000] in scoring_combos([1,1,1,1,1,1])

def test_scoring_combos_straight():
    """scoring combos of straight are correct"""
    assert [[1,2,3,4,5,6],1500] in scoring_combos([1,2,3,4,5,6])
    
def test_scoring_combos_3pair():
    """scoring combos of 3pair are correct"""
    assert [[1,1,2,2,3,3],1500] in scoring_combos([1,1,2,2,3,3])

def test_scoring_combos_2triples():
    """scoring combos of 2triplets are correct"""
    assert [[1,1,1,2,2,2],2500] in scoring_combos([1,1,1,2,2,2])

def test_scoring_choices_basic():
    """ 123 """
    assert [[[1]],100] in scoring_choices([1,1,5,5])

def test_top_score_basic():
    """..."""
    assert 1000 == top_score([1,1,1,1])