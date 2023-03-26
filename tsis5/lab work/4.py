import re

file = open ('/Users/rustammusagaliev/Desktop/University study/semestr 2/GIT/pp2-22B030166/tsis5/lab work/row.txt', 'r')
result = re.findall('[A-Z]{1}[a-z]+', file.read())
print(result)