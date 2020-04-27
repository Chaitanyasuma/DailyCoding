'''Implement division of two positive integers without using the division, multiplication, 
or modulus operators. Return the quotient as an integer, ignoring the remainder.'''
a = int(input())
b = int((input()))
counter = 0
flag = 0
if a == b:
	print("Divisible")
	flag = 1
else:
	while(a > counter):
		counter = counter + b
		if counter == a:
			print("Divisible")
			flag = 1
			break
		#end if
	#end while
	if flag == 0:
		print("Not Divisible")
#end else
'''Output:
1899
3
Divisible
'''
