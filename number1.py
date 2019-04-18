
def countWays(n,m): 
    
    
    mem = [0] * (n + 1)
    mem[0] = 1
    mem[1] = 1
    mem[2] = 2
    for i in range (3,n+1):
        mem[i] = 0
        for j in range (1,m+1):
            if(j <=i):
                mem[i] = mem[i] + mem[i-j]
                j = j + 1
        
       
    return mem[n] % 65535
        
    
      
    
        
n = int(input("Enter number of marbles: "))
m = int(input("Enter maximum to pick:"))
output = countWays(n,m)
print("Number of ways: ",output)