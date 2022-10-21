T = int(input())
for x in range(1, T+1):
    N = int(input())
    count = 0
    
    zero_to_nine = [str(i) for i in range(10)]
    while zero_to_nine:
        count += 1
        room = N * count
        room = str(room)

        for c in room:
            if c in zero_to_nine:
                zero_to_nine.remove(c)

    print('#{} {}'.format(x, room))


T = int(input())
for test_case in range(1, T+1):
    # Input 가져오기
    N = input(())
    # Set에 계속 추가 예정
    numbers = set()
    # while 반복 => set 길이가 10이 될 때 까지
    while len(numbers) < 10:
        # for 반복 : 숫자를 문자로
        for n in str(N):
        # numbers set에 계속 추가
            numbers.add(n)
        print(n, numbers)
        N += N