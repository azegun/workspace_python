data = [3, 2, 1, 5, 4]

sorted_data = sorted(data)
print(sorted_data)

data1 =[("000060", 8.25), ("000020", 5.75), ("039490", 1.3)]

print(data1)
# pbr이 낮은 순서대로 정렬
data1.sort(key=lambda x:x[1])
print(data1)



