def scramble(s1, s2):
    for element in set(s2):
        if s2.count(element) > s1.count(element):
            return False
    return True


if __name__ == "__main__":
    
    #CASOS TEST
    assert scramble('scriptjavx', 'javascript')
    assert scramble('cedewaraaossoqqyt', 'codewars')
    assert scramble('katas', 'steak')