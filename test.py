n = [9,5,3,6,8,1,4]

# length = len(n) - 1

# while length:
# 	for i in range(length):
# 		if n[i]>n[i+1]:
# 			n[i],n[i+1] = n[i+1],n[i]
# 	length -= 1


# def quick_sort(n):
# 	if len(n)<2: return n
# 	return quick_sort([lt for lt in n[1:] if lt<= n[0]]) + n[0:1] + quick_sort([rt for rt in n[1:] if rt> n[0]])

# x = quick_sort(n)
# print(x)	


# def insert_sort(sort_list):
# 	length = len(sort_list)
# 	for i in range(1,length):
# 		for j in range(i,0,-1):
# 			if sort_list[j] < sort_list[j-1]:
# 				sort_list[j],sort_list[j-1] = sort_list[j-1],sort_list[j]
# 			else:
# 				break

# insert_sort(n)
# print(n)


length = len(n)
for i in range(length-1):
	min_index = i
	for j in range(i+1,length):
		if n[min_index] > n[j]:
			min_index = j
	n[i],n[min_index] = n[min_index],n[i]
print(n)







