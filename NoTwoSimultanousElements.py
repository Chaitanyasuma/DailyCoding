#to find whether a given list has elements that can be arranged such that no two same elements occuerside by side
from collections import Counter
nums = list(map(int,input("\nEnter the numbers : ").strip().split()))
dic = Counter(nums)
flag = 0
for i in dic:
    if (dic[i] > (len(nums)/2)):
    	flag = 1
if flag == 0:
	print("Possible")
else:
	print("Not possible")
                