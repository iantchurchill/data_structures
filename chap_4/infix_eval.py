from pythonds.basic import Stack

def tokenize(expr):
    lst = list(expr)
    result = [ch for ch in lst if ch != " "] #tokenize, supports mixed whitespacing\
    return result                           # but not exponentiation
    
def checkBalance(tokens):
    return tokens.coun("(") == tokens.count(")")

def reToken(lst):
    result = []
    digits = "01234567890"
    ops = "*/+-"
    for i, ch in enumerate(lst):
        token = ch
        if (ch in digits and lst[i+1] in digits) or ch in ops and lst[i+1]:
            token += lst[i+1]
        result.append(token)
            
def infixToPostfix(infixexpr):
    prec = {}
    prec["**"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = tokenize(infixexpr)
    

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + 23 * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
