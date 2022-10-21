import sys
sys.stdin = open("input1.txt")

TC = int(input())

# r = 광고를 하지 않았을 때 수익  
# e = 광고를 했을 때의 수익 
# c = 광고 비용

for i in range(TC):
    r,e,c = map(int, input().split())
    

# 광고를 해야 하면 "advertise"
# 하지 않아야 하면 "do not advertise" 
# 광고를 해도 수익이 차이가 없다면 "does not matter"를 출력한다.

#1 = r < e-c 광고수익 - 광고비용이 광고 안한 비용보다 더크면 advertise
#2 = r == e-c 같다면 do not advertise
#3 하면안됨 = 수익 or 같을때 제외

    if r < e - c:
        print('advertise') #1
    elif r == e - c:
        print('does not matter') #2
    else:
        print('do not advertise') #3
