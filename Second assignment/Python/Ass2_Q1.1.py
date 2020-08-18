add = 0
diff = 0
no = 0
for i in range(6):
    for j in range(6):
        diff = abs(i - j)
        add = add + diff
        no = no + 1
print("Total distance = ", add)
average = add / 36
print("Average distance = ", average)
