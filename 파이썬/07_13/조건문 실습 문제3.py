dust = -10

if dust > 150:
	print('매우나쁨')
elif dust  > 80:
	print('나쁨')
elif dust > 30:
 	print('보통')
else:
	if dust < 0: 
		print('음수')
	else:
		print('좋음')