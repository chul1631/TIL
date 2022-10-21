score = []
ans = 0
j = 0
for i in range(10):
# 10번 반복해서 버섯의 점수를 입력
    score.append(int(input()))
# 무한 반복
while True :
# 점수 획득
    ans += score[j]
# 점수 100점과 동일하면 즉시 반복문 종료
    if (ans ==100) : 
        break
    #ans >100 이면 ans값과 ans값에서 더해준 값 (score[j])를 빼준값 중
    # 차이가 더 작은 값 출력
    # 두 값의 차이가 같다면 둘중 더 큰 값을 출력 
    elif(ans > 100) :
        if ans - 100 <= 100 -(ans - score[j]) :
            break
        else:
            ans = ans - score[j]
        break
    j += 1
print(ans)
