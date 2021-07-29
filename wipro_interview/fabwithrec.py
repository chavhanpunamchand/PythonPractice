
def check_pattern(str1):
    list1=[]
    for char in str1:
        if char in ["{","[","("]:
            list1.append(char)
        else:
            if not list:
                return False
            current_char=list1.pop()
            if current_char == "{":
                if char !="}":
                    return False
            if current_char == "[":
                if char !="]":
                    return False
            if current_char == "(":
                if char !=")":
                    return False

    if list1:
        return False
    else:
        return True

str1="{{[[]}}"
if check_pattern(str1):
    print("Balanced")
else:
    print("Unbalance")
