with open("file1.txt") as file1:
    first_list = [num.rstrip('\n') for num in file1]

with open("file2.txt") as file2:
    second_list = [num.rstrip('\n') for num in file2]

result =[int(num) for num in first_list if num in second_list]

# Write your code above 👆

print(result)


