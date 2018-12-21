'''In this kata, the number 0 is infected. You are given a list. Every turn, any item in the list that is adjacent to a 0 becomes infected and 
transforms into a 0.  How many turns will it take for the whole list to become infected?
All lists will contain at least one item, and at least one zero, and the only items will be 0s and 1s. 
Lists may be very very long, so pure brute force approach will not work.'''


def infected_zeroes(lst):
    turns = 0
    lsttemporal = []
    lsttemporal = lst[:]
    if lst.count(0) == len(lst):
        return turns
    while lst.count(0) != len(lst):
        for i in range(0,len(lst)):
            if lst[i] == 0:
                if i > 0:  
                    lsttemporal[i - 1] = 0
                if i < len(lst) - 1:
                    lsttemporal[i + 1] = 0
        if i == len(lst) - 1:    
            turns += 1
            lst = lsttemporal[:]
    return turns

if __name__ == "__main__":
    

    # TEST CASES #


    assert infected_zeroes([0]) == 0
    assert infected_zeroes([0,1,1,0]) == 1
    assert infected_zeroes([0,1,1,1,0]) == 2
    assert infected_zeroes([1,1,0,1,1]) == 2
    assert infected_zeroes([1,1,1,0]) == 3
    assert infected_zeroes([0,1,1,1]) == 3