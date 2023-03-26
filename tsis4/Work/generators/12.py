u = [1, 2, 3, 4, 5]
def change(u):
     for x in range(0, len(u)):
         yield u[x] + 1
         
print(u)

