# Given a list of elements, the task is to count how many times a specific element appears in it. Counting occurrences is a common operation when analyzing data or checking for duplicates.

# For example:

# a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
# Count occurrences of 2 -> 4
# Count occurrences of 3 -> 3


a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
ele=2

count=0

for i in a:
    if ele==i:
        count+=1

print(f"Count occurrences of {ele} -> {count}")

