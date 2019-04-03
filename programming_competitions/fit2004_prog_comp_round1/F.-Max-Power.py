n = int(input())
power_list = list(map(int, input().strip().split()))

#with open('randomPowers.txt','r') as f:
#	power_list = list(map(int,f.readlines()[1].split()))

#power_list = [3,58,284,284,286,284,1001]

power_list.sort()
length = len(power_list)
max_power = max(power_list)

powers_count = [0]*(max_power+1)
for power in power_list:
	powers_count[power] += 1

prefix_count = [0]*(max_power+1)
for i in range(1, len(powers_count)):
	prefix_count[i] = prefix_count[i-1] + powers_count[i]

#print(powers_count)
#print(prefix_count)

total_power = [0]*length
#totals = [0]*length
maxxx = 0

for j in range(length):
#	print(j)
	power_j = power_list[j]
	
#	print('power_j is', power_j)
	
#	totals[j] = sum([power_list[k] - (power_list[k] % power_j) for k in range(j,length)])
	n = 1
	totalNs = 0
	for k in range(power_j, max_power+1, power_j):
#		print(k)
		try:
			totalNs += (prefix_count[k+power_j-1]-prefix_count[k-1])*n
		except:
			totalNs += (prefix_count[max_power]-prefix_count[k-1])*n
		n += 1
	
	power_sum = power_j*totalNs
	total_power[j] = power_sum
	
	
#for z in range(len(totals)):
#	if power_list[z-1] == power_list[z]:
#		continue
#	if totals[z] != total_power[z]:
#		print('dammit', z)
#		break
		
#print(totals)
#print(total_power)
print(max(total_power))
	