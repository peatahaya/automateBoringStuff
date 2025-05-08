def collatz(num):
    if num == 1:
        print(1)
    elif num % 2 == 0:
        num = num / 2
        if num != 1:
            collatz(num)
        else:
            return 1
    elif num % 2 == 1:
        num = (3 * num + 1)
        collatz(num)
    elif num / 2 == 1:
        return 1
    
            

while True:
    num = int(input('Enter number: '))
    collatz(num)
    if collatz(num) == 1:
        break
    