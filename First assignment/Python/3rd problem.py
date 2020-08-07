count = 0
nxt = 1
add = 0
max_no = int(input("Please enter the maximum denominator value. = "))
while nxt > 0.001:
    nxt = 1 / (count + 1)
    print("nxt=", nxt)
    add = add + nxt
    print("add=", add)
    count = count + 1
    if count >= max_no:
        break
if nxt <= 0.001:
    print("The limit reached(The sum changed by 0.001)")
print("The sum is =", add)
