evenCount = 0
oddCount = 0

for i in range(1, 11):
    if i % 2 == 0:
        print(i)
        evenCount += 1
    else:
        oddCount += 1

print(evenCount)        
print(oddCount)

count_divisible_3_5 = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        count_divisible_3_5 += 1
print(count_divisible_3_5)    