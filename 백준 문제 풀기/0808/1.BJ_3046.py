# R1, R2 평균 = S
# 첫번째 변수 R1, 두번째 변수 S일때 R2 = ?
# 만약 a,b 평균 = c 일때  (a+b) = 2*c
# 구해야 할 값 = b 
# b = 2*c - a

R1, S = map(int, input().split())  
R2 = S*2 - R1 
print(R2)
