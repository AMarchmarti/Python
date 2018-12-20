#The goal of this exercise is to convert a string to a new string where each character in the new string is 
# '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    encoder = {}
    for character in word:
        if character.lower() in encoder:
            encoder[character.lower()] = ")"
        else:
            encoder[character.lower()] = "("
    assert isinstance(encoder,dict)

    solution_encoder = ""
    for character in word:
        solution_encoder = solution_encoder + encoder[character.lower()]
    assert isinstance(solution_encoder, str)
    
    return solution_encoder



if __name__ == "__main__":

    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("