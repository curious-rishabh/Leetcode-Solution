answer = [[],[]]
set1 = set(nums1)
set2 = set(nums2)
for i in set1:
    if i not in set2:
        answer[0].append(i)

for i in set2:
    if i not in set1:
        answer[1].append(i)
return answer