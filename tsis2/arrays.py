cars = ["Ford", "volvo", "BMW"]
x = cars [0]
print (x)
cars [0] = "Toyota"
x = len(cars)
print (x, cars)
for x in cars:
    print (x)
cars.append("Honda")
for x in cars:
    print (x)
cars.pop (0)
for x in cars:
    print (x)
cars.remove ("volvo")