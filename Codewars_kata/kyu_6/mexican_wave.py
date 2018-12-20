def wave (strin):
    list_strin = []
    for letter in strin:
        list_strin.append(letter)
    
    assert isinstance(list_strin, list)
    assert list_strin[0] == "h"
    
    result = []
    result.append(strin.capitalize())
    rest = ""
    count = 0
    while count < len(strin) - 1:
        rest = rest + list_strin.pop(0)
        save = rest + "".join(list_strin).capitalize()
        result.append(save)
        count += 1
        

    return result

print(wave("hello"))