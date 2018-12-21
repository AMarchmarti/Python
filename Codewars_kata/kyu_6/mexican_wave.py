'''In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.

1.  The input string will always be lower case but maybe empty.
2.  If the character in the string is whitespace then pass over it as if it was an empty seat.'''

def wave (strin):
    result =[]
    tamaño = len(strin)
    for pos in range(tamaño):
        letter = strin[pos]
        if letter != " ":
            new_word = strin[:pos] + letter.upper() + strin[pos+1:]
            result.append(new_word)
    
    return result 
        

if __name__ == "__main__":
    

    # TEST CASES #

    result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
    assert wave("hello") == result

    result2 = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
    assert wave("codewars") == result2

    result3 = []
    assert wave("") == result3

    result4 = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
    assert wave("two words") == result4

    result5 = [" Gap ", " gAp ", " gaP "]
    assert wave(" gap ") == result5