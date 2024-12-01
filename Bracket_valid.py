def valid(exp):
    brackets="({["
    stack=[]
    for s in exp:
        if s in brackets:
            stack.append(s)
        else:
            if not stack:
                return False
            elif s==')' and stack[-1]=='(':
                stack.pop()
            elif s==']' and stack[-1]=='[':
                stack.pop()
            elif s=='}' and stack[-1]=='{':
                stack.pop()
            else:
                return False
    return True

exp="]})"
print("Input: ",exp)
print("Are the brackets valid?",valid(exp))
            
        