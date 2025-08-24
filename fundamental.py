# Reverse a string without using slicing ([::1])

str = 'Adil Ijaz'

reverse_str = ''
for char in str:
    reverse_str = char + reverse_str

#print(reverse_str)


# Reverse a string with using slicing ([::1])
str = 'Adil Ijaz'
reverse_str = str[::-1]
#print(reverse_str)


# Reverse a string with using reversed() function
str = 'Adil Ijaz'
reverse_str = ''.join(reversed(str))
# print(reverse_str)      

# Get the last three characters of a string
str = 'Adil Ijaz'
last_three_chars = str[-4:]
# print(last_three_chars)   


# Count the frequency of a character in a string
str = 'Adil Ijaz'
char_to_count = 'a'
frequency = str.lower().count(char_to_count.lower())
#print(frequency)

# Count the frequency of a character in a string using loop
str = 'Adil Ijaz'
char_to_count = 'a'
frequency = 0
for char in str:
    if char.lower() == char_to_count.lower():
        frequency += 1
# print(frequency)

#  Find the second largest number in the list (without using Max)
lis = [8,6,2,1,9,10]
sec_larger_num = 0
count = 0
for num in lis:
    if(num > sec_larger_num and count <= 1):
        sec_larger_num = num
        count = count + 1

#print(sec_larger_num)

#  Find the second largest number in the list (using Max)
lis = [8,6,2,1,9,10]
max_num = max(lis)
lis.remove(max_num)
sec_larger_num = max(lis)
# print(sec_larger_num)

# Flaten a nested list (without using itertools)
nested_list = [[1,2,3],[4,5],[6,7,8,9]]
flat_list = []
for sublist in nested_list:         
    for item in sublist:
        flat_list.append(item)
# print(flat_list)

# Flaten a nested list using itertools
import itertools
nested_list = [[1,2,3],[4,5],[6,7,8,9]]
flat_list = list(itertools.chain.from_iterable(nested_list))
# print(flat_list)




