def remove_character(string, char, replace_char, times):
    return string.replace(char, replace_char, times)


def remove_character_without_replace(string, rep_char, times):
    result = ""
    count = 0
    # result = [result + i if != rep_char else count += 1 for i in string]
    for i in string:
        if i != rep_char or count >= times:
            result = result + i
        else:
            count += 1
    return result


obj = remove_character("helloo", "o", "", 1)
print(obj)

obj = remove_character_without_replace("geeksforgeeks", "e", 1)
print(obj)