import re

file = open ('C:/Users/acer/Desktop/git lessin/L5/lab work/row.txt', 'r')
result = re.sub(r'[ ,.]',':', file.read())
print(result)