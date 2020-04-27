a = int(input())
b = int((input()))
flag = 0
if a == b:
	print("Divisible")
else:
	while(a > b):
		flag = flag + b
		if flag == a:
			print("Divisible")
			break

	