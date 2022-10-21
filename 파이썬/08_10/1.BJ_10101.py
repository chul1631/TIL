#총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다.
a = int(input())
b = int(input())
c = int(input())
# 세 각의 크기가 모두 60인 경우
if a == b == c == 60:          
    print("Equilateral")
# 세 각의 합이 180이고
elif a + b + c == 180:  
# 두 각이 같은 경우            
    if a == b or b == c or c == a: 
        print("Isosceles")
# 같은 각이 없는 경우
    else:                        
        print("Scalene")

 # 세 각의 합이 180이 아닌 경우
else:                           
    print("Error")