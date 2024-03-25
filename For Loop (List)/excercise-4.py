## Find numbers which are divisible by 7 and multiple of 5 between a range ##
## 1st Way ##
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        print(x)

## 2nd Way ##
nl = []
# Iterate through numbers from 1500 to 2700 (inclusive)
for x in range(1500, 2701):
    # Check if the number is divisible by 7 and 5 without any remainder
    if (x % 7 == 0) and (x % 5 == 0):
        # If the conditions are met, convert the number to a string and append it to the list
        nl.append(str(x))
# Join the numbers in the list with a comma and print the result
print(','.join(nl))
