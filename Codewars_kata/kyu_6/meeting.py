def meeting(s):
    arr = s.split(";")
    lst = []
    for element in arr:
        lst.append(element.split(":"))
    for item in lst:
        for pos in range(0, len(item)-1):
            aux = item[pos].upper()
            item[pos] = item[pos + 1].upper()
            item[pos + 1] = aux
    lst.sort()
    final = ""
    for item in lst:
        final += "(" + ", ".join(item) + ")"
    
    return final

if __name__ == "__main__":

    assert meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn") ==  "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)"
           