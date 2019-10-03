from timeit import Timer

# Python code to demonstrate naive 
# method to compute gcd ( recursion ) 
  
def hcfnaive(a, b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b) 

# Python code to demonstrate naive 
# method to compute gcd ( Loops ) 
  
  
def loopGCD(x,y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd


# Python code to demonstrate naive 
# method to compute gcd ( Euclidean algo ) 
  
  
def euclidGCD(x,y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x


t1 = Timer("hcfnaive(60,48)", "from __main__ import hcfnaive")
print("hcfnaive ",t1.timeit(number = 1000), "milliseconds")

t2 = Timer("loopGCD(60, 48)", "from __main__ import loopGCD")
print("loopGCD ",t2.timeit(number = 1000), "milliseconds")

t3 = Timer("euclidGCD(60, 48)", "from __main__ import euclidGCD")
print("euclidGCD ",t3.timeit(number = 1000), "milliseconds")