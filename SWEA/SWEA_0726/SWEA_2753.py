year = int(input())
if (year %4 == 0 and year %100 !=0) or year %400 == 0:
    #4의 배수이면서 100의 배수가 아닐때, 400의 배수일때
    print("1")
else: 
    print("0")