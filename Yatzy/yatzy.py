class Yatzy:

    @staticmethod
    def chance(*args):
        total = 0
        for dice in args:
            total += dice
        return total

    @staticmethod
    def yatzy(*dices):
        return 50 if dices.count(dices[0]) == 5 else 0
            
    
    @staticmethod
    def ones(*args):
        sum = 0
        for one in args:
            if one == 1:
                sum += 1
        return sum
    
    

    @staticmethod
    def twos(*args):
        sum = 0
        for two in args:
            if two == 2:
                sum += 2
        return sum
    
    @staticmethod
    def threes(*args):
        sum = 0
        for three in args:
            if three == 3:
                sum += 3
        return sum
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    

    @staticmethod
    def fours(*args):
        sum = 0
        for four in args:
            if four == 4:
                sum += 4
        return sum
    
    @staticmethod
    def fives(*args):
        sum = 0
        for five in args:
            if five == 5:
                sum += 5
        return sum
    
    @staticmethod
    def sixes(*args):
        sum = 0
        for six in args:
            if six == 6:
                sum += 6
        return sum
       
    @staticmethod
    def pair(*dice):
        maximum = 0
        for die in dice:
            if die > maximum and dice.count(die) >= 2:
                maximum = die
                
        return maximum * 2
    
    
    @staticmethod
    def two_pair(*dice):
        pair = 0
        score = 0
        i= 1
        while i <= 6:
            if dice.count(i) >= 2:
                pair += 1
                score += i * 2
            i += 1
        if pair == 2:
            return score
        return 0
    
    @staticmethod
    def four_of_a_kind(*dice):
        for i in range(6):
            if dice.count(i) >= 4:
                return i * 4
        return 0
    

    @staticmethod
    def three_of_a_kind(*dice):
        for i in range(6):
            if dice.count(i) >= 3:
                return i * 3
        return 0
    

    @staticmethod
    def smallStraight(*dice):
        for die in range(1, 6):
            if dice.count(die) != 1:
                return 0
        return Yatzy.chance(*dice)
    

    @staticmethod
    def largeStraight(*dice):
        for die in range(2, 7):
            if dice.count(die) != 1:
                return 0
        return Yatzy.chance(*dice)
    

    @staticmethod
    def fullHouse(*dice):
        threes = 0
        score = 0
        pair = 0
        for die in range(7):
            if dice.count(die) == 3:
                threes +=1
                score += die * 3
            if dice.count(die) == 2:
                pair +=1
                score += die * 2
        if threes == 1 and pair == 1:
            return score
        else:       
            return 0

if __name__ == "__main__":

    #Funcion chance Casos Tests
    assert 15 == Yatzy.chance(2,3,4,5,1)
    assert 16 == Yatzy.chance(3,3,4,5,1)
    assert Yatzy.chance(6, 5, 3, 3, 6, 1) == 24

    #Funcion yatzy Casos Tests
    assert 50 == Yatzy.yatzy(6,6,6,6,6)
    assert 0 == Yatzy.yatzy(6,6,6,6,3)
    assert 0 == Yatzy.yatzy(1,2,3,7,5)

    #Funcion ones Casos Tests
    assert Yatzy.ones(1,2,3,4,5) == 1
    assert 2 == Yatzy.ones(1,2,1,4,5)
    assert 0 == Yatzy.ones(6,2,2,4,5)
    assert 4 == Yatzy.ones(1,2,1,1,1)

    #Funcion Twos Casos Tests
    assert 4 == Yatzy.twos(1,2,3,2,6)
    assert 10 == Yatzy.twos(2,2,2,2,2)

    #Funcion threes Casos Tests
    assert 6 == Yatzy.threes(1,2,3,2,3)
    assert 12 == Yatzy.threes(2,3,3,3,3)

    #Funcion fours Casos Tests
    assert 12 == Yatzy.fours(4,4,4,5,5)
    assert 8 == Yatzy.fours(4,4,5,5,5)
    assert 4 == Yatzy.fours(4,5,5,5,5)

    #Funcion fives Casos Tests
    assert 10 == Yatzy.fives(4,4,4,5,5)
    assert 15 == Yatzy.fives(4,4,5,5,5)
    assert 20 == Yatzy.fives(4,5,5,5,5)

    #Funcion sixes Casos Tests
    assert 0 == Yatzy.sixes(4,4,4,5,5)
    assert 6 == Yatzy.sixes(4,4,6,5,5)
    assert 18 == Yatzy.sixes(6,5,6,6,5)
    
    #Funcion one_pair Casos Tests
    assert 6 == Yatzy.pair(3,4,3,5,6)
    assert 10 == Yatzy.pair(5,3,3,3,5)
    assert 12 == Yatzy.pair(5,3,6,6,5)
    
    #Funcion Two_pairs Casos Tests
    assert 16 == Yatzy.two_pair(3,3,5,4,5)
    assert 18 == Yatzy.two_pair(3,3,6,6,6)
    assert 0 == Yatzy.two_pair(3,3,6,5,4)

    #Funcion Four_of_a_kind
    assert 12 == Yatzy.four_of_a_kind(3,3,3,3,5)
    assert 20 == Yatzy.four_of_a_kind(5,5,5,4,5)
    assert 12 == Yatzy.four_of_a_kind(3,3,3,3,3)
    assert 0  == Yatzy.four_of_a_kind(3,3,3,2,1)

    #Funcion Three_of_a_kind
    assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
    assert 15 == Yatzy.three_of_a_kind(5,3,5,4,5)
    assert 9 == Yatzy.three_of_a_kind(3,3,3,3,5)

    #Funcion Small
    assert 15 == Yatzy.smallStraight(1,2,3,4,5)
    assert 15 == Yatzy.smallStraight(2,3,4,5,1)
    assert 0 == Yatzy.smallStraight(1,2,2,4,5)

    #Funcion Large
    assert 20 == Yatzy.largeStraight(6,2,3,4,5)
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(1,2,2,4,5)

    #Funcion Full House
    assert 18 == Yatzy.fullHouse(6,2,2,2,6)
    assert 0 == Yatzy.fullHouse(2,3,4,5,6)