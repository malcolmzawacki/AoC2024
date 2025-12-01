f = open('text/day1.txt')
text = f.read()
text = text.split('\n')
list1, list2, total,similarity = [],[], 0,0
for row in text:
    list1.append(int(row.split(' ')[0]))
    list2.append(int(row.split(' ')[3]))
list1.sort()
list2.sort()

for i in range(len(list1)):
    total+=abs(list1[i]-list2[i])
    similarity+=list2.count(list1[i])*list1[i]

print(total)
print(similarity)