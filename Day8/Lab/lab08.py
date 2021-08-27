## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x > y:
        r = x % y
        return gcd(r, y)
    else:
        r = y % x
        return gcd(x, r)
    

## Problem 2
## Write a function using recursion that returns prime numbers less than 121
## remember, primes are not the product of 
## any two numbers except 1 and the number itself
## hint, "hardcode" 2
def find_primes(me = 121,  primes = []):
    if me == 2:
        primes.append(2)
        return primes

    flag = True
    for i in range(2, me):
        if me % i == 0:
            flag = False
            break
    if flag:
        primes.append(me)
        
    return find_primes(me-1, primes)
        
print(find_primes())
         
            
 
## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html

def TowerOfHanoi(n, source, destination, auxiliary):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
# Driver code
n = 3
TowerOfHanoi(n,'A','B','C')
        
    