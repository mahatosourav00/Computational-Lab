max = 6
add = 0
diff = 0
no = 0
for y1 in range(max):
    x1 = 0
    for x1 in range(max):
        y2 = 0
        for y2 in range(max):
            x2 = 0
            for x2 in range(max):
                diff = abs(x2 - x1) + abs(y2 - y1)
                add = add + diff
                no = no + 1
print("Total distance = ", add)
average = add/no
print("Average distance = ", average)