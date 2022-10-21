
# same3 / 10000 + 같은눈 x 1000w
# same2 / 1000 + 같은눈 x 100w
# samex / 가장 큰 눈 x 100w 

a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b:
    print(1000+a*100)
elif a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(100 * max(a,b,c))