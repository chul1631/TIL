T = int(input())

for i in range(T):
    s = int(input())
    n = int(input())
    cost = s
    
    for i in range(n):
        q, p = map(int, input().split())
        cost += q * p
        
    print(cost)