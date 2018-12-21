def score(dice):
    for i in dice:
        if dice.count(i) < 3:
            result = (dice.count(1) * 100) + (dice.count(5) * 50)
         
        if dice.count(i) >= 3 and ((dice.count(i) > dice.count(5)) or (dice.count(i) > dice.count(1))):
            if i == 1:
                return 1000 + (dice.count(5) * 50) + ((dice.count(1) - 3) * 100)
            elif i == 6:
                return 600 + result
            elif i == 5:
                return 500 + (dice.count(1) * 100) + ((dice.count(5) - 3) * 50)
            elif i == 4:
                return 400 + result
            elif i == 3:
                return 300 + result
            elif i == 2:
                return 200 + result
    return result
    
        

dice = [2, 4, 4, 5, 4]
print(score(dice))