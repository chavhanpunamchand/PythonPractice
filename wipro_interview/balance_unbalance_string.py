


def check_balance_str(exp):
    stack=[]
    for char in exp:
        if char.isalnum() or char.isalpha():
            continue
        if char in ["{","(","["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char=stack.pop()
            if current_char =="{":
                if char != "}":
                    return False
            if current_char =="[":
                if char != "]":
                    return False
            if current_char == "(":
                if char !=")":
                    return False
    if stack:
        return False
    return True

exp="{{{}}}}"
flag=check_balance_str(exp)
if flag:
    print("Balance string")
else:
    print("Unbalance")