def create_phone_number(n):
    phone = "("
    for pos in range(0, len(n)):
        phone += str(n[pos])
        if pos == 2:
            phone += ")" + " "
        if pos == 5:
            phone += "-"
    return phone



assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
assert create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
assert create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) ==  "(123) 456-7890"
assert create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
assert create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"           
assert create_phone_number([6, 2, 0, 3, 0, 1, 0, 7, 6, 0]) == "(620) 301-0760"
