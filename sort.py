import random

random.seed(1234)
data = [random.randint(1, 10000) for _ in range(10000)]
#print(data)
#test comment
with open('./output.txt', 'w') as f:
    for number in data:
        f.write(str(number) + ',')
