listnum = [8, 15, 5, 3, 2, 1, 16]
result = []

while listnum:
    # Assume the first element is the smallest
    min_value = listnum[0]
    for num in listnum:
        if num < min_value:
            min_value = num
    # Append the smallest element to the result list
    result.append(min_value)
    # Remove the smallest element from the original list
    listnum.remove(min_value)

# Print the sorted result
for i in result:
    print(i)