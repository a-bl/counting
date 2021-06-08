# What is FOR loop?

sum = 0

while True:
    n = int(input('Enter N:'))
    if n > 0:
        for num in range(1, n + 1):
            sum += num
        print(sum)
        break
    else:
        print('Enter positive integer!')
