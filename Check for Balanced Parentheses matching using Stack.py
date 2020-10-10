#check for balanced parenthesis. 

def areParanthesisBalanced(a):
    stack=[]
    for i in a:
        if i in ["(","{","["]:
            # Push the element in the stack
            stack.append(i)
        else:
            # If current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return(False)
            current_char=stack.pop() 
            if current_char=='(': 
                if i!=")":
                    return(False)
            if current_char=='{':
                if i!="}":
                    return(False)
            if current_char=='[':
                if i!="]":
                    return(False)
        #Check empty stack
    if stack:
        return(False)
    return(True)

a=input() 
if areParanthesisBalanced(a):
    print("Balanced") 
else:
    print("Not Balanced")
