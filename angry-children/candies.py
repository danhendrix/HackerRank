# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
k = int(raw_input())
candies = []
for i in xrange(0, n):
   candies.append(int(raw_input()))

candies = sorted(candies)
#print candies
def findLowest(candies,k):
	lowest_list = []
	for i in candies[:(-k+1)]:
		#print "new line! it is: {}".format(i)
		super_count = 0
		current_sum = []
		while super_count < (len(candies)-k+1):
			count = 1
			while (count + super_count) < k:
				current_sum.append(abs(candies[candies.index(i)+super_count] - candies[candies.index(i)+count+super_count]))
				#print abs(candies[super_count] - candies[count+super_count]) 
				count += 1
			super_count += 1
			
		lowest_list.append(sum(current_sum))
				 
		print "lowest_list = {}".format(lowest_list)
	return min(lowest_list)

ans = findLowest(candies,k)

print ans

