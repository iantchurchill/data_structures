def genNums(start, end):
    for i in range(start,end+1):
        yield i
        
x = genNums(1,10)
print(next(x))