#Welcome.
#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
#"a" = 1, "b" = 2, etc.

def alphabet_position(text):
    txt = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num_alphabet = []
    for letter in txt:
        for letter_alphabet in alphabet:
            if  letter == letter_alphabet:
                value = str(alphabet.find(letter) + 1)
                num_alphabet.append(value)
    return " ".join(num_alphabet)


if __name__ == "__main__":

    # CASOS TEST  

    print(alphabet_position("The sunset sets at twelve o' clock."))
    ##expected solution: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    
    print(alphabet_position("The narwhal bacons at midnight.")) 
    ##expected solution: "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"