import re

text = "hello my abbd hey ey ab"
pattern = r'[aA][bB]' # ab => bc
# r = removes all /
# \b "include all word" \d {3,3} "namely 3-th numbers"


text = re.sub(pattern, 'bc', text) #it changes the pattern where 'a' and 'b' steps it an oreder

with open('data.txt', mode='w', encoding = 'UTF-8') as f:
    f.write(text)