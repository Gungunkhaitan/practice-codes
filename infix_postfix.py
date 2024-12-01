def infix_to_postfix(infix_exp):
    operators="+-*/^"
    precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    stack=[]
    postfix=[]
    i=0
    while i<len(infix_exp):
        ch=infix_exp[i]
        if ch.isalnum(): 
            postfix.append(ch)
        elif ch=='(':
            stack.append(ch)
        elif ch==')':
            while stack[-1] !='(':
                postfix.append(stack.pop())
            stack.pop()
        elif ch in operators:
            while stack and stack[-1] in operators and precedence[stack[-1]]>=precedence[ch]:
                postfix.append(stack.pop())
            stack.append(ch)
        i+=1
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)
infix_exp="K+L-M*N+(O^P)*W/U/V*T+Q"
print(infix_to_postfix(infix_exp))