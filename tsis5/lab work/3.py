import re

file = open ('C:/Users/acer/Desktop/git lessin/L5/lab work/row.txt', 'r', encoding='UTF8')
result = re.findall('[a-z]+_[a-z]+', file.read())
print(result)