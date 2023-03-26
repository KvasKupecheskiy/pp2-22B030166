import re

file = open ('/Users/rustammusagaliev/Desktop/University study/semestr 2/GIT/pp2-22B030166/tsis5/lab work/row.txt', 'r')
result = re.findall('.*a.*b$', file.read())
print(result)