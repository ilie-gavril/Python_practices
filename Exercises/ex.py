# Exercise 1: Reverse each word of a string

str = 'asseJ si emaN yM'
split_str = str.split()
print(split_str)
reversed_str = ''
index = len(str)
print(str[index-1])
while index > 0:
    # print(reversed_str)
    reversed_str += str[index - 1]
    index = index - 1
print(reversed_str)


a = "Hello"
a += " world"

print(a)