def duplicate_count(text):
    text = text.lower()
    duplicates = []
    for letter in text:
        number = text.count(letter)
        if number >= 2:
            if letter not in duplicates:
                duplicates.append(letter)
    return len(duplicates)

if __name__ == "__main__":
    
    assert duplicate_count("abcde") == 0
    assert duplicate_count("abcdea") ==  1
    assert duplicate_count("indivisibility") == 1
    assert duplicate_count("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26
    assert duplicate_count("indivisibilities") == 2