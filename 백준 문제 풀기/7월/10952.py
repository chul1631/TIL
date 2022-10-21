while True: #무한반복하겠다.
    A, B=map(int, input().split()) #A, B를 정수로 입력을 받겠다.
    if(A==0 and B==0): #A가 0일때와 B가 0일때 모두를 만족한다면,
        break #반복을 종료하겠다.
    else: #if문에 해당되지 않는다면,
        print(A+B) #A+B의 합을 구하겠다.