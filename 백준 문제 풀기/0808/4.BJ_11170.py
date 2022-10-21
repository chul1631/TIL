T = int(input())
for _ in range(T):
	n,m = map(int,input().split())
	cnt = 0

# n부터 m까지의 수를 string형으로 바꿔서 0이 나올 때마다 cnt +1씩 증가
	for i in range(n,m+1):
		for a in str(i):
			if a == '0':
				cnt += 1
	print(cnt)