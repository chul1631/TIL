
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print( "#%d %d %d" % (i+1, a//b, a%b) )