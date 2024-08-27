time = int(input())

fibo = [1, 1]

while len(fibo) < time:
    fibo.append(sum(fibo[-2:]))
    

distance = 0

for second in fibo:
    distance += (1/second**(1/2))*second

print(round(distance, 3))
