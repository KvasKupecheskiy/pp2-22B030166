import re
print (dir(re))
file = open ('/Users/rustammusagaliev/Desktop/University study/semestr 2/GIT/pp2-22B030166/tsis5/lab work/row.txt', 'r')
result = re.findall(r".*а.*б.*б.*|.*а.*б.*б.*б.*", file.read())
#result = re.findall(".*a.{2}b.*", file.read())
print(result)