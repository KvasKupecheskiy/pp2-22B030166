def even_numbers():
    number = 2
    for i in range(n):
      if i % 2 == 0:
        yield i
    while True:
       yield number
       number += 2
