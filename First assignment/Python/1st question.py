count = 0
add = 0
max_no = int(input("Please enter the max integer(< or = to 100) till you want to add = "))
while max_no > 100:
    max_no = int(input("The integer have to be less than 100 = "))
while count < max_no:
    count = count+1
    add = add+count
print("The sum of integers till", max_no, "=", add)