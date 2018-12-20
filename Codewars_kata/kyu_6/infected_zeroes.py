def infected_zeroes(lst):
    turns = 0
    lsttemporal = []
    for i in lst:
        lsttemporal.append(i)
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